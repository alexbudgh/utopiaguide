# MunkBot

### MunkBot

MunkBot is a new developer tool that was introduced in [Age 71](../history/Age_71.md). This tool has been created in particular for third-party targetfinders to operate more efficiently, without stressing the Utopia servers. Any targetfinders found running that scrape the Utopia kingdom pages are going to be banned.

The tool updates every 15 minutes (but offset from the tick, so at 5, 20, 35, and 50 minutes into the hour), and contains the following information:

- Kingdom-level:
  - Location
  - Number of provinces
  - Kingdom name
  - Stance
  - Wars
  - Kingdom Land
  - Kingdom NW
  - Kingdom honor

- Province-level:
  - Location
  - Land
  - Province name
  - Protection status
  - Race
  - Honor Rank (e.g. lord, baron -- not the numerical value)
  - Networth

### Setting up MunkBot for the Kingdom

If you would like access to the tool, reach out to ChristianM@Utopia-Game.com, and include who you are and what you intend to use it for. Access will only be denied if you are banned for play violations or past activities.

### Setting up MunkBot for an individual Province

Once your kingdom account has been created and the kingdom contact has created a username for each player, you will access your MunkBot account by going to the respective website (xxx.umunk.net) then click to setup your password.

- Username is the IRC nickname that a bot admin has added. This may not exceed 16 characters in length.
- Password must contain only numbers and letters and must be a minimum of 8 characters in length.
  - **Passwords can only be set once. They can never be reset or changed.** Therefore, you must type it twice for verification.

### Adding intel to MunkBot

There are two ways to update your province information to MunkBot. They are:

- Manually:
  - Log into your MunkBot account (xxx.umunk.net) and paste the raw intel in the top right box

OR

- Automatically:
  - Once ingame (eg Throne page), press the Preferences link.
  - Click "Set munkbot" and write resurgence (Do not write the full url)
  - Go to your throne and notice that below your navigation pane to the left, you now have the option to open munkbot and to disable it.
  - Press munkbot to enable.
  - Navigate to the various pages that information is pulled from to update your details (Throne, Military, Buildings, Science, Mystic page with current spells)
  - Additional information that can be uploaded includes the Kingdom page, Province News and Kingdom News

### Adding intel to MunkBot

Once ingame, press the Disable Munkbot button or disable text. This will disable the script until you enable it again by clicking the munkbot text again.

---

## Bot Commands

!!! warning "Known limitation"
    Do **not** trust the `.bush` command — it does not account for new troop values. Always take bush value from the new intelsite instead.

### Aid

| Command | Description |
|---|---|
| `.aid [amount] [type] [comment]` | Request aid |
| `.aidfor [prov] [amount] [type] [comment]` | Request aid for someone else |
| `.delaid [user]` | Delete a requested aid |

### Armies

| Command | Description |
|---|---|
| `.eta [user]` | Check a province's army home time |
| `.def [user]` | Check a province's defense based on latest intel |
| `.bush [user]` | Calculate ambush send amount (**do not trust** — see warning above) |
| `.plunders` | Check which kingdoms recently exited EoWCF |
| `.etalist` | List incoming armies |
| `.etalist war` | List incoming enemy armies |

**Intel commands (PM)** — bot sends results via private message:

| Command | Description |
|---|---|
| `.sot [user]` | Check SoT |
| `.som [user]` | Check SoM |
| `.sur [user]` | Check survey |
| `.sos [user]` | Check science |

**Intel commands (channel)** — bot displays results in channel:

| Command | Description |
|---|---|
| `.sotc [user]` | Check SoT |
| `.somc [user]` | Check SoM |
| `.surc [user]` | Check survey |
| `.sosc [user]` | Check science |

### Kingdom Stats

| Command | Description |
|---|---|
| `.bestgains [location] [province]` | Check which province in that kingdom is the given province's best gains target |
| `.kdeconwar` | Check enemy kingdom total income |
| `.kdecon` | Check own kingdom total income |
| `.mintime` | Check when WD mintime is |
| `.notactivesince [hrs]` | List users who were **not** active within the given hours |
| `.dragon` | Check dragon funding details |
| `.dragon [amount]` | Show funding based on the given number of hours |
| `.dragonsent` | Check dragon killing details |
| `.dragonsent [amount]` | Show killing details for the past given hours |
| `.ritual` | Check ritual casting details |
| `.ops[hr] [prov name]` | Show ops activity of that province for the last X hours |
| `.ops[hr] [loc]` | Show ops done by a kingdom in the last X hours |
| `.list [stat] [race/pers]` | List every province's stat in your kingdom |
| `.listwar [stat] [race/pers]` | List every province's stat in enemy kingdom |

**Available stats for `.list` / `.listwar`:** `gc`, `gcpa`, `mtpa`, `mwpa`, `tpa`, `wpa`, `epa`, `dspa`, `ospa`, `opa`, `popa`, `off`, `poff`, `dpa`, `pdpa`, `pdef`, `totalbooks`, `bpa`, `wages`, `food`, `rune`, `solds`, `spa`, `tb`, `peons`, `ppa`, `stealth`, `mana`, `mpa`, `draft`, `poppa`, `income`, `intel` (SoT age)

### Province

| Command | Description |
|---|---|
| `.farms` | Check the optimum number of farms required |
| `.econ` | Check province econ stats |
| `.prophet` | Check future stats when everything is built and trained |
| `.income` | Check province income |
| `.wpacalc` | NW breakdown of your province; also calculates rWPA from NW (requires survey, SoS, and SoT) |
| `.time` | Display current Utopian time |
| `.eff [building] [amount] [BE]` | Show the effects of a building at a given amount and BE |
| `.soldswap [user]` | Show how many soldiers you can send before the province goes into troop overpop |
| `.max eff [be]` | Show the max buildings needed for maximum effect at a given efficiency |
