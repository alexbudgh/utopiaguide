#!/usr/bin/env python3

"""Fetch and cache the latest Wayback snapshot for a forum thread id."""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch and cache the latest Wayback snapshot for a Utopia forum thread id."
    )
    parser.add_argument("thread_id", type=int, help="Forum thread id, e.g. 631144")
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=Path("/tmp/utopia-wayback-thread-cache"),
        help="Directory for cached thread HTML.",
    )
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--retry-delay", type=float, default=2.0)
    return parser.parse_args()


def latest_snapshot(thread_id: int) -> tuple[str, str]:
    query = urllib.parse.urlencode(
        {
            "url": f"https://forums.utopia-game.com/showthread.php?{thread_id}*",
            "output": "json",
            "fl": "timestamp,original,statuscode",
            "filter": "statuscode:200",
            "limit": "50",
        }
    )
    url = f"https://web.archive.org/cdx/search/cdx?{query}"
    with urllib.request.urlopen(url, timeout=30) as response:
        rows = json.load(response)
    if len(rows) <= 1:
        raise RuntimeError(f"no Wayback snapshot found for thread {thread_id}")
    latest = max(rows[1:], key=lambda row: row[0])
    return latest[0], latest[1]


def fetch(url: str, target: Path, retries: int, retry_delay: float) -> None:
    if target.exists():
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    delay = retry_delay
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            with urllib.request.urlopen(url, timeout=30) as response:
                html_text = response.read().decode("utf-8", "ignore")
            target.write_text(html_text, encoding="utf-8")
            return
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            if attempt >= retries:
                break
            time.sleep(delay)
            delay *= 2
    raise RuntimeError(f"failed to fetch {url}: {last_error}") from last_error


def main() -> int:
    args = parse_args()
    try:
        timestamp, original = latest_snapshot(args.thread_id)
    except Exception as exc:  # noqa: BLE001
        print(f"error: {exc}", file=sys.stderr)
        return 1

    cache_path = args.cache_dir / f"{args.thread_id}-{timestamp}.html"
    wayback_url = f"https://web.archive.org/web/{timestamp}/{original}"
    try:
        fetch(wayback_url, cache_path, args.retries, args.retry_delay)
    except Exception as exc:  # noqa: BLE001
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(cache_path)
    print(wayback_url)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
