ROOMS = [
    "Lobby", "Medical Wing", "ICU", "Morgue", "Security Wing",
    "Armory", "Research Lab", "Mutation Chamber", "Generator Room",
    "Nest Core",
]

EVENTS = [
    "The lights flicker violently.",
    "A corpse falls from the ceiling.",
    "You hear something moving nearby.",
    "A distant scream echoes.",
    "The floor trembles beneath you.",
]

WEAPONS = {
    "Handgun": {"min": 8, "max": 15, "crit": 15},
    "Shotgun": {"min": 20, "max": 35, "crit": 5},
    "Magnum": {"min": 40, "max": 65, "crit": 25},
    "Rocket Launcher": {"min": 120, "max": 200, "crit": 0},
}
LOOT_TABLE = ["Ammo", "Ammo", "Ammo", "First Aid", "Shotgun", "Magnum"]
ENEMY_TEMPLATES = [
    {"name": "Zombie", "hp": 40, "damage": [1, 6], "xp": 25},
    {"name": "Crawler", "hp": 60, "damage": [5, 10], "xp": 50},
    {"name": "Hunter", "hp": 120, "damage": [10, 15], "xp": 100},
    {"name": "Licker", "hp": 150, "damage": [15, 25], "xp": 150},
]
BOSS_TEMPLATE = {"name": "NEMESIS-X", "hp": 500, "damage": [30, 40], "xp": 1000}
