print("=" * 52)
print("       🐾 WELCOME TO THE CORGI SORTING HAT 🐾")
print("=" * 52)

dog_name = input("What is your corgi's name?: ").strip().title()
weight = int(input(f"How much does {dog_name} weigh in pounds?: "))

# Stop only if the scale reading is invalid
if weight <= 0:
    print("\n" + "!" * 52)
    print("⚠️  ERROR: CHECK THE SCALE AND REWEIGH THE CORGI!")
    print("!" * 52)
    exit()

high_energy = int(
    input(f"Is {dog_name} high energy? (1 = yes, 0 = no): ")
)

# Stop if the energy answer is invalid
if high_energy != 0 and high_energy != 1:
    print("\n⚠️ ERROR: Please enter only 1 for yes or 0 for no.")
    exit()

print("\n" + "✨" * 26)
print("The Sorting Hat is examining your corgi...")
print("✨" * 26)

if weight < 20 and high_energy == 1:
    yard = "⚡ ZOOMIES YARD ⚡"
    message = "Small, speedy, and ready to run!"

elif weight < 20 and high_energy == 0:
    yard = "🧸 PUPPY LOUNGE 🧸"
    message = "A cozy spot for a calm little corgi!"

elif weight >= 20 and high_energy == 1:
    yard = "🚀 BIG DOG RUN 🚀"
    message = "A powerful corgi needs room to zoom!"

else:
    yard = "💤 NAP PORCH 💤"
    message = "The perfect place for a relaxing afternoon!"

print("\n" + "=" * 52)
print(f"              SORTING RESULTS FOR {dog_name.upper()}")
print("=" * 52)
print(f"Weight: {weight} pounds")
print(f"Assigned play-yard: {yard}")
print(f"Sorting Hat says: {message}")
print("=" * 52)
print(f"🐾 Have fun, {dog_name}! 🐾")
