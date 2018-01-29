from text_paste import *

def tools_get_list_available_languages():
    
    dictionary_with_languages = get_list_available_languages()
    keys_with_languages = dictionary_with_languages.keys()
    dictionary_with_languages = get_list_available_languages()
    keys_with_languages = dictionary_with_languages.keys()
    BoolLanguages = []
    list_with_some_languages = ['ruby', 'java5', 'cpp', 'scala', 'python', 'text', 'mysql', 'csharp', 'css', 'javascript', 'php']
    for every_language in list_with_some_languages:
        if every_language in keys_with_languages:
            BoolLanguages.append(True)
        else:
            BoolLanguages.append(False)
    return all(BoolLanguages)


def tools_get_random_paste():

    dictionary_with_random_paste = get_random_paste()
    dictionary_with_random_paste_keys = dictionary_with_random_paste.keys()
    dictionary_with_random_paste = get_random_paste()
    dictionary_with_random_paste_keys = dictionary_with_random_paste.keys()
    BoolRandomPaste = []
    list_with_values = ['lang', 'title', 'name', 'url']
    for every_value in list_with_values:
        if every_value in dictionary_with_random_paste:
            BoolRandomPaste.append(True)
        else:
            BoolRandomPaste.append(False)
    return all(BoolRandomPaste)

