# Game package

The complete run, control, combat, save, and build instructions are in the repository [README](../README.md).

## Modules

- `main.py` initializes Pygame and handles keyboard input.
- `state.py` stores the current run state, including per-room search usage and combat animations.
- `data.py` contains rooms, weapons, enemy templates, events, and loot.
- `enemy.py` defines the `Enemy` class.
- `combat.py` handles regular and search-triggered enemy encounters, attack choices, and combat rewards.
- `systems.py` handles logging, leveling, healing, and save/load.
- `rendering.py` draws the screens and brief attack effects.
