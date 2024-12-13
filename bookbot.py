import sys

def main():
    if len(sys.argv) == 1:
        print("Please enter a relative path as first argument of this application.")
        return
    path = sys.argv[1]
    try:
        text = read_content(path)
    except:
        print("File not found. First argument should be a relative path to a text file.")
        return
    number_of_words = count_words(text)
    character_dict = count_characters(text)
    character_list = character_dict_to_list(character_dict)
    make_report(path, number_of_words, character_list)

def read_content(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    character_dict = {}
    for character in text.lower():
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def character_dict_to_list(characters_dict):
    character_list = []
    for character, appearances in characters_dict.items():
        character_list.append({"character": character, "appearances": appearances})

    character_list.sort(reverse=True, key=sort_on_appearances)
    return character_list

def sort_on_appearances(dict):
    return dict["appearances"]

def make_report(path, number_of_words, character_list):
    print(f"--- Begin report of {path} ---")
    print("")
    print(f"{number_of_words} words found in the file.")
    print("")
    for item in character_list:
        if item["character"].isalpha():
            print(f"The {item["character"]} was found {item["appearances"]} times.")
    print("")
    print("--- End report ---")

main()