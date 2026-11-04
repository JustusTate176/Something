"""Logging, progression, healing, and save-file operations."""

import json
import os

from . import state


def log(message):
    """Add a message to the on-screen log and keep it within the display limit."""
    state.messages.append(message)
    while len(state.messages) > 16:
        state.messages.pop(0)


def level_up():
    """Apply every level earned from the player's current experience."""
    needed = state.player["level"] * 100
    while state.player["xp"] >= needed:
        state.player["xp"] -= needed
        state.player["level"] += 1
        state.player["skill_points"] += 1
        state.player["max_hp"] += 20
        state.player["hp"] = state.player["max_hp"]
        log(f"LEVEL UP! ({state.player['level']})")
        log("+1 Skill Point")
        needed = state.player["level"] * 100


def spend_skill():
    """Spend one skill point to increase Vitality and maximum health."""
    if state.player["skill_points"] <= 0:
        log("No Skill Points")
        return
    state.player["skill_points"] -= 1
    state.skills["Vitality"] += 1
    state.player["max_hp"] += 10
    log("Vitality Increased")


def use_first_aid():
    """Use a First Aid item to restore up to 50 health."""
    if "First Aid" not in state.inventory:
        log("No First Aid")
        return
    state.inventory.remove("First Aid")
    state.player["hp"] = min(state.player["hp"] + 50, state.player["max_hp"])
    log("Recovered 50 HP")


def save_game():
    """Write the current player progress and room search count to disk."""
    data = {
        "player": state.player,
        "inventory": state.inventory,
        "room": state.room_index,
        "weapon": state.equipped_weapon,
        "searches_used": state.searches_used,
    }
    with open("save.json", "w", encoding="utf-8") as save_file:
        json.dump(data, save_file)
    log("Game Saved")


def load_game():
    """Restore saved player progress, inventory, room, and search count."""
    if not os.path.exists("save.json"):
        log("No Save File")
        return
    with open("save.json", "r", encoding="utf-8") as save_file:
        data = json.load(save_file)
    state.player.update(data["player"])
    state.inventory[:] = data["inventory"]
    state.room_index = data["room"]
    state.equipped_weapon = data["weapon"]
    state.searches_used = data.get("searches_used", 0)
    log("Game Loaded")
