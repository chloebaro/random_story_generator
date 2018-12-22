import random

def replace_newlines(text):
    new_text = text
    for index in range(len(text)):
        if text[index] == "\n":
            new_text = new_text[:index] + " " + new_text[index + 1:]
    return new_text

def separate_words(text):
    new_text = replace_newlines(text)
    word_list = new_text.split(" ")
    return word_list

def choose_random_word(word_list):
    rand_index = random.randrange(0, len(word_list))
    return word_list[rand_index]

def next_words(text, context):
    word_list = separate_words(text)
    possible_next_words = []
    index1 = 0
    index2 = 0
    loop = True
    while(loop == True):
        new_list = word_list[index1:]
        if(context in new_list):
            index2 = new_list.index(context)
            index1 = index1 + index2
            if(index1 < len(word_list) - 1):
                possible_next_words.append(new_list[index2 + 1])
            else:
                possible_next_words.append(word_list[0])
            index1 += 1
        else:
            loop = False
    return possible_next_words

def generate_story(file_name, num_words):
    file = open(file_name)
    text = file.read()
    word_list = separate_words(text)
    context = choose_random_word(word_list)
    story = context
    for i in range(num_words):
        possible_next_words = next_words(text, context)
        context = choose_random_word(possible_next_words)
        story = story + " " + context
    file.close()
    return story
    
        

file_name = "training_text.txt"
story = generate_story(file_name, 15)
print(story)
