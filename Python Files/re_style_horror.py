print("RESIDENT EVIL: NIGHT SHIFT")
print("You wake inside a locked research station.")

name = input("What is your name? ").strip() or "Rookie"

health = 3
keycard = False
turn = 0
escaped = False

while health > 0 and not escaped and turn < 5:
    print(f"\nTurn {turn + 1} | {name} | Health: {health} | Keycard: {keycard}")
    print("1. Search the medical office")
    print("2. Check the security hall")
    print("3. Try the exit door")

    choice = input("Choose 1, 2, or 3: ")

    if choice == "1":
        if not keycard:
            keycard = True
            print("You find a blue keycard under a damaged radio.")
        else:
            print("You find a first-aid spray and recover one health.")
            health = min(3, health + 1)

    elif choice == "2":
        print("A creature blocks the hall.")
        action = input("Run or hide? ").lower()

        if action == "hide":
            print("You stay silent until it passes.")
        else:
            health -= 1
            print("You escape, but lose one health.")

    elif choice == "3":
        if keycard:
            escaped = True
            print("The keycard works. You escape into the rain!")
        else:
            print("The exit is locked. You need a keycard.")

    else:
        print("That is not a valid choice. Your turn is not used.")
        continue

    turn += 1

if escaped:
    print(f"\n{name} survived the night shift.")
elif health <= 0:
    print(f"\n{name} could not escape the station.")
else:
    print(f"\nTime ran out. {name} hides until morning.")
    print("More of the station remains unexplored.")