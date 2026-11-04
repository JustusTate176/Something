"""Pygame drawing functions."""

import pygame

from . import state
from .data import ROOMS


def draw_bar(screen, x, y, width, height, value, maximum, color):
    """Draw a background bar and the proportional filled amount."""
    pygame.draw.rect(screen, (50, 50, 50), (x, y, width, height))
    fill = max(0, int((value / maximum) * width)) if maximum else 0
    pygame.draw.rect(screen, color, (x, y, fill, height))


def draw_game(screen, font, small_font):
    """Draw the current room, player stats, inventory, messages, and controls."""
    player = state.player
    screen.fill((15, 15, 15))
    pygame.draw.rect(screen, (30, 30, 30), (15, 15, 850, 690))
    pygame.draw.rect(screen, (40, 40, 40), (885, 15, 380, 690))
    screen.blit(font.render("RESIDENT EVIL: OUTBREAK", True, (220, 60, 60)), (20, 20))
    screen.blit(font.render(f"Room: {ROOMS[state.room_index]}", True, (255, 255, 255)), (20, 70))
    draw_bar(screen, 20, 110, 300, 25, player["hp"], player["max_hp"], (255, 0, 0))
    draw_bar(screen, 20, 145, 300, 20, player["xp"], player["level"] * 100, (0, 255, 0))
    stats = [
        f"HP: {player['hp']}/{player['max_hp']}", f"Ammo: {player['ammo']}",
        f"Armor: {player['armor']}", f"Dodge: {player['dodge']}",
        f"Level: {player['level']}", f"Credits: {player['credits']}",
        f"Skill Pts: {player['skill_points']}", f"Weapon: {state.equipped_weapon}",
    ]
    for index, stat in enumerate(stats):
        screen.blit(small_font.render(stat, True, (255, 255, 255)), (900, 55 + index * 30))
    screen.blit(font.render("Inventory", True, (255, 255, 0)), (900, 300))
    for index, item in enumerate(state.inventory[-12:]):
        screen.blit(small_font.render(item, True, (220, 220, 220)), (910, 340 + index * 22))
    for index, message in enumerate(state.messages):
        screen.blit(small_font.render(message, True, (150, 255, 150)), (20, 190 + index * 24))
    if state.game_mode == "combat" and state.enemy:
        screen.blit(font.render(state.enemy.status(), True, (255, 100, 100)), (20, 620))
        draw_combat_effects(screen)
    pygame.draw.rect(screen, (25, 25, 25), (880, 500, 370, 180))
    pygame.draw.rect(screen, (100, 100, 100), (880, 500, 370, 180), 2)
    screen.blit(font.render("Controls", True, (0, 200, 255)), (900, 510))
    controls = [
        "M = Move  S = Search  H = Shop",
        "",
        "1 = Quick strike (free)",
        "2 = Aimed shot (-1 ammo)",
        "3 = Heavy shot (-2 ammo)",
        "F = Heal  R = Run  K = Skill",
        "F5/F9 = Save/Load",
    ]
    for index, control in enumerate(controls):
        screen.blit(small_font.render(control, True, (255, 255, 255)), (900, 550 + index * 16))


def draw_combat_effects(screen):
    """Animate short player shots and enemy attacks, removing expired effects."""
    now = pygame.time.get_ticks()
    duration = 320
    active_effects = []
    player_colors = {"quick": (255, 235, 120), "aimed": (100, 210, 255), "heavy": (255, 130, 50)}
    for effect in state.combat_effects:
        progress = (now - effect["started"]) / duration
        if progress >= 1:
            continue
        active_effects.append(effect)
        if effect["kind"] == "player":
            x = int(80 + progress * 640)
            color = player_colors[effect["style"]]
            pygame.draw.line(screen, color, (55, 620), (x, 620), 3)
            pygame.draw.circle(screen, color, (x, 620), 6 if effect["style"] != "heavy" else 10)
        else:
            x = int(720 - progress * 600)
            pygame.draw.line(screen, (255, 70, 70), (750, 590), (x, 590), 4)
            pygame.draw.circle(screen, (255, 110, 80), (x, 590), 8)
    state.combat_effects[:] = active_effects


def draw_menu(screen, font):
    """Draw the title screen and its available menu actions."""
    screen.fill((0, 0, 0))
    screen.blit(font.render("RESIDENT EVIL: OUTBREAK", True, (255, 0, 0)), (400, 180))
    for index, item in enumerate(["ENTER = Start Game", "L = Load Save", "ESC = Quit"]):
        screen.blit(font.render(item, True, (255, 255, 255)), (430, 320 + index * 50))


def draw_end_screen(screen, message, color, font):
    """Draw a full-screen end message in the requested color."""
    screen.fill((0, 0, 0))
    screen.blit(font.render(message, True, color), (350, 320))
