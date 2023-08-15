import random

def random_string():
    random_list = [
        "Sure. Outfits on the way",
        "Let me show you what I got.",
        "Searching outfits for you",
        "Looking for the best outfits that fit the description."
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]
print(random_string())