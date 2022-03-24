import random

story_setting = [
    "You are in a dark forest",
    "You are in the void",
    "You are in a dark cave",
    "You are in a desert",
    "You are lost"
]

story_charecters = [
    "You are a knight",
    "You are a wizard",
    "You are a thief",
    "You are a warrior",
    "You are a monk",
    "You are a priest",
    "You are a mage",
    "You are a rogue",
    "You are a barbarian",
]

story_enemy = [
    "goblin",
    "orc",
    "troll",
    "you",
    "dragon",
    "demon",
    "skeleton",
    "zombie",
]

plot_twist = [
    "You are in a comma",
    "You dont exist",
    "You are not real"
]


def PickRandomSelection(setting, story_char, story_enemy, plot_twist):
    ran_setting = random.choice(setting)
    ran_story_char = random.choice(story_char)
    ran_enemy = random.choice(story_enemy)
    ran_plot = random.choice(plot_twist)

    return f'{ran_setting} {ran_story_char} your enemy is {ran_enemy} {ran_plot}'


print(PickRandomSelection(story_setting, story_charecters, story_enemy, plot_twist))
