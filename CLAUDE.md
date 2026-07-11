# CLAUDE.md

Project-specific guidance for editing the Utopia Guide docs.

## Building and previewing

- MkDocs is installed in the project's `.venv`, not globally. Always
  `source .venv/bin/activate` before running `mkdocs build` or
  `mkdocs serve`.
- Run `mkdocs build --strict` after editing docs to catch broken
  internal links and nav entries before considering the change done.

## Ingesting a new age

When given raw patch-notes text for a new age (e.g. a pasted forum post
or changelog), reproduce the pattern used for the most recent prior
age:

1. Read the previous age's page (e.g. `history/Age_N-1.md`) to confirm
   the current subsection layout and heading order before writing the
   new one — the pattern drifts slightly age to age.
2. Create `history/Age_N.md`: intro bullets (WoL Open/Start/End dates,
   plus any timeline/schedule info given), a "Changes from Age N-1"
   bullet summary linking to the three comparison docs below, then the
   full reference sections (Core Mechanic Changes, Dragons, Rituals if
   changed, Races, Personalities) with absolute Age N values — not
   diffs.
3. Create the three diff-only comparison docs, showing only rows that
   changed (unchanged stats are omitted per the established pattern):
   - `history/Race_Comparison_N-1_N.md`
   - `history/Personality_Comparison_N-1_N.md`
   - `history/Dragons_Rituals_Comparison_N-1_N.md`
   Use `<span class="bonus">`/`<span class="penalty">`/
   `<span class="badge-new">New</span>` spans to mark changed values,
   matching the existing comparison docs' styling.
4. Note new/removed/reintroduced races and personalities explicitly
   (an admonition works well) rather than silently omitting them from
   a diff table, since they have no prior-age baseline to diff against.
5. Wire the four new files into `mkdocs.yml`'s nav (both under
   `Comparisons` and `Ages`), and add the new age's row to
   `history/Ages_Index.md` if missing.
6. Update `docs/index.md`'s "Current Age" link and highlights
   admonition to point at the new age.
7. Run `mkdocs build --strict` to verify before reporting done.

## Markdown and MkDocs gotchas

- MkDocs uses Python-Markdown, which is stricter than GitHub-flavored
  Markdown in a few places.
- Nested list items should use 4-space indentation per level. Two-space
  indentation may render as a single flat `<ul>` instead of nested
  lists.
- If a nested list still renders poorly, prefer a flatter structure or
  real headings instead of forcing deep nesting.
- Avoid placeholder self-links like `(#)` and self-referential links to
  the current page. Convert them to real links or plain text.
- Prefer real Markdown headings over bold pseudo-headings.
- MkDocs admonitions are available and already used on the site. Use
  `!!! note "Title"`, `!!! tip "Title"`, `!!! info "Title"`, or
  `!!! example "Title"` with 4-space-indented body content for
  editorial sidebars, cautions, and callouts.
- Prefer real Markdown tables only for genuinely row/column data. If a
  table is just being used for layout, convert it to headings or lists.
- For historical age pages, avoid duplicating the same material in both
  early summary sections and later reference sections. Keep one
  canonical presentation.

## Historical age docs

- Use the more modern reference-style layout for `Races` and
  `Personalities` when feasible.
- Typical race subsections: `Bonuses`, `Penalties`, `Spell Book`,
  `Operation Access`, `Special Access`, `Units`.
- Typical personality subsections: `Bonuses`, `Spell Book`,
  `Starting Bonuses`, and other clearly named access sections where
  needed.
- Keep `Rituals` and `Dragons` near each other when both are present.
- If a `Rituals` section merely points to content elsewhere on the same
  page, remove the duplicate stub instead of keeping both.
- Use bullet summaries instead of wide one-row tables for stances,
  relations, dragons, and similar dense summaries when the table is hard
  to read on narrow screens.
- If an age page is only a placeholder forum link, prefer replacing it
  with a full local archive from the forum or Wayback rather than
  keeping a thin outbound link.
- The live forum is flaky. Prefer using the repo helpers under
  `scripts/`:
  `fetch_forum_page.sh`, `fetch_wayback_thread.py`, and
  `extract_forum_post.py`.
- If a recovered forum post is structured as `Age N` compared against
  `Age N-1`, preserve that comparison shape explicitly with `#### Age N`
  and `#### Age N-1` subsections instead of flattening the old values
  into prose.
- For recovered forum-backed age pages, keep the content materially
  intact while normalizing headings, bullets, and labels to match the
  surrounding age-doc style.
