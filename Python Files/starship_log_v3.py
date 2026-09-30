# ============================================================
#              AEGIS-7 STARSHIP COMMAND CONSOLE
# ============================================================

ship_name = "Tai Ceti 55"
captain_name = "Your MOther"
hours_cold = int(input("Enter hours traveled through cold space: "))
fuel_level = int(input("Enter current fuel level (0-100): "))

print()
print("============================================================")
print("           AEGIS-7 DEEP SPACE MISSION REPORT")
print("============================================================")
print("STARSHIP:        ", ship_name.upper())
print("COMMANDING OFFICER:", captain_name)
print("COLD-SPACE HOURS:", hours_cold)
print("FUEL RESERVES:   ", str(fuel_level) + "%")
print("------------------------------------------------------------")

# Check the starship's fuel reserves.
if fuel_level < 10:
    print("[RED ALERT] Fuel reserves are critically low!")
    print("[ACTION REQUIRED] Initiate emergency refueling protocol!")
elif fuel_level < 25:
    print("[WARNING] Fuel reserves are running low.")
    print("[RECOMMENDATION] Locate the nearest refueling station.")
else:
    print("[SYSTEM OK] Fuel reserves are within safe limits.")

print("------------------------------------------------------------")

# Check how long the ship has been in cold space.
if hours_cold > 48:
    print("[RED ALERT] Maximum cold-space exposure exceeded!")
    print("[ACTION REQUIRED] Exit cold space immediately!")
elif hours_cold == 48:
    print("[WARNING] The ship has reached its 48-hour exposure limit!")
    print("[ACTION REQUIRED] Prepare to leave cold space.")
else:
    hours_remaining = 48 - hours_cold
    print("[SYSTEM OK] Cold-space exposure remains within safe limits.")
    print("[TIME REMAINING]", hours_remaining, "hours")

print("------------------------------------------------------------")

# Display a final mission status.
if fuel_level < 10 or hours_cold > 48:
    print("MISSION STATUS: CRITICAL")
    print("Commander, immediate action is required!")
elif fuel_level < 25 or hours_cold == 48:
    print("MISSION STATUS: CAUTION")
    print("Commander, monitor ship systems carefully.")
else:
    print("MISSION STATUS: ALL SYSTEMS NOMINAL")
    print("The vessel is cleared to continue its mission.")

print("============================================================")
print("             END OF STARSHIP TRANSMISSION")
print("============================================================")
