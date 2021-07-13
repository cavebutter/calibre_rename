#  Make a whole bunch of empty directories that I can use to play around with

import os
import random

authors = ['Adams', 'Baker', 'Cooper', 'Davis', 'Eddings', 'Fielding', 'Grant', 'Harris',
           'Ickles', 'Jackson', 'Kenworth', 'Levine', 'Mason', 'Newbury', 'Olivier', 'Penrose',
           'Quinn', 'Robinson', 'Stephens', 'Truman', 'Underhill', 'Verene', 'Wilson', 'Xavier',
           'Young', 'Zwelling']
nouns = ['Bear', 'Apple', 'Cookie', 'Dixie Cup', 'Elephant', 'Fire Hydrant', 'Giraffe', 'Horn',
         'Iguana', 'Jug', 'Kangaroo', 'Lemur', 'Monkey', 'Nut', 'Orange', 'Person', 'Quill',
         'Rose', 'Stoat', 'Teapot', 'Umbrella', 'Xylophone', 'Yam', 'Zebra']
pronouns = ['I', 'He', 'She', 'They']
verbs = ["Met", "Ate", "Spied", "Inspected", "Bit", "Called", "Dated", "Ended Formal Diplomatic "
                                                                       "Relations With",
         "Forgot About", "Greeted", "Harried", "Jumped", "Kicked", "Lampooned", "Mocked",
         "Never Considered Before", "Opted Against", "Pressed", "Queried", "Rode", "Talked To",
         "Underestimated", "Vacationed With", "Winked At", "Xylophoned", "Yelled At", "Zanzibarred"]
articles = ["A", "The", "That", "One"]

if __name__ == "__main__":
    my_path = 'ENTER THE PATH FOR YOUR TEST DIRECTORY HERE'
    os.mkdir(my_path)
    os.chdir(my_path)
    j = random.randint(3, 6)
    used_names = []
    for directory in range(j):
        author = random.choice(authors)
        if author not in used_names:
            used_names.append(author)
            author_dir = os.path.join(my_path, author)
            os.mkdir(author_dir)
            os.chdir(author_dir)
            i = 0
            for i in range(3):
                title = random.choice(articles) + " " + random.choice(nouns) + " " + random.choice(
                    pronouns) + " " + random.choice(verbs) + " (" + str(random.randint(1,1000)) + ")"
                os.mkdir(title)
                i += 1
        else:
            continue
