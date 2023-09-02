from PyDictionary import PyDictionary
import os
import time

time.sleep(1)
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')  # Clear the console (works for Unix-like systems)


# ANSI escape codes for text color
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"


def dictionary_app():
    dictionary = PyDictionary()

    while True:
        print("\n" + BOLD + "Welcome to the PyDict App!" + RESET)
        print("1. " + GREEN + "Find Word Definitions" + RESET)
        print("2. " + GREEN + "Find Synonyms" + RESET)
        print("3. " + GREEN + "Find Antonyms" + RESET)
        print("4. " + GREEN + "Translate Word" + RESET)
        print("5. " + RED + "Exit" + RESET)
        print("6. " + YELLOW + "About" + RESET)

        choice = input("Enter your choice: ")

        if choice == '1':
            word = input("Enter a word: ")
            definitions = dictionary.meaning(word)
            if definitions:
                for key, value in definitions.items():
                    if os.name == 'nt':
                        os.system('cls')
                    else:
                        os.system('clear')  # Clear the console (works for Unix-like systems)
                    print(f"{BOLD}{key}:{RESET} {', '.join(value)}")

            else:
                print(RED + "Word not found in the dictionary." + RESET)

        elif choice == '2':
            word = input("Enter a word: ")
            synonyms = dictionary.synonym(word)
            if synonyms:
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')  # Clear the console (works for Unix-like systems)
                print(GREEN + f"Synonyms: {', '.join(synonyms)}" + RESET)
            else:
                print(RED + "No synonyms found." + RESET)

        elif choice == '3':
            word = input("Enter a word: ")
            antonyms = dictionary.antonym(word)
            if antonyms:
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')  # Clear the console (works for Unix-like systems)
                print(GREEN + f"Antonyms: {', '.join(antonyms)}" + RESET)
            else:
                print(RED + "No antonyms found." + RESET)

        elif choice == '4':
            word = input("Enter a word: ")
            language = input("Enter target language (e.g., 'fr' for French): ")
            translation = dictionary.translate(word, language)
            if translation:
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')  # Clear the console (works for Unix-like systems)
                print(BLUE + f"Translation: {translation}" + RESET)
            else:
                print(RED + "Translation not available." + RESET)

        elif choice == '5':
            print(RED + "Goodbye!" + RESET)
            break

        elif choice == '6':
            print(YELLOW + "This is a simple Python dictionary app.")
            print(
                YELLOW + "This project is licensed to " + BLUE + BOLD + "Independent-coder" + YELLOW + " using an MIT license on GitHub" + RESET)
            time.sleep(5)  # Add a 5-second delay
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')  # Clear the console (works for Unix-like systems)

        else:
            print(RED + "Invalid choice. Please try again." + RESET)


if __name__ == "__main__":
    dictionary_app()
