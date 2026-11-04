"""Enemy spawning and combat actions."""

import random

import pygame

from . import state
from .data import BOSS_TEMPLATE, ENEMY_TEMPLATES, LOOT_TABLE, WEAPONS
from .enemy import Enemy
from .systems import level_up, log


def spawn_enemy():
    """Spawn a random regular enemy, with a chance to make it elite."""
    template = random.choice(ENEMY_TEMPLATES)
    state.enemy = Enemy(
        template["name"], template["hp"], template["damage"].copy(), template["xp"]
    )
    if random.randint(1, 100) <= 10:
        state.enemy.name = "Elite " + state.enemy.name
        state.enemy.hp *= 2
        state.enemy.damage[0] += 10
        state.enemy.xp *= 2
        log("ELITE ENEMY!")
    state.game_mode = "combat"
    log(f"A {state.enemy.name} appears!")


def spawn_search_enemy():
    """Spawn a Zombie or Crawler when a search disturbs something nearby."""
    template = random.choice(ENEMY_TEMPLATES[:2])
    state.enemy = Enemy(
        template["name"], template["hp"], template["damage"].copy(), template["xp"]
    )
    state.game_mode = "combat"
    log("Something lunges out while you search!")
    log(f"A {state.enemy.name} appears!")


def spawn_boss():
    """Create the Nemesis boss encounter."""
    state.enemy = Enemy(
        BOSS_TEMPLATE["name"], BOSS_TEMPLATE["hp"],
        BOSS_TEMPLATE["damage"].copy(), BOSS_TEMPLATE["xp"]
    )
    state.game_mode = "combat"
    log("NEMESIS-X HAS AWAKENED")


def enemy_attack():
    """Resolve the active enemy's attack against the player."""
    enemy = state.enemy
    state.combat_effects.append({"kind": "enemy", "started": pygame.time.get_ticks()})
    if random.randint(1, 100) <= state.player["dodge"]:
        log("DODGED!")
        return
    if enemy and enemy.name == "NEMESIS-X" and random.randint(1, 100) <= 25:
        state.player["hp"] -= 40
        log("NEMESIS SMASH!")
        return
    base_damage = random.randint(*enemy.damage) if isinstance(enemy.damage, list) else enemy.damage
    damage = max(1, base_damage - state.player["armor"])
    state.player["hp"] -= damage
    log(f"{enemy.name} deals {damage}")


def attack(style="quick"):
    """Resolve a quick strike, aimed shot, or heavy shot and enemy retaliation."""
    enemy = state.enemy
    ammo_costs = {"quick": 0, "aimed": 1, "heavy": 2}
    damage_multipliers = {"quick": 1.0, "aimed": 1.2, "heavy": 1.75}
    ammo_cost = ammo_costs[style]
    if state.player["ammo"] < ammo_cost:
        log(f"Not enough ammo for a {style} shot")
        return
    state.player["ammo"] -= ammo_cost
    state.combat_effects.append({"kind": "player", "style": style, "started": pygame.time.get_ticks()})
    weapon = WEAPONS[state.equipped_weapon]
    damage = int(random.randint(weapon["min"], weapon["max"]) * damage_multipliers[style])
    crit = weapon["crit"] + state.skills["Critical"] * 2
    if style == "aimed":
        crit += 20
    elif style == "heavy":
        crit = max(0, crit - 5)
    if random.randint(1, 100) <= crit:
        damage *= 2
        log("CRITICAL HEADSHOT!")
    if state.equipped_weapon == "Magnum":
        damage += 15
    enemy.hp -= damage
    log(f"You deal {damage}")
    if enemy.name == "NEMESIS-X" and enemy.hp <= 250 and not enemy.phase2:
        enemy.phase2 = True
        enemy.damage = [value + 15 for value in enemy.damage]
        log("NEMESIS MUTATES!")
    if enemy.hp <= 0:
        log(f"{enemy.name} defeated")
        state.player["xp"] += enemy.xp
        credits = random.randint(25, 75)
        state.player["credits"] += credits
        log(f"+{credits} credits")
        level_up()
        drop = random.choice(LOOT_TABLE)
        state.inventory.append(drop)
        log(f"Dropped: {drop}")
        state.game_mode = "victory" if enemy.name == "NEMESIS-X" else "explore"
        state.enemy = None
        return
    enemy_attack()
