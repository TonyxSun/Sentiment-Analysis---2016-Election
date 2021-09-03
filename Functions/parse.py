def clean_data(tw):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    cleaned_tw = ""
    for char in tw:
        if char not in punctuations:
            cleaned_tw += char
    return cleaned_tw

# print(clean_data("living the dream.#tommulcair instagram.com/p/8up9qepkxw/"))