

def read_template():
    pass


def parse_template():
    pass


def merge():
    pass


def main():
    # print welcome message to the user, explaining the Madlib process and command line interactions
    print("""\nWelcome to MADLIB. Input random words as prompted. Upon completion, a unique story shall be created.
""")

    # read a template Madlib file, and parse that file into usable parts
    with open("assets/dark_and_stormy_night_template.txt", "r") as file:
        bananas = file.read()
        print(bananas)

    # prompt the user to submit a series of words to fit each of the required components of the Madlib template
    adj_one = input("Name an adjective that describes a noun")
    adj_two = input("And another adjective")
    noun = input("And a noun such as a place, person, or thing")

    # with the collected user inputs, populate the template such that each provided input is placed into the correct
    with open("assets/dark_and_stormy_night_template.txt", "r") as file:

    # position within the template
        print(f"{adj_one}{adj_two}{noun}")

    # After the resulting Madlib has been completed, provide the completed response back to the user in the command line

    # Write the completed test to a new file on your file system(in the repo)

if __name__ == "__main__":
    main()