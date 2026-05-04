# Ritual

Kingdom Rituals (KR) are kingdom-wide spells that require coordinated casting to provide powerful bonuses for multiple Utopian Months. The Monarch or Steward can start, complete, or abandon a ritual. Only one KR can be active at a time, though a new one can be started before the current one expires; it replaces the active ritual when completed.

Spy on Throne and Crystal Ball show any active ritual affecting a province and its strength.

*Last updated: Age 115*

## Starting a Ritual

The Monarch or Steward chooses one of the available ritual types. Once started, the kingdom has **48 Utopian Days** to complete the ritual.

## Casting a Ritual

The kingdom must successfully cast the ritual spell at least:

```
Minimum Ritual Casts = max(45, Kingdom Provinces * 3)
```

Each ritual cast has difficulty similar to the hardest self spell, a very expensive rune cost (**Cost Multiplier 6**), and costs **2% Mana**.

A ritual can be cast beyond the minimum to increase its effect:

```
Ritual Effect = 1 + (2 * SQRT(Casts - max(45, Kingdom Provinces * 3))) / 100
```

The effect applies to all bonuses provided by the ritual. For example, Onslaught at 110% effect provides +11% Offensive Military Efficiency and +16.5% enemy casualties.

## Completing a Ritual

A ritual automatically completes **48 Utopian Days** after it is started, or it can be completed early by the Monarch or Steward once the minimum casts are reached.

Once completed, the ritual applies to all provinces in the kingdom. Its effect decays by **0.25% per tick**. Completed rituals last for at least **48 Utopian Days** and up to **120 Utopian Days**.

## Abolishing a Ritual

Enemy kingdoms can destroy completed rituals with [Abolish Ritual](../guide/Mystics.md#abolish-ritual). Rituals start at **100% strength**, and each successful Abolish Ritual cast reduces strength by **2 percentage points**. Ritual strength is separate from ritual effect; a low-strength ritual can still have more than 100% effect from extra casts.

Only the first **10 successful Abolish Ritual casts** on each province reduce ritual strength. Destroying a ritual therefore requires **50 successful casts** spread across at least **5 different provinces**.

Once a ritual reaches 0% strength, it is abolished unless it has not reached its 48 Utopian Day minimum duration. If it reaches 0% strength before then, it remains until the 48th Utopian Day and is then automatically removed.

## Ritual Types

| Ritual | Effects |
| --- | --- |
| **Ascendancy** | +50% Wizard Production · -50% Wizard Losses on Failed Spells · -25% Science Book Production |
| **Barrier** | +20% Birth Rates · -25% Damage from Enemy Instant Magic and Thievery Operations · -20% Massacre Damage · -10% Battle (Resource) Losses |
| **Benediction** | +20% Building Efficiency · -20% Draft Costs · -20% Build Costs · -20% Wages |
| **Haste** | -10% Attack Time · -25% Training Time · -25% Construction Time |
| **Havoc** | +25% Offensive WPA · +25% Offensive TPA · +20% Spell Damage · +20% Sabotage Damage |
| **Onslaught** | +10% Offensive Military Efficiency · +15% Enemy Military Casualties on Attacks |
| **Stalwart** | +5% Defensive Military Efficiency · -20% Raze Damage · -25% Military Casualties |
