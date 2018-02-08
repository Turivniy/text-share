import pytest
from text_paste import *
from tools import *


@pytest.mark.skip(reason = "#Bug #1 Expire is -1 instead of positive Value")
def test_create_paste_with_expire_negative():
    """Test create paste with expire field equal -1 """

    link = create_paste(text='text', title='',  name='Olga', private=0, lang='Text', expire='-1' )
    id_from_the_link = get_paste_id(link)
    dictionary_with_data = get_paste(id_from_the_link)
    url_from_the_dictionary_with_data = dictionary_with_data['url']

    assert (url_from_the_dictionary_with_data == link)

def test_create_paste_with_expire_zer0():
    """Test create paste with expire field equal 0 """

    link = create_paste(text='text', title='',  name='Olga', private=0, lang='Text', expire='0' )
    id_from_the_link = get_paste_id(link)
    dictionary_with_data = get_paste(id_from_the_link)
    url_from_the_dictionary_with_data = dictionary_with_data['url']

    assert (url_from_the_dictionary_with_data == link)

@pytest.mark.skip(reason = "#Bug #2 Expire is string instead of Int Value (time)")
def test_create_paste_with_expire_string():
    """Test create paste with expire fiels equal STRING"""

    link = create_paste(text='text', title='',  name='Olga', private=0, lang='Text', expire='abc' )
    id_from_the_link = get_paste_id(link)
    dictionary_with_data = get_paste(id_from_the_link)
    url_from_the_dictionary_with_data = dictionary_with_data['url']

    assert (url_from_the_dictionary_with_data == link)

@pytest.mark.skip(reason = "#Bug #3 Value Private 3 instead of 1 or 0")
def test_create_paste_with_private_number_3():
    """Test create paste with Private value equal 3 """

    link = create_paste(text='text', title='',  name='Olga', private=3, lang='Text', expire='1' )
    id_from_the_link = get_paste_id(link)
    dictionary_with_data = get_paste(id_from_the_link)
    url_from_the_dictionary_with_data = dictionary_with_data['url']

    assert (url_from_the_dictionary_with_data == link)

@pytest.mark.skip(reason = "#Bug #4 Value Private equal STRING instead of 1 or 0") 
def test_create_paste_with_private_number_string():
    """Test create paste with Private value equal 'abc' """

    link = create_paste(text='text', title='',  name='Olga', private='abc', lang='Text', expire='1' )
    id_from_the_link = get_paste_id(link)
    dictionary_with_data = get_paste(id_from_the_link)
    url_from_the_dictionary_with_data = dictionary_with_data['url']

    assert (url_from_the_dictionary_with_data == link)

@pytest.mark.skip(reason = "#Bug #5 Value Private -1 instead of 1 or 0") 
def test_create_paste_with_private_negative():
    """Test create paste with Private value equal -1 """

    link = create_paste(text='text', title='',  name='Olga', private=-1, lang='Text', expire='1' )
    id_from_the_link = get_paste_id(link)
    dictionary_with_data = get_paste(id_from_the_link)
    url_from_the_dictionary_with_data = dictionary_with_data['url']

    assert (url_from_the_dictionary_with_data == link)

@pytest.mark.skip(reason = "# Bug #6 Empty field language")
def test_create_paste_with_empty_field_lang():
    """Test create paste with empty field lang """

    link = create_paste(text='text', title='',  name='Olga', private=0, lang=' ', expire='1' )
    id_from_the_link = get_paste_id(link)
    dictionary_with_data = get_paste(id_from_the_link)
    url_from_the_dictionary_with_data = dictionary_with_data['url']

    assert (url_from_the_dictionary_with_data == link)

def test_create_paste():
    """ Test create paste
        1.create link
        2.paste link and receieve only my id
        3.take id from the dict get_paste
        4.take key url from the dict
        5.link from the dictionary_with_data == created link  """
    link = create_paste(text='this is my text', title='some title',  name='myname', private=0, lang='Text', expire='1')
    id_from_the_link = get_paste_id(link)
    dictionary_with_data = get_paste(id_from_the_link)
    url_from_the_dictionary_with_data = dictionary_with_data['url']

    assert (url_from_the_dictionary_with_data == link)  

def test_get_paste_raw_text():
    """ Test Get raw text paste
        1.create link
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

def test_get_paste_id():
    """ Test get ID from the paste text
        1.create link
        2.paste link and receieve only my id
        3.take text from the dict get_paste
        4.take key id from the dict """
    link = create_paste(text='this is my text', title='some title',  name='myname', private=0, lang='Text')
    id_from_the_link = get_paste_id(link)
    dictionary_with_data = get_paste(id_from_the_link)
    id_from_the_dictionary_with_data = dictionary_with_data['pid']

    assert (id_from_the_link == id_from_the_dictionary_with_data)

def test_get_list_available_languages_len():
    """Test len of dictionary with the languages """
    dictionary_with_languages = get_list_available_languages()

    assert(len(dictionary_with_languages) > 30)

def test_get_list_available_languages():
    """ Test get list available languages 
        Returns:
            True: all languages are present ,like in documentation"""
     
    assert(tools_get_list_available_languages())

def test_get_random_paste():
    """ Test get random paste
        Returns:
            True: required fields('lang', 'title', 'name', 'url') are present in the paste"""
 
    assert(tools_get_random_paste())
