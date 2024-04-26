import random
import choices
#---hang diagram---
stages = ['''
  +-----+
  |     |
  O     |
/ | \   |
 / \    |
        |
============   
''','''
 +-----+
  |     |
  O     |
/ | \   |
 /      |
        |
============''',
''' +-----+
  |     |
  O     |
/ | \   |
        |
        |
===========''',
''' +-----+
  |     |
  O     |
/ |     |
        |
        |
==========''','''
 +-----+
  |     |
  O     |
/       |
        |
        |
===========
''','''
 +-----+
  |     |
  O     |
/       |
        |
        |
===========''','''
 +-----+
  |     |
  O     |
        |
        |
        |
============   ''',
'''
 +-----+
  |     |
        |
        |
        |
        |
===========''']

end_game = False

rd_word = random.choice(choices.words)
lives = 6
display = []
for _ in rd_word:
    display += "_"

    #--------IF TRUE---------
while not end_game:
    in_words = input("guess a letter : ").lower()
    for position in range(len(rd_word)):
        i = rd_word[position]
        if i == in_words:
            display[position] = i
    if in_words not in rd_word:
        lives -= 1
        if lives == 0:
            end_game = True
            print("You lost ")
            print(f"u r word is {rd_word}")
    print(display)
    if "_" not in display :
        end_game = True
        print("You Won")
    print(stages[lives])
