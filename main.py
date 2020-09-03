import random
import string


scrambled_passage = ""
# get a string of all punctuations
punctuations = string.punctuation
# convert to list then tuple - will use later for str.endswith
punctuations = tuple(list(punctuations))


# get user input
print("please type a sentence below:")
user_passage = input()
# while user input is only whitespace, do this
while user_passage.isspace():
    print("You can't input white space.  please type a sentence:")
    user_passage = input()


# returns boolean value.  If all words in the passage are greater than 3 in length, return True
def words_check(passage):
    greater_than_three = False
    for word in passage.split():
        if len(word) > 3:
            greater_than_three = True

    return greater_than_three


# function that attempts to scramble each word
def scramble_word(word):
    # if all words in the passage are greater than 3
    if words_check(user_passage):
        if len(word) > 3:
             # if the word ends with a punctuation, set temp_word to word, but without the first character and the last
             # two characters
            if word.endswith(punctuations):
                temp_word = word[1:-2]
                temp_word = random.sample(temp_word, len(temp_word))
                temp_word.insert(0, word[0])
                temp_word.append(word[-2])
                temp_word.append(word[-1])
                return ''.join(temp_word)
            # else set temp_word to word, but without the first character and the last character
            else:
                temp_word = word[1:-1]
                temp_word = random.sample(temp_word, len(temp_word))
                temp_word.insert(0, word[0])
                temp_word.append(word[-1])
                return ''.join(temp_word)
        # else return word as is
        else:
            return word
    # if greater than 1 then scramble the word - 20% chance
    elif len(word) > 1:
        temp_word = word
        if random.random() < 0.2:
            temp_word = random.sample(word, len(word))
        return ''.join(temp_word)
    # else add a duplicate letter to the word - 20% chance
    else:
        temp_word = word
        if random.random() < 0.2:
            temp_word = word + word
        return temp_word


# this function will create the passage with the scrambled words
def create_new_passage(passage):
    new_passage = ""
    for word in passage.split():
        new_passage = new_passage + scramble_word(word) + " "

    return new_passage


# set scrambled_passage to the returned value of the function create_new_passage(user_passage)
scrambled_passage = create_new_passage(user_passage)
# if last character of the passage is an empty space, then remove the empty space
if scrambled_passage[len(scrambled_passage) - 1] == " ":
    scrambled_passage = scrambled_passage[:len(scrambled_passage) - 1]

# While the the scrambled passage equals user_passage, that means there is not at least one misspelling in the passage
# call the create_new_passage(user_passage) function again and set it to scrambled_passage
while scrambled_passage == user_passage:
    scrambled_passage = create_new_passage(user_passage)
    # if last character of the passage is an empty space, then remove the empty space
    if scrambled_passage[len(scrambled_passage) - 1] == " ":
        scrambled_passage = scrambled_passage[:len(scrambled_passage) - 1]

print(scrambled_passage)
