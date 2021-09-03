# -*- coding: utf-8 -*-

def clean_data(tw):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    cleaned_tw = ""
    for char in tw:
        if char == "#":
            cleaned_tw += " "
        elif char not in punctuations:
            cleaned_tw += char
    return cleaned_tw

def remove_stop_words(tw):
    with open("./Assets/stop_words.txt", 'r') as stop_words_txt:
        stop_words = stop_words_txt.readlines()
        stop_words_list = [word.strip() for word in stop_words]
    tw_words = clean_data(tw).split()
    tw_stripped = ""
    for word in tw_words:
        if not word.lower() in stop_words_list:
            tw_stripped += word + " "
        # else:
        #     print(word)
    return tw_stripped

def tokenize_unigram(tw):
    cleaned_tw = remove_stop_words(tw)
    print(cleaned_tw)
    return cleaned_tw.split()

print(tokenize_unigram("living the dream.#tommulcair instagram.com/p/8up9qepkxw/"))

