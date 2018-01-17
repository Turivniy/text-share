import pytest
from text_paste_1 import *


# def test_create_paste():

#     """create link with id"""
#     link = create_paste(text='this is my text', title='some title',  name='myname', private=0, lang='Text')


#     """paste link and receieve only my id"""
#     id_from_the_link = get_paste_id(link)
    

#     """take id from the dict get_paste"""
#     dictionary_with_data = get_paste(id_from_the_link)
 

#     """take key url from the dict"""
#     url_from_the_dictionary_with_data = dictionary_with_data['url']

    
#     assert (url_from_the_dictionary_with_data == link)

# def test_get_paste_id():

#     """create link"""
#     link = create_paste(text='this is my text', title='some title',  name='myname', private=0, lang='Text')

#     """paste link and receieve only my id"""
#     id_from_the_link = get_paste_id(link)
    
#     """take text from the dict get_paste"""
#     dictionary_with_data = get_paste(id_from_the_link)

#     """take key id from the dict """
#     id_from_the_dictionary_with_data = dictionary_with_data['pid']

#     assert (id_from_the_link == id_from_the_dictionary_with_data)

# def test_get_paste_raw_text():

#     """create link"""
#     link = create_paste(text='this is my text', title='some title',  name='myname', private=0, lang='Text')

#     """paste link and receieve only my id"""
#     id_from_the_link = get_paste_id(link)
    
#     """take text from the dict get_paste"""
#     dictionary_with_data = get_paste(id_from_the_link)

#     """take key raw from the dictinary with data"""
#     raw_from_the_dictionary_with_data = dictionary_with_data['raw']

#     """take text by id"""
#     text_from_the_dictionary = get_paste_raw_text(id_from_the_link)

#     assert (raw_from_the_dictionary_with_data == text_from_the_dictionary)

def test_random_paste():

    """create link"""
    link = create_paste(text='this is my text', title='some title',  name='myname', private=0, lang='Text')
    
    """get random paste"""
    random_paste = get_random_paste()

def 



