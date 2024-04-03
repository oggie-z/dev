import random as rdm

name1 = input("What is your NAME ?")
print("Best of Luck!", name1)

words1 = ['Donkey', 'Aeroplane', 'America', 'Program',
          'Python', 'language', 'Cricket', 'Football', 
          'Hockey', 'Spaceship', 'bus', 'flight']

# rdm.choice() function will choose one random word from the given list of words
word1 = rdm.choice(words1)

print("Please guess the characters:")

guesses1 = ""

# we can use any number of turns here 
turns1 = 10 

while turns1 > 0:

    # counting the number of times a user is failed to guess the right character
    failed1 = 0

    # all the characters from the input will be taken one at a time. 
    for char in words1:

        # here, we will compare the input character with the character in guesses1
        if char in guesses1:
            print(char)

        else:
            print:("_")

            #for every failure of the user 1 will be incremented in failed1
            failed1 += 1

        if failed1 == 0:
            # user will win the game if failure is 0 and 'User Win' will be giver as outpud
            print("User Win")


            # this will print the correct word
            print("The correct word is:", word1)
            break

            # if the user has input the wrong alphabet then
            #it will ask user to enter another alphabet
            guess1 
