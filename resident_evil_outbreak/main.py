"""Application entry point and keyboard event loop."""

import random

import pygame

from . import state
from .combat import attack, enemy_attack, spawn_boss, spawn_enemy, spawn_search_enemy
from .data import EVENTS, ROOMS
from .rendering import draw_end_screen, draw_game, draw_menu
from .systems import load_game, log, save_game, spend_skill, use_first_aid

SEARCHES_PER_ROOM = 3


def handle_key(key):
    """Apply the action for a key press and return whether the game should continue."""
    if state.game_mode == "menu":
        if key == pygame.K_RETURN:
            state.game_mode = "explore"
        elif key == pygame.K_l:
            load_game()
            state.game_mode = "explore"
        elif key == pygame.K_ESCAPE:
            return False
    elif state.game_mode in ("explore", "combat"):
        if key == pygame.K_F5:
            save_game()
        elif key == pygame.K_F9:
            load_game()
        elif state.game_mode == "explore":
            if key == pygame.K_m:
                previous_room = state.room_index
                state.room_index = min(state.room_index + 1, len(ROOMS) - 1)
                if state.room_index != previous_room:
                    state.searches_used = 0
                log(f"Entered {ROOMS[state.room_index]}")
                if random.randint(1, 100) <= 30:
                    log(random.choice(EVENTS))
                if ROOMS[state.room_index] == "Nest Core":
                    spawn_boss()
                elif random.randint(1, 100) <= 50:
                    spawn_enemy()
            elif key == pygame.K_s:
                if state.searches_used >= SEARCHES_PER_ROOM:
                    log("No searches left in this room")
                else:
                    state.searches_used += 1
                    if random.randint(1, 100) <= 20:
                        spawn_search_enemy()
                    else:
                        found = random.choice(["ammo", "credits", "nothing"])
                        if found == "ammo":
                            state.player["ammo"] += 5
                            log("Found Ammo")
                        elif found == "credits":
                            credits = random.randint(25, 75)
                            state.player["credits"] += credits
                            log(f"Found {credits} Credits")
                        else:
                            log("Nothing Found")
            elif key == pygame.K_h:
                if state.player["credits"] >= 100:
                    state.player["credits"] -= 100
                    state.inventory.append("First Aid")
                    log("Purchased First Aid")
                else:
                    log("Need 100 Credits")
        elif state.game_mode == "combat":
            if key == pygame.K_a:
                attack()
            elif key == pygame.K_1:
                attack("quick")
            elif key == pygame.K_2:
                attack("aimed")
            elif key == pygame.K_3:
                attack("heavy")
            elif key == pygame.K_f:
                use_first_aid()
            elif key == pygame.K_k:
                spend_skill()
            elif key == pygame.K_r:
                if random.randint(1, 100) <= 50:
                    state.enemy = None
                    state.game_mode = "explore"
                    log("Escaped")
                else:
                    log("Failed Escape")
                    enemy_attack()
    return True


def run():
    """Initialize Pygame and run the game's main event and drawing loop."""
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Resident Evil: Outbreak")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas", 24)
    small_font = pygame.font.SysFont("consolas", 18)
    log("Facility lockdown detected.")
    log("Reach Nest Core.")
    log("Defeat NEMESIS-X.")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                running = handle_key(event.key)
        if state.player["hp"] <= 0:
            draw_end_screen(screen, "GAME OVER", (255, 0, 0), font)
        elif state.game_mode == "menu":
            draw_menu(screen, font)
        elif state.game_mode == "victory":
            draw_end_screen(screen, "YOU ESCAPED THE FACILITY", (0, 255, 0), font)
        else:
            draw_game(screen, font, small_font)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
