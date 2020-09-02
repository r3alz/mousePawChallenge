import random
import string


scrambled_passage = ""
punctuations = string.punctuation
punctuations = tuple(list(punctuations))

print("please type a sentence below:")
user_passage = input()
while user_passage.isspace():
    print("You can't input white space.  please type a sentence:")
    user_passage = input()


def words_check(passage):
    greater_than_three = False
    for word in passage.split():
        if len(word) > 3:
            greater_than_three = True

    return greater_than_three


def scramble_word(word):
    if words_check(user_passage):
        if len(word) > 3:
            if word.endswith(punctuations):
                temp_word = word[1:-2]
                temp_word = random.sample(temp_word, len(temp_word))
                temp_word.insert(0, word[0])
                temp_word.append(word[-2])
                temp_word.append(word[-1])
                return ''.join(temp_word)
            else:
                temp_word = word[1:-1]
                temp_word = random.sample(temp_word, len(temp_word))
                temp_word.insert(0, word[0])
                temp_word.append(word[-1])
                return ''.join(temp_word)
        else:
            return word
    elif len(word) > 1:
        temp_word = word
        if random.random() < 0.2:
            temp_word = random.sample(word, len(word))
        return ''.join(temp_word)
    else:
        temp_word = word
        if random.random() < 0.2:
            temp_word = word + word
        return temp_word


def create_new_passage(passage):
    new_passage = ""
    for word in passage.split():
        new_passage = new_passage + scramble_word(word) + " "

    return new_passage


scrambled_passage = create_new_passage(user_passage)
if scrambled_passage[len(scrambled_passage) - 1] == " ":
    scrambled_passage = scrambled_passage[:len(scrambled_passage) - 1]

while scrambled_passage == user_passage:
    scrambled_passage = create_new_passage(user_passage)
    if scrambled_passage[len(scrambled_passage) - 1] == " ":
        scrambled_passage = scrambled_passage[:len(scrambled_passage) - 1]

print(scrambled_passage)
