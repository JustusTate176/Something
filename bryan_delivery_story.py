"""Stage 3: learn how strings can find information in dictionaries."""


# A dictionary groups related information. Its string keys label each value.
bryan = {
    "name": "Bryan",
    "job": "medical courier",
    "destination": "Raccoon City",
    "package": "a medical delivery",
}

print("BRYAN'S VERY BAD DELIVERY SHIFT: MAD LIBS")
print("First, let's use a string to look up one of Bryan's details.\n")

# This variable contains a string. We use that string as the dictionary key.
detail_key = input("Choose a detail (name, job, destination, package): ")
detail_key = detail_key.strip().lower()

# .get() looks up a key. If it isn't present, it gives us the backup text.
detail_value = bryan.get(detail_key, "I don't know that detail")
print(f"Bryan's {detail_key}: {detail_value}\n")

print("Now add your words to the story. input() gives us strings of text.\n")
mad_lib = {
    "adjective": input("Give me an adjective: "),
    "sound": input("Give me a noise: "),
    "excuse": input("Give me a terrible excuse: "),
    "number": input("Give me a number: "),
}

# These story parts are strings. F-strings insert dictionary values into them.
opening_scene = [
    f"{bryan['name']} has a girlfriend named Michelle.",
    "They have a big conversation to finish.",
    "Bryan is not ready to be a dad. The night has scheduled other topics.",
    f"{bryan['name']} is a {bryan['job']}. He has {bryan['package']}.",
    f"The package needs to go to {bryan['destination']}.",
    "It is snowing. This is not the main problem.",
    "The main problem is that Raccoon City is having a terrible night.",
    f"Bryan nearly hits a sick woman. She makes a {mad_lib['adjective']} sound: {mad_lib['sound']}!",
    "A police officer is dead. Bryan takes the officer's gun.",
    f"Bryan now has protection. It has {mad_lib['number']} bullets and no customer support.",
    "There are infected people everywhere.",
    f"Bryan explains the situation to himself: '{mad_lib['excuse']}'",
    "Bryan still has the package.",
    "The delivery is going poorly.",
]

print("\nTHE STORY\n")
for sentence in opening_scene:
    print(sentence)
