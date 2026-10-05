import pygame
import random
import json
import os

pygame.init()

# =========================
# SETTINGS
# =========================

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Resident Evil: Outbreak")

clock = pygame.time.Clock()

FONT = pygame.font.SysFont("consolas", 24)
SMALL = pygame.font.SysFont("consolas", 18)

# =========================
# WORLD
# =========================

rooms = [
    "Lobby",
    "Medical Wing",
    "ICU",
    "Morgue",
    "Security Wing",
    "Armory",
    "Research Lab",
    "Mutation Chamber",
    "Generator Room",
    "Nest Core"
]

events = [
    "The lights flicker violently.",
    "A corpse falls from the ceiling.",
    "You hear something moving nearby.",
    "A distant scream echoes.",
    "The floor trembles beneath you."
]

# =========================
# PLAYER
# =========================

player = {
    "hp": 100,
    "max_hp": 100,
    "ammo": 20,
    "armor": 2,
    "credits": 100,
    "xp": 0,
    "level": 1,
    "dodge": 10,
    "skill_points": 0
}

skills = {
    "Vitality": 0,
    "Critical": 0
}

inventory = [
    "Handgun"
]

weapons = {

    "Handgun": {
        "min": 8,
        "max": 15,
        "crit": 15
    },

    "Shotgun": {
        "min": 20,
        "max": 35,
        "crit": 5
    },

    "Magnum": {
        "min": 40,
        "max": 65,
        "crit": 25
    },

    "Rocket Launcher": {
        "min": 120,
        "max": 200,
        "crit": 0
    }
}

loot_table = [
    "Ammo",
    "Ammo",
    "Ammo",
    "First Aid",
    "Shotgun",
    "Magnum"
]

equipped_weapon = "Handgun"

# =========================
# GAME STATE
# =========================

enemy = None
messages = []
room_index = 0
state = "menu"

# =========================
# ENEMIES
# =========================

enemy_pool = [

    {
        "name": "Zombie",
        "hp": 40,
        "damage": [1, 6],
        "xp": 25
    },

    {
        "name": "Crawler",
        "hp": 60,
        "damage": [5, 10],
        "xp": 50
    },

    {
        "name": "Hunter",
        "hp": 120,
        "damage": [10, 15],
        "xp": 100
    },

    {
        "name": "Licker",
        "hp": 150,
        "damage": [15, 25],
        "xp": 150
    }
]

boss = {
    "name": "NEMESIS-X",
    "hp": 500,
    "damage": [30, 40],
    "xp": 1000
}

# =========================
# LOGGING
# =========================

def log(text):

    messages.append(text)

    while len(messages) > 16:
        messages.pop(0)

# =========================
# LEVELING
# =========================

def level_up():

    needed = player["level"] * 100

    while player["xp"] >= needed:

        player["xp"] -= needed
        player["level"] += 1
        player["skill_points"] += 1

        player["max_hp"] += 20
        player["hp"] = player["max_hp"]

        log(f"LEVEL UP! ({player['level']})")
        log("+1 Skill Point")

        needed = player["level"] * 100

# =========================
# SKILLS
# =========================

def spend_skill():

    if player["skill_points"] <= 0:
        log("No Skill Points")
        return

    player["skill_points"] -= 1
    skills["Vitality"] += 1
    player["max_hp"] += 10

    log("Vitality Increased")

# =========================
# HEALING
# =========================

def use_first_aid():

    if "First Aid" not in inventory:
        log("No First Aid")
        return

    inventory.remove("First Aid")

    player["hp"] += 50

    if player["hp"] > player["max_hp"]:
        player["hp"] = player["max_hp"]

    log("Recovered 50 HP")

# =========================
# SAVE / LOAD
# =========================

def save_game():

    data = {
        "player": player,
        "inventory": inventory,
        "room": room_index,
        "weapon": equipped_weapon
    }

    with open("save.json", "w") as f:
        json.dump(data, f)

    log("Game Saved")

def load_game():

    global room_index
    global equipped_weapon

    if not os.path.exists("save.json"):
        log("No Save File")
        return

    with open("save.json", "r") as f:
        data = json.load(f)

    player.update(data["player"])

    inventory.clear()
    inventory.extend(data["inventory"])

    room_index = data["room"]
    equipped_weapon = data["weapon"]

    log("Game Loaded")

# =========================
# COMBAT
# =========================

def spawn_enemy():

    global enemy
    global state

    enemy = random.choice(enemy_pool).copy()

    if random.randint(1, 100) <= 10:

        enemy["name"] = "Elite " + enemy["name"]
        enemy["hp"] *= 2
        enemy["damage"][0] += 10
        enemy["xp"] *= 2

        log("ELITE ENEMY!")

    state = "combat"

    log(f"A {enemy['name']} appears!")

def spawn_boss():

    global enemy
    global state

    enemy = boss.copy()

    state = "combat"

    log("NEMESIS-X HAS AWAKENED")

def enemy_attack():

    dodge_roll = random.randint(1, 100)

    if dodge_roll <= player["dodge"]:
        log("DODGED!")
        return

    if enemy and enemy["name"] == "NEMESIS-X":

        if random.randint(1, 100) <= 25:

            player["hp"] -= 40

            log("NEMESIS SMASH!")

            return

    if isinstance(enemy["damage"], list):

        base_damage = random.randint(
            enemy["damage"][0],
            enemy["damage"][1]
        )

    else:

        base_damage = enemy["damage"]

    damage = max(
        1,
        base_damage - player["armor"]
    )

    player["hp"] -= damage

    log(
        f"{enemy['name']} deals {damage}"
    )

def attack():

    global enemy
    global state

    weapon = weapons[equipped_weapon]

    damage = random.randint(
        weapon["min"],
        weapon["max"]
    )

    crit = weapon["crit"] + skills["Critical"] * 2

    if random.randint(1, 100) <= crit:

        damage *= 2

        log("CRITICAL HEADSHOT!")

    if equipped_weapon == "Magnum":
        damage += 15

    enemy["hp"] -= damage

    log(f"You deal {damage}")

    if (
        enemy["name"] == "NEMESIS-X"
        and enemy["hp"] <= 250
        and not enemy.get("phase2")
    ):

        enemy["phase2"] = True

        enemy["damage"] += 15

        log("NEMESIS MUTATES!")

    if enemy["hp"] <= 0:

        log(f"{enemy['name']} defeated")

        player["xp"] += enemy["xp"]

        credits = random.randint(25, 75)
        player["credits"] += credits

        log(f"+{credits} credits")

        level_up()

        drop = random.choice(loot_table)
        inventory.append(drop)

        log(f"Dropped: {drop}")

        if enemy["name"] == "NEMESIS-X":

            state = "victory"

        else:

            state = "explore"

        enemy = None
        return

    enemy_attack()

# =========================
# DRAW HELPERS
# =========================

def draw_bar(x, y, w, h, value, maximum, color):

    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (x, y, w, h)
    )

    fill = max(
        0,
        int((value / maximum) * w)
    )

    pygame.draw.rect(
        screen,
        color,
        (x, y, fill, h)
    )

# =========================
# DRAW GAME
# =========================

def draw_game():

    screen.fill((15, 15, 15))

    pygame.draw.rect(
        screen,
        (30, 30, 30),
        (15, 15, 850, 690)
    )

    pygame.draw.rect(
        screen,
        (40, 40, 40),
        (885, 15, 380, 690)
    )

    title = FONT.render(
        "RESIDENT EVIL: OUTBREAK",
        True,
        (220, 60, 60)
    )

    screen.blit(title, (20, 20))

    room_text = FONT.render(
        f"Room: {rooms[room_index]}",
        True,
        (255, 255, 255)
    )

    screen.blit(room_text, (20, 70))

    draw_bar(
        20, 110, 300, 25,
        player["hp"],
        player["max_hp"],
        (255, 0, 0)
    )

    xp_needed = player["level"] * 100

    draw_bar(
        20, 145, 300, 20,
        player["xp"],
        xp_needed,
        (0, 255, 0)
    )

    stats = [
        f"HP: {player['hp']}/{player['max_hp']}",
        f"Ammo: {player['ammo']}",
        f"Armor: {player['armor']}",
        f"Dodge: {player['dodge']}",
        f"Level: {player['level']}",
        f"Credits: {player['credits']}",
        f"Skill Pts: {player['skill_points']}",
        f"Weapon: {equipped_weapon}"
    ]

    y = 55

    for stat in stats:

        screen.blit(
            SMALL.render(
                stat,
                True,
                (255,255,255)
            ),
            (900,y)
        )

        y += 30

    screen.blit(
        FONT.render(
            "Inventory",
            True,
            (255,255,0)
        ),
        (900,300)
    )

    y = 340

    for item in inventory[-12:]:

        screen.blit(
            SMALL.render(
                item,
                True,
                (220,220,220)
            ),
            (910,y)
        )

        y += 22

    y = 190

    for msg in messages:

        screen.blit(
            SMALL.render(
                msg,
                True,
                (150,255,150)
            ),
            (20,y)
        )

        y += 24

    if state == "combat" and enemy:

        combat_text = FONT.render(
            f"{enemy['name']} HP: {enemy['hp']}",
            True,
            (255,100,100)
        )

        screen.blit(
            combat_text,
            (20,620)
        )

    pygame.draw.rect(
        screen,
        (25,25,25),
        (880,500,370,180)
    )

    pygame.draw.rect(
        screen,
        (100,100,100),
        (880,500,370,180),
        2
    )

    screen.blit(
        FONT.render(
            "Controls",
            True,
            (0,200,255)
        ),
        (900,510)
    )

    controls = [
        "M = Move",
        "S = Search",
        "H = Merchant",
        "",
        "A = Attack",
        "F = Heal",
        "R = Run",
        "",
        "K = Spend Skill",
        "F5 = Save",
        "F9 = Load"
    ]

    y = 550

    for c in controls:

        screen.blit(
            SMALL.render(
                c,
                True,
                (255,255,255)
            ),
            (900,y)
        )

        y += 16

# =========================
# MENU
# =========================

def draw_menu():

    screen.fill((0,0,0))

    title = FONT.render(
        "RESIDENT EVIL: OUTBREAK",
        True,
        (255,0,0)
    )

    screen.blit(title,(400,180))

    menu = [
        "ENTER = Start Game",
        "L = Load Save",
        "ESC = Quit"
    ]

    y = 320

    for item in menu:

        screen.blit(
            FONT.render(
                item,
                True,
                (255,255,255)
            ),
            (430,y)
        )

        y += 50

# =========================
# START
# =========================

log("Facility lockdown detected.")
log("Reach Nest Core.")
log("Defeat NEMESIS-X.")

# =========================
# MAIN LOOP
# =========================

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if state == "menu":

                if event.key == pygame.K_RETURN:
                    state = "explore"

                elif event.key == pygame.K_l:
                    load_game()
                    state = "explore"

                elif event.key == pygame.K_ESCAPE:
                    running = False

            elif state in ["explore","combat"]:

                if event.key == pygame.K_F5:
                    save_game()

                elif event.key == pygame.K_F9:
                    load_game()

                elif state == "explore":

                    if event.key == pygame.K_m:

                        room_index += 1

                        if room_index >= len(rooms):
                            room_index = len(rooms)-1

                        log(f"Entered {rooms[room_index]}")

                        if random.randint(1,100) <= 30:
                            log(random.choice(events))

                        if rooms[room_index] == "Nest Core":
                            spawn_boss()

                        elif random.randint(1,100) <= 50:
                            spawn_enemy()

                    elif event.key == pygame.K_s:

                        found = random.choice(
                            ["ammo","credits","nothing"]
                        )

                        if found == "ammo":
                            player["ammo"] += 5
                            log("Found Ammo")

                        elif found == "credits":

                            c = random.randint(25,75)

                            player["credits"] += c

                            log(f"Found {c} Credits")

                        else:

                            log("Nothing Found")

                    elif event.key == pygame.K_h:

                        if player["credits"] >= 100:

                            player["credits"] -= 100

                            inventory.append("First Aid")

                            log("Purchased First Aid")

                        else:

                            log("Need 100 Credits")

                elif state == "combat":

                    if event.key == pygame.K_a:
                        attack()

                    elif event.key == pygame.K_f:
                        use_first_aid()

                    elif event.key == pygame.K_k:
                        spend_skill()

                    elif event.key == pygame.K_r:

                        if random.randint(1,100) <= 50:

                            enemy = None
                            state = "explore"

                            log("Escaped")

                        else:

                            log("Failed Escape")

                            enemy_attack()

    if player["hp"] <= 0:

        screen.fill((0,0,0))

        text = FONT.render(
            "GAME OVER",
            True,
            (255,0,0)
        )

        screen.blit(text,(520,340))

    elif state == "menu":

        draw_menu()

    elif state == "victory":

        screen.fill((0,0,0))

        text = FONT.render(
            "YOU ESCAPED THE FACILITY",
            True,
            (0,255,0)
        )

        screen.blit(text,(350,320))

    else:

        draw_game()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()