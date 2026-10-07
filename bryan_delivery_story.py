"""An interactive Mad Libs lesson about Python strings and object-oriented code.

Run with: python bryan_delivery_story.py

The game introduces one idea at a time, asks you to predict what Python will
do, and then uses the same ideas to build Bryan's delivery story.
"""


def reveal(prompt, answer, explanation):
    """Give the player a moment to predict before showing an answer."""
    input(prompt + "\nYour prediction (press Enter to reveal): ")
    print("Python says:", answer)
    print("Why:", explanation, "\n")


def get_word(prompt):
    """Read a non-empty word from the player and return it as a string."""
    while True:
        word = input(prompt).strip()
        if word:
            return word
        print("Please type at least one character. Try again.")


class Character:
    """A recipe for character objects: data (attributes) plus behavior (methods)."""

    def __init__(self, name, job, destination, package):
        # input() and quoted text are strings. These become this object's data.
        self.name = name
        self.job = job
        self.destination = destination
        self.package = package
        self.status = "ready for a difficult shift"

    def introduce(self):
        """Build and return a new string using this character's attributes."""
        return f"{self.name} is a {self.job}. He has {self.package}."

    def change_destination(self, new_destination):
        """Update one attribute; strings cannot be edited in place."""
        self.destination = new_destination

    def deliver(self):
        """Change the character's state and report the result as a string."""
        self.status = f"delivering the package to {self.destination}"
        return f"{self.name} is now {self.status}."


def teach_strings():
    print("BRYAN'S VERY BAD DELIVERY SHIFT")
    print("A hands-on lesson in strings and object-oriented programming\n")

    print("PART 1 — STRINGS: TEXT AS DATA")
    print('A string is text in quotes, such as "Raccoon City".')
    print("input() also gives your program a string, even when you type digits.\n")

    phrase = "Bryan has a package"
    reveal(
        'Predict len("Bryan has a package"): ',
        len(phrase),
        "len() counts every character, including spaces.",
    )

    print("A string is a sequence: Python numbers its characters starting at 0.")
    reveal(
        'Predict "Bryan"[0] and "Bryan"[-1]: ',
        f"{phrase[:5][0]!r} and {phrase[:5][-1]!r}",
        "Index 0 is the first character; index -1 is the last.",
    )
    reveal(
        'Predict "Raccoon City"[0:7]: ',
        "Raccoon"[0:7],
        "A slice includes its start and stops before its end. [0:7] takes positions 0 through 6.",
    )

    print("Strings are immutable: an operation makes a new string instead of editing the old one.")
    label = "urgent delivery"
    louder_label = label.upper()
    reveal(
        'Predict label.upper() for label = "urgent delivery": ',
        louder_label,
        "upper() returns a new uppercase string. label still contains its original text.",
    )
    print(f"After calling upper(): label = {label!r}; louder_label = {louder_label!r}\n")

    print("Useful string methods return strings you can use again:")
    raw_word = "  sNoWy  "
    clean_word = raw_word.strip().lower()
    reveal(
        'Predict "  sNoWy  ".strip().lower(): ',
        clean_word,
        "strip() removes outside whitespace; lower() changes letter case. Chaining runs left to right.",
    )
    print("Use + to join strings, or an f-string to place values inside a sentence.")
    word = "snowy"
    reveal(
        'Predict f"The road is {word}.": ',
        f"The road is {word}.",
        "The f before the quote lets Python evaluate the expression inside braces.",
    )

    print("input() returns text. Convert it with int() before doing arithmetic:")
    typed_number = "3"
    reveal(
        'Predict int("3") + 2: ',
        int(typed_number) + 2,
        'The text "3" becomes the integer 3, so Python adds numbers instead of joining text.',
    )
    print("You can check the type of a value with type(value).\n")


def teach_objects(bryan):
    print("PART 2 — OBJECT-ORIENTED PROGRAMMING")
    print("A class is a recipe. An object is one thing made from that recipe.")
    print("Character is the class; bryan is one Character object.")
    print("Attributes store an object's data. Methods are functions that belong to its class.\n")

    reveal(
        "Predict bryan.job: ",
        bryan.job,
        "The dot looks up the job attribute on this particular object.",
    )
    reveal(
        "Predict bryan.introduce(): ",
        bryan.introduce(),
        "The parentheses call a method. Inside it, self means the object receiving the call.",
    )

    print("__init__ runs when an object is created. It sets up that object's attributes.")
    print("self.name belongs to this character; another Character can have a different name.")
    other_character = Character("Sam", "night dispatcher", "the station", "a radio")
    reveal(
        "Predict other_character.name: ",
        other_character.name,
        "Each object keeps its own attribute values, even when both came from Character.",
    )

    print("Objects can change their state by updating attributes through methods.")
    old_destination = bryan.destination
    bryan.change_destination("the police station")
    reveal(
        "After bryan.change_destination('the police station'), what is bryan.destination? ",
        bryan.destination,
        "The method assigns a new string to this object's destination attribute.",
    )
    bryan.change_destination(old_destination)
    reveal(
        "What does bryan.deliver() return? ",
        bryan.deliver(),
        "The method uses attributes, changes status, and returns a string. Methods can do both.",
    )
    print(f"Bryan's status is now: {bryan.status}\n")


def build_story(bryan):
    print("PART 3 — PUT THE IDEAS INTO A MAD LIB")
    print("Each answer starts as a string. strip() trims it; we keep the player's wording.\n")
    mad_lib = {
        "adjective": get_word("Give me an adjective: ").strip(),
        "sound": get_word("Give me a noise: ").strip(),
        "excuse": get_word("Give me a terrible excuse: ").strip(),
        "number": get_word("Give me a number: ").strip(),
    }

    # Each list item is a string. f-strings insert attribute and dictionary values.
    opening_scene = [
        f"{bryan.name} has a girlfriend named Michelle.",
        "They have a big conversation to finish.",
        "Bryan is not ready to be a dad. The night has scheduled other topics.",
        bryan.introduce(),
        f"The package needs to go to {bryan.destination}.",
        "It is snowing. This is not the main problem.",
        "The main problem is that Raccoon City is having a terrible night.",
        f"Bryan nearly hits a sick woman. She makes a {mad_lib['adjective']} sound: {mad_lib['sound']}!",
        "A police officer is dead. Bryan takes the officer's gun.",
        f"Bryan now has protection. It has {mad_lib['number']} bullets and no customer support.",
        "There are infected people everywhere.",
        f"Bryan explains the situation to himself: '{mad_lib['excuse']}'",
        f"Bryan is {bryan.status}.",
        "Bryan still has the package.",
        "The delivery is going poorly.",
    ]

    print("\nTHE STORY\n")
    for sentence in opening_scene:
        print(sentence)


def review():
    print("\nPART 4 — QUICK REVIEW")
    print("Try answering these without scrolling back:")
    print("1. What does input() return, and how can you count a string's characters?")
    print("2. What do index 0, index -1, and the slice [start:stop] mean?")
    print("3. Why does calling upper() leave the original string alone?")
    print("4. When would you use int() after input()?")
    print("5. How is a class different from an object made from it?")
    print("6. What do self, an attribute, and a method mean?")
    print("7. Which method changed Bryan's destination and status?")
    print("\nMini challenge: add a favorite_food attribute to Character, then use it in introduce().")
    print("Next challenge: write a method that changes Bryan's status to 'on break'.")


def main():
    teach_strings()

    # Constructor arguments become the initial state of this Character object.
    bryan = Character(
        name="Bryan",
        job="medical courier",
        destination="Raccoon City",
        package="a medical delivery",
    )
    teach_objects(bryan)
    build_story(bryan)
    review()


if __name__ == "__main__":
    main()
