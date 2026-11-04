"""Mutable run state shared by the game systems."""

player = {
    "hp": 100, "max_hp": 100, "ammo": 20, "armor": 2,
    "credits": 100, "xp": 0, "level": 1, "dodge": 10,
    "skill_points": 0,
}
skills = {"Vitality": 0, "Critical": 0}
inventory = ["Handgun"]
equipped_weapon = "Handgun"
enemy = None
messages = []
room_index = 0
game_mode = "menu"
searches_used = 0
combat_effects = []
