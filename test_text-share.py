import pytest
from text_paste import *


def test_create_paste():

    """create link with id"""
    text = create_paste(text='this is my text', title='title',  name='myname', private=0, lang='Text')
    print(text)

    """paste link and receieve only my id"""
    my_id = get_paste_id(text)
    print(my_id)


    """take text from the dict get_paste"""
    my_get_paste = get_paste(my_id)
    print (my_get_paste)

    """take key from the dict"""
    my_url = my_get_paste([u'url'])
    print(my_url)
    
    assert (my_url == text)

# def test_get_paste_id():

#     """create link with id"""
#     text = create_paste(text='this is my text', title='title',  name='myname', private=0, lang='Text')
#     print(text)

#     """paste link and receieve only my id"""
#     my_id = get_paste_id(text)
#     print(my_id)

