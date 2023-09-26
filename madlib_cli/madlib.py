import re

def read_template(file):
    try:
        with open(file, 'r') as file:
            content = file.read()
            return content
    except:
        raise FileNotFoundError


def parse_template(string):
    stripped = re.sub(r'\{.*?\}', '{}', string)
    # return "It was a {} and {} {}.", ("Adjective", "Adjective", "Noun")
    parts = re.findall( r'\{.*?\}', string)
    #list comprehension with help from Jacob Bassett
    parts = (i[1:-1] for i in parts)
    return stripped, tuple(parts)


# this passed but I don't think it's pretty
def merge(template, words):
    print(template, words)
    formatted_string = "It was a {} and {} {}.".format(words[0],words[1], words[2])
    return formatted_string


def main():
    # print welcome message to the user, explaining the Madlib process and command line interactions
    print("""\nWelcome to MADLIB. Give me random words as prompted. Upon completion, a unique story shall be created."
""")
    # read a template Madlib file, and parse that file into usable parts
    with open("../assets/dark_and_stormy_night_template.txt", "r+") as file:
        template = file.read()
        # prompt the user to submit a series of words to fit each of the required components of the Madlib template
        adjective_one = input("Enter an adjective ")
        adjective_two = input("Enter another adjective ")
        noun = input("Enter a noun ")
        words = [adjective_one, adjective_two, noun]
        formatted_words = tuple(words)
        # with the collected user inputs, populate the template such that each provided input is placed into the correct
        # position within the template
        story = merge(template, formatted_words)
        revised_story = file.write(story)
        print(revised_story)


    # After the resulting Madlib has been completed, provide the completed response back to the user in the command line

    # Write the completed test to a new file on your file system(in the repo)

if __name__ == "__main__":
    main()