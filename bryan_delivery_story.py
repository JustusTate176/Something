"""A Mad Libs game with beginner challenges about strings and dictionaries."""


# A dictionary groups related information. Its string keys label each value.
bryan = {
    "name": "Bryan",
    "job": "medical courier",
    "destination": "Raccoon City",
    "package": "a medical delivery",
}


# A class is a recipe for making character objects.
class Character:
    def __init__(self, name, job, destination, package):
        # These values are strings. self.name and the others are attributes.
        self.name = name
        self.job = job
        self.destination = destination
        self.package = package

    def delivery_intro(self):
        # A method is an action the character object can perform.
        return f"{self.name} is a {self.job}. He has {self.package}."


# Make one Character object using the same details as the dictionary.
bryan_character = Character(
    bryan["name"],
    bryan["job"],
    bryan["destination"],
    bryan["package"],
)

print("BRYAN'S VERY BAD DELIVERY SHIFT: DICTIONARY TRAINING")
print("Try each challenge before Python reveals the result.\n")

# CHALLENGE 1: Input gives us a string. Use it as a dictionary key with .get().
print("CHALLENGE 1: Bryan's information desk")
detail_key = input("Type a key: name, job, destination, or package: ")
detail_value = bryan.get(detail_key, "Unknown detail")
print(f"Bryan's {detail_key} is: {detail_value}")
print("Why it works: detail_key contains text, and .get() checks whether that text matches a key in bryan.\n")

# CHALLENGE 2: Change the string stored in the variable, then look up again.
print("CHALLENGE 2: Change the delivery label")
detail_key = "job"
print('The code sets detail_key = "job". What value do you predict?')
input("Type your prediction, then press Enter: ")
print(f"With detail_key set to '{detail_key}', bryan.get(detail_key) gives: {bryan.get(detail_key)}")
detail_key = input("Change detail_key: type name, job, destination, or package: ")
print(f"Now detail_key is '{detail_key}', so the lookup gives: {bryan.get(detail_key, 'Unknown detail')} ")
print("Why it works: the dictionary stays the same, but changing the string variable makes .get() search for a different key.\n")

# CHALLENGE 3: Add a new string key and value, then predict its lookup.
print("CHALLENGE 3: Add a delivery update")
bryan["delivery_status"] = "very late"
print('We added bryan["delivery_status"] = "very late".')
input('What do you predict bryan["delivery_status"] will show? Type your prediction: ')
print(f"Python returns: {bryan['delivery_status']}")
print('Why it works: the string "delivery_status" is now a key in bryan, connected to the value "very late".\n')

# CHALLENGE 4: Predict a direct dictionary lookup using bracket notation.
print("CHALLENGE 4: Predict the job lookup")
input('Before Python looks it up, predict: what does bryan["job"] return? ')
print(f"Answer: {bryan['job']}")
print('Why it works: square brackets ask bryan for the value stored under the exact string key "job".\n')

# CHALLENGE 5: A missing key gets the backup value passed to .get().
print("CHALLENGE 5: The key that is not on the clipboard")
missing_key = "favorite_snack"
input('Predict what bryan.get("favorite_snack", "No snack listed") will show: ')
print(f"Python returns: {bryan.get(missing_key, 'No snack listed')}")
print("Why it works: there is no matching key, so .get() returns the backup value instead.\n")

# CHALLENGE 6: Let the player add their own key and value.
print("CHALLENGE 6: Add your own detail to Bryan's file")
my_key = input("Make up a key (for example, mood): ")
my_value = input("What value should that key hold? ")
bryan[my_key] = my_value
print(f"Using the string key '{my_key}' finds this value: {bryan[my_key]}")
print("Why it works: your input strings become a key and value in the dictionary. The key lets Python find its matching value.\n")

# The dictionary section used strings like "job" as keys. Now compare that
# with attributes on a Character object.
print("NOW BRYAN GETS AN OBJECT")
print("The Character class is a recipe. bryan_character is one character made from that recipe.")
print("The object's name, job, destination, and package are attributes.\n")

# CHALLENGE 7: Predict the value of an object attribute.
print("CHALLENGE 7: Read Bryan's character badge")
input("Predict what bryan_character.job will show: ")
print(f"Python returns: {bryan_character.job}")
print("Why it works: the dot and name job select the job attribute on this Character object. Its value is a string.\n")

# CHALLENGE 8: Compare a string dictionary key with an object attribute.
print("CHALLENGE 8: Same information, two ways")
input('Predict whether bryan.get("job") and bryan_character.job show the same information: ')
print(f"Dictionary lookup: {bryan.get('job')}")
print(f"Object attribute:  {bryan_character.job}")
print('Why it works: "job" is a string key inside the dictionary. job after the dot is an attribute name in the code. Both hold the same text here.\n')

# CHALLENGE 9: Call a method on the character object.
print("CHALLENGE 9: Ask Bryan for his delivery introduction")
input("Predict what bryan_character.delivery_intro() will say: ")
print(f"Bryan says: {bryan_character.delivery_intro()}")
print("Why it works: delivery_intro is a method, a named action written inside the Character class. It uses this object's string attributes to make a sentence.\n")

print("WHAT DID YOU LEARN? Answer these out loud or in a notebook:")
print('1. In bryan["job"], which part is the key?')
print("2. What does .get() return when the key is missing and you give it a backup value?")
print("3. If detail_key changes from 'job' to 'destination', what changes in the lookup?")
print("4. What does this line add to a dictionary: bryan['delivery_status'] = 'very late' ?\n")
print("5. In bryan_character.job, what is the object's attribute, and how is that different from bryan['job']?\n")

print("BRYAN'S VERY BAD DELIVERY SHIFT: MAD LIBS")

print("Now add your words to the story. input() gives us strings of text.\n")
mad_lib = {
    "adjective": input("Give me an adjective: "),
    "sound": input("Give me a noise: "),
    "excuse": input("Give me a terrible excuse: "),
    "number": input("Give me a number: "),
}

# These story parts are strings. F-strings insert dictionary values into them.
opening_scene = [
    f"{bryan_character.name} has a girlfriend named Michelle.",
    "They have a big conversation to finish.",
    "Bryan is not ready to be a dad. The night has scheduled other topics.",
    bryan_character.delivery_intro(),
    f"The package needs to go to {bryan_character.destination}.",
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
