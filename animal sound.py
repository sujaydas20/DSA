# import random
# import pygame

# pygame.mixer.init()

# animal_files = {
#     "Dog": "sounds/dog.mp3",
#     "Cat": "sounds/cat.mp3",
#     "Lion": "sounds/lion.mp3",
#     "Cow": "sounds/cow.mp3",
#     "Horse": "sounds/horse.mp3"
# }

# animal = random.choice(list(animal_files.keys()))

# print(f"Animal: {animal}")

# pygame.mixer.music.load(animal_files[animal])
# pygame.mixer.music.play()

# while pygame.mixer.music.get_busy():
#     pass



import random
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Animal sounds
animal_sounds = {
    "Dog": "Woof Woof",
    "Cat": "Meow Meow",
    "Cow": "Moo Moo",
    "Lion": "Roar",
    "Tiger": "Grrr",
    "Duck": "Quack Quack",
    "Sheep": "Baa Baa",
    "Horse": "Neigh",
    "Elephant": "Trumpet",
    "Monkey": "Oo Oo Ah Ah",
    "Goat": "Maa Maa",
    "Frog": "Ribbit",
    "Pig": "Oink Oink",
    "Owl": "Hoot Hoot"
}

# Choose a random animal
animal = random.choice(list(animal_sounds.keys()))
sound = animal_sounds[animal]

# Print the result
print(f"Animal : {animal}")
print(f"Sound  : {sound}")

# Speak the sound
engine.say(sound)
engine.runAndWait()