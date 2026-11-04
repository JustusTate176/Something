# Resident Evil: Outbreak

Run the game from the project root with:

```powershell
python re_tb.py
```

The game is organized into modules:

- `main.py` starts Pygame and handles input.
- `state.py` stores the current run state.
- `data.py` contains rooms, weapons, enemies, events, and loot.
- `enemy.py` defines the `Enemy` class.
- `combat.py` handles enemy spawning and combat.
- `systems.py` handles logging, leveling, healing, and save files.
- `rendering.py` draws the game screens.
