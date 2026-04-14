# Ambush

## Why Ambush?

1. To Kill Elites (especially if your target is an orc).
   1. **Why? -->** The have an insanely low defensive value elite
   2. **Why? -->** Ambushes are 25% faster than normal attacks
2. To decrease incoming land (especially if your target is a chain target).
3. Because you're able to Ambush + Trad him and want to rub it in his face.

## Notes About Ambush

1. You can ambush each successful attack once. If you fail, too bad.
2. You cannot ambush if your opponent used War Spoils.
3. You cannot ambush if your opponent's hit was made with Anonymity on.
4. A successful ambush recaptures 50% of the land taken from you. Ambush ignores all gains modifiers.
5. Ambush inflicts 15% increased Military Casualties on the defender.
6. You ALWAYS ambush from the last hit to the first.
   1. You will ambush the last successful hit. Conquests don't count. You CAN ambush an ambush.

## How to Figure out What to Send

Take a SoM of the attacker, then check the intel site's Armies tab — it has an **Ambush** column that shows the required offense directly, so you don't need to run the formula manually unless you want to understand the math. If the target has multiple armies listed, work through them in reverse order (last hit first) and make sure you are only looking at attacks made against your province, not hits they made against other provinces.

In the War Room, make sure **Ambush** is selected as the attack type and use the ambush calculator option so the game calculates the minimum offense correctly. Enter the value from the intel site manually. Unlike other attack types, the ambush offense requirement does not change mid-tick due to modifiers like Minor Protection.

If you prefer to calculate manually:

1. Take a SoM
2. Record the value of troops out in the SoM.
3. Once you have obtained these numbers, use this formula:

```
Raw Offense Required = [(Target's Elites sent*Racial Elite Defense Value) + (Target's Offspecs Sent*Racial Defspec Value) + (Target's Soldiers sent*Racial Soldier Offense Value)] * 0.8 Remember, this is the RAW offense required - therefore, don't bother sending > 1 generals, they have no effect!
```

p.s. If you ever see a 0 in the 'army out' column, it means that he did not send ANY of that army type.

### Example

*June 4th, YR5 **call (9:11)** invaded **Kzagl (3:17)** and captured 81 acres of land.
June 4th, YR5 **I just been (9:11)** invaded **Kzagl (3:17)** and captured 139 acres of land.
June 4th, YR5 **piercing through (9:11)** invaded **Kzagl (3:17)** and captured 131 acres of land.*

**Kzagl** didn't take particularly kindly to these attacks, and thought it would be a good idea to ambush one of them, so he took a SoM of **I just been**, the largest hit against him, to see what troops had been sent out against him and whether it was a good idea to ambush.

**SOM**

*\*\* Armies #2/#3/#4 (Back in 10:46 hours) \*\**
*Ogres: 4,424 (46,308 offense / 9,485 defense)*

*Captured Land: 143 Acres*

On seeing the no specialists (goblins) and high amount of elites (ogres), Kzagl made the decision to get a few of his acres back

So, basically the target sent 4424 ogres (well, he sent a few more, but lost some in the attack) to attack **Kzagl**. If he had sent some soldiers or specialists (or both) you'd see them also in the SoM. Now we can calculate what is going to be required to successfully ambush.

Orc elites are great for attacking with, not so great for defending with. Because they only have 2 defense (note values change form age to age, this is an example only), that's what they defend with on an ambush.

```
Therefore, 4424 Elites * 2 Defense Value = 8,856
```

'The defense will fight at 80% of its normal capacity.' So, we multiply that number by 0.8

```
8,856 * 0.8 = 7084.8
```

Now, this is another important bit, when we calculate how much offense we're going to send, we don't modify it in anyway. If you're using angel's military calculator to do it, make sure you use the **RAW OFFENSE** number.

If you are just sending (5/0) offensive specialists at the target, you would require

```
7084.8/5 offspecs (send a few more to compensate for rounding error).
```

- Sending more than one general does not increase your offense.

You always ambush the last hit made against your province by that particular province. So in this case, if the paper had looked like this:
*June 4th, YR5 I just been (9:11) invaded Kzagl Elven Grave (3:17) and captured 139 acres of land.
June 4th, YR5 piercing through (9:11) invaded Kzagl Elven Grave (3:17) and captured 131 acres of land.
June 4th, YR5 I just been (9:11) invaded KZAGL ELVEN GRAVE (3:17) and captured 25 acres of land.*

You would have to ambush the hit for 25 acres before you could ambush the hit for 139 acres. You wouldn't necessarily have to be successful though, because once you've ambushed a hit by a province, you can't ambush that hit again, so the game moves onto the next hit.
