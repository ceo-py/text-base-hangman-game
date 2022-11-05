import random

hang_man = {1: " +----+\n"
               "      |\n"
               "      |\n"
               "      |\n"
               "     ===",
            2: " +----+\n"
               " O    |\n"
               "      |\n"
               "      |\n"
               "     ===",
            3: " +----+\n"
               " O    |\n"
               " |    |\n"
               "      |\n"
               "     ===",
            4: " +----+\n"
               " O    |\n"
               " |    |\n"
               "/     |\n"
               "     ===",
            5: " +----+\n"
               " O    |\n"
               " |    |\n"
               "/|    |\n"
               "     ===",
            6: " +----+\n"
               " O    |\n"
               " |    |\n"
               "/|\   |\n"
               "     ===",
            7: " +----+\n"
               " O    |\n"
               " |    |\n"
               "/|\   |\n"
               "/    ===",
            8: " +----+\n"
               " O    |\n"
               " |    |\n"
               "/|\   |\n"
               "/ \  ==="}

word_generator = ["abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure", "bagpipes",
                  "bandwagon", "banjo", "bayou", "beekeeper", "bikini", "blitz", "blizzard", "boggle", "bookworm",
                  "boxcar", "boxful", "buckaroo", "buffalo", "buffoon", "buxom", "buzzard", "buzzing", "buzzwords",
                  "caliph", "cobweb", "cockiness", "croquet", "crypt", "curacao", "cycle", "daiquiri", "dirndl",
                  "disavow", "dizzying", "duplex", "dwarves", "embezzle", "equip", "espionage", "euouae", "exodus",
                  "faking", "fishhook", "fixable", "fjord", "flapjack", "flopping", "fluffiness", "flyby", "foxglove",
                  "frazzled", "frizzled", "fuchsia", "funny", "gabby", "galaxy", "galvanize", "gazebo", "giaour",
                  "gizmo", "glowworm", "glyph", "gnarly", "gnostic", "grogginess", "haiku", "haphazard", "hyphen",
                  "iatrogenic", "icebox", "injury", "ivory", "ivy", "jackpot", "jaundice", "jawbreaker", "jaywalk",
                  "jazziest", "jazzy", "jelly", "jigsaw", "jinx", "jiujitsu", "jockey", "jogging", "joking", "jovial",
                  "joyful", "juicy", "jukebox", "jumbo", "kayak", "kazoo", "keyhole", "khaki", "kilobyte", "kiosk",
                  "kitsch", "kiwifruit", "klutz", "knapsack", "larynx", "lengths", "lucky", "luxury", "lymph",
                  "marquis", "matrix", "megahertz", "microwave", "mnemonic", "mystify", "naphtha", "nightclub",
                  "nowadays", "numbskull", "nymph", "onyx", "ovary", "oxidize", "oxygen", "pajama", "peekaboo",
                  "phlegm", "pixel", "pizazz", "pneumonia", "polka", "pshaw", "psyche", "puppy", "puzzling",
                  "quartz", "queue", "quips", "quixotic", "quiz", "quizzes", "quorum", "razzmatazz", "rhubarb",
                  "rhythm", "rickshaw", "schnapps", "scratch", "shiv", "snazzy", "sphinx", "spritz", "squawk",
                  "staff", "strength", "strengths", "stretch", "stronghold", "stymied", "subway", "swivel", "syndrome",
                  "thriftless", "thumbscrew", "topaz", "transcript", "transgress", "transplant", "triphthong",
                  "twelfth", "twelfths", "unknown", "unworthy", "unzip", "uptown", "vaporize", "vixen", "vodka",
                  "voodoo", "vortex", "voyeurism", "walkway", "waltz", "wave", "wavy", "waxy", "wellspring",
                  "wheezy", "whiskey", "whizzing", "whomever", "wimpy", "witchcraft", "wizard", "woozy", "wristwatch",
                  "wyvern", "xylophone", "yachtsman", "yippee", "yoked", "youthful", "yummy", "zephyr", "zigzag",
                  "zigzagging", "zilch", "zipper", "zodiac", "zombie"]
ltr_list = {}
wrong_answer = 0
word_to_guess = random.choice(word_generator)
show_word = f"{len(word_to_guess) * '_'}"
used_letter = []


def print_result():
    for pos, ltr in enumerate(show_word):
        if pos in ltr_list:
            print(f"{ltr_list[pos]}", end="")
        else:
            print("_", end="")
    print()


print_result()
while wrong_answer != 8:
    letter_to_guess = input("Enter letter: ").lower()
    if len(letter_to_guess) != 1:
        print("Type only one letter!!!")
        continue
    if letter_to_guess in ltr_list.values():
        print("You already try that letter!!")
        continue
    used_letter.append(letter_to_guess)
    if letter_to_guess in word_to_guess and letter_to_guess not in list(ltr_list.values()):
        for pos, char in enumerate(word_to_guess):
            if char == letter_to_guess:
                ltr_list[pos] = letter_to_guess
    else:
        wrong_answer += 1
        print(hang_man[wrong_answer])
        print(f"{wrong_answer}/8 wrong answers!!!\n")

        if wrong_answer == 8:
            print("Game Over!!! You have been hang!!!")
            print(f"Correct word was {word_to_guess}!")
            print(f"You guess {len(ltr_list)} out of {len(word_to_guess)} letters!")
            continue
    if len(ltr_list) == len(word_to_guess):
        print("Congrats you want the game!!!")
        print(f"You guess the word - {word_to_guess}")
        break
    print_result()
    print(f"\nUsed letters so far\n{', '.join(used_letter)}\n")
