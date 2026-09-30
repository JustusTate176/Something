# This is a starship log that tests fuel levels.

# Ask the user to enter the starship's current information.
hours_cold = int(input("Enter the number of hours in cold space: "))
fuel_level = int(input("Enter the current fuel level: "))

print()
print("STARSHIP LOG")
print("Hours in cold space:", hours_cold)
print("Current fuel level:", fuel_level)

if fuel_level < 10:
    print("CRITICAL: Fuel level is dangerously low!")
elif fuel_level < 25:
    print("WARNING: Fuel level is low!")
else:
    print("Fuel level is normal.")
