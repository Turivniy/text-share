import pytest
from text_paste_1 import *


def test_create_paste():
    """ 1.create link with id
        2.paste link and receieve only my id
        3.take id from the dict get_paste
        4.take key url from the dict """
    link = create_paste(text='this is my text', title='some title',  name='myname', private=0, lang='Text', expire='1')
    id_from_the_link = get_paste_id(link)
    dictionary_with_data = get_paste(id_from_the_link)
    url_from_the_dictionary_with_data = dictionary_with_data['url']

    assert (url_from_the_dictionary_with_data == link)

#Bug #1 Expire is -1 instead of positive Value
def test_create_paste_with_expire_negative():

    link = create_paste(text='text', title='',  name='Olga', private=0, lang='Text', expire='-1' )
    id_from_the_link = get_paste_id(link)
    dictionary_with_data = get_paste(id_from_the_link)
    url_from_the_dictionary_with_data = dictionary_with_data['url']

    assert (url_from_the_dictionary_with_data == link)

def test_create_paste_with_expire_zer0():

    link = create_paste(text='text', title='',  name='Olga', private=0, lang='Text', expire='0' )
    id_from_the_link = get_paste_id(link)
    dictionary_with_data = get_paste(id_from_the_link)
    url_from_the_dictionary_with_data = dictionary_with_data['url']

    assert (url_from_the_dictionary_with_data == link)

#bug #2 Expire is string instead of Int Value (time)
def test_create_paste_with_expire_string():

    link = create_paste(text='text', title='',  name='Olga', private=0, lang='Text', expire='0' )
    id_from_the_link = get_paste_id(link)
    dictionary_with_data = get_paste(id_from_the_link)
    url_from_the_dictionary_with_data = dictionary_with_data['url']

    assert (url_from_the_dictionary_with_data == link)

#Bug #3 Value Private 3 instead of 1 or 0 
def test_create_paste_with_private_number_3():

    link = create_paste(text='text', title='',  name='Olga', private=3, lang='Text', expire='2' )
    id_from_the_link = get_paste_id(link)
    dictionary_with_data = get_paste(id_from_the_link)
    url_from_the_dictionary_with_data = dictionary_with_data['url']

    assert (url_from_the_dictionary_with_data == link)

#Bug #4 Value Private 3 instead of 1 or 0 
def test_create_paste_with_private_number_string():

    link = create_paste(text='text', title='',  name='Olga', private='1', lang='Text', expire='1' )
    id_from_the_link = get_paste_id(link)
    dictionary_with_data = get_paste(id_from_the_link)
    url_from_the_dictionary_with_data = dictionary_with_data['url']

    assert (url_from_the_dictionary_with_data == link)

#Bug #5 Value Private 3 instead of 1 or 0 
def test_create_paste_with_private_negative():

    link = create_paste(text='text', title='',  name='Olga', private=-1, lang='Text', expire='1' )
    id_from_the_link = get_paste_id(link)
    dictionary_with_data = get_paste(id_from_the_link)
    url_from_the_dictionary_with_data = dictionary_with_data['url']

    assert (url_from_the_dictionary_with_data == link)

# Bug #6 Empty field language
def test_create_paste_with_expire_string():

    link = create_paste(text='text', title='',  name='Miss x', private=0, lang=' ', expire='1' )
    id_from_the_link = get_paste_id(link)
    dictionary_with_data = get_paste(id_from_the_link)
    url_from_the_dictionary_with_data = dictionary_with_data['url']

    assert (url_from_the_dictionary_with_data == link)

def test_get_paste_id():
    """ 1.create link
        2.paste link and receieve only my id
        3.take text from the dict get_paste
        4.take key id from the dict """
    link = create_paste(text='this is my text', title='some title',  name='myname', private=0, lang='Text')
    id_from_the_link = get_paste_id(link)
    dictionary_with_data = get_paste(id_from_the_link)
    id_from_the_dictionary_with_data = dictionary_with_data['pid']

    assert (id_from_the_link == id_from_the_dictionary_with_data)


def test_get_paste_raw_text():
    """ 1.create link
        2.paste link and receieve only my id
        3.take text from the dict get_paste
        4.take key raw from the dictinary with data
        5.take text by id"""
    link = create_paste(text='this is my text', title='some title',  name='myname', private=0, lang='Text', expire='1', reply='1')
    id_from_the_link = get_paste_id(link)
    dictionary_with_data = get_paste(id_from_the_link)
    raw_from_the_dictionary_with_data = dictionary_with_data['raw']
    text_from_the_dictionary = get_paste_raw_text(id_from_the_link)

    assert (raw_from_the_dictionary_with_data == text_from_the_dictionary)


def test_get_list_available_languages_len():
    """len of ditctionary with the languages """
    dictionary_with_languages = get_list_available_languages()

    assert(len(dictionary_with_languages) > 30)


def test_get_list_available_languages():
    """ 1.languages from the list in the dictionary with languages.keys()
        2.create list with true/false """
    dictionary_with_languages = get_list_available_languages()
    keys_with_languages = dictionary_with_languages.keys()
    BoolLanguages = []
    list_with_some_languages = ['ruby', 'java5', 'cpp', 'scala', 'python', 'text', 'mysql', 'csharp', 'css', 'javascript', 'php']
    for every_language in list_with_some_languages:
        if every_language in keys_with_languages:
            BoolLanguages.append(True)
        else:
            BoolLanguages.append(False)

    assert(all(BoolLanguages))


def test_get_random_paste():

    dictionary_with_random_paste = get_random_paste()
    dictionary_with_random_paste_keys = dictionary_with_random_paste.keys()
    BoolRandomPaste = []
    list_with_values = ['lang', 'title', 'name', 'url']
    for every_value in list_with_values:
        if every_value in dictionary_with_random_paste:
            BoolRandomPaste.append(True)
        else:
            BoolRandomPaste.append(False)

    assert(all(BoolRandomPaste))
