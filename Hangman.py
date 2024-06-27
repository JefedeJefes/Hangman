import random

word_list = ["ardvark","baboon","camel"]

chosen_word=random.choice(word_list)

print(f"the chosen word is {chosen_word}")

length_of_list = len(chosen_word)

display=[]

for _ in range(length_of_list):
    display+="_"
print(display)

guess=input("enter the letter to check")

for position in range(length_of_list):
    letter=chosen_word[position]

    if letter==guess:
        display[position]=letter

print(display)


