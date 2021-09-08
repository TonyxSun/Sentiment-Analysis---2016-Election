# -*- coding: utf-8 -*-

with open("./Assets/classified_tweets.txt", 'r') as classified_tweets_txt:
        tweets_list = classified_tweets_txt.readlines()

with open("./Assets/stop_words.txt", 'r') as stop_words_txt:
    stop_words = stop_words_txt.readlines()
    # print(stop_words)
    stop_words_list = [word.strip() for word in stop_words]

with open("./Assets/corpus.txt", 'r') as corpus_txt:
    corpus_list = corpus_txt.readlines()
    corpus_list = [word.strip() for word in corpus_list]
    corpusDict = {}
    for item in corpus_list:
        corpusDict[item[:-2].strip()] = item[-2:].strip()

# generates corpus_dict.txt, a list of all words in corpus
# with open("./Assets/corpus_dict.txt", 'w') as corpus_dict:
#     for x in corpusDict:
#         corpus_dict.write(x + '\n')

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
    # print(cleaned_tw)
    return cleaned_tw.split()

def bag_of_words(tw):
    cleaned_tw = tokenize_unigram(tw)
    bag_dict = {}
    for token in cleaned_tw:
        if token in bag_dict:
            bag_dict[token] += 1
        else:
            bag_dict[token] = 1

    return bag_dict

# print(bag_of_words("living the dream.#tommulcair  instagram.com/p/8up9qepkxw/"))

def tweet_score(tw):
    for tweet in tweets_list:
        wordsDict = bag_of_words(tweet[2:])
        # for word in wordsDict:


