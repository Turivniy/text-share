import pytest
from text_paste import *


def test_create_paste():

    """create link with id"""
    link = create_paste(text='this is my text', title='title',  name='myname', private=0, lang='Text')
    print "link", link

    """paste link and receieve only my id"""
    my_id = get_paste_id(link)
    print "my_id is", my_id


    """take text from the dict get_paste"""
    dictionary_with_data = get_paste(my_id)
    dictionary_right = get_paste('8aca597c')
    print "dictionary with data", dictionary_with_data

    """take key from the dict"""
    my_url = dictionary_with_data['url']
    print my_url
    
    assert (my_url == link)



