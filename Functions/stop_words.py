# -*- coding: utf-8 -*-
def remove_stop_words(tw):
    with open("./Assets/stop_words.txt", 'r') as stop_words_txt:
        stop_words = stop_words_txt.readlines()
        stop_words_list = [word.strip() for word in stop_words]
    tw_words = tw.split()
    tw_stripped = ""
    for word in tw_words:
        if not word.lower() in stop_words_list:
            tw_stripped += word
        else:
            print(word)
    return tw_stripped
        
remove_stop_words("“living the dream.#tommulcair instagram.com/p/8up9qepkxw/")