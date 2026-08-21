# Dice Roller

A small command-line dice roller for Dungeons & Dragons and other tabletop games. Roll one or more dice, add modifiers, and optionally enable a short suspense effect before each roll.

I started playing D&D some time and realised I didn't have any of the dice I needed. Instead of buying dice or using any online tools, I made my own dice roller program instead.

## Run it

Make sure Python 3 is installed, then run:

```bash
python dice.py
```

When prompted, choose whether to enable suspense mode with `y` or `n`.

## Commands

- `help` - Show the available commands.
- `suspense` - Toggle suspense mode on or off.
- `quit` - Exit the roller.

## Rolling dice

Use the familiar `XdY` format, where `X` is the number of dice and `Y` is the number of sides:

```text
2d6        Roll two six-sided dice
d20        Roll one twenty-sided die
2d6+3      Roll two six-sided dice and add 3
d20+d8     Roll a d20 and a d8 together
2d6+d4+-2  Roll two d20 and a d4 together and subtract 2
```

The program displays each roll, the total for each dice group, and the final total including modifiers.