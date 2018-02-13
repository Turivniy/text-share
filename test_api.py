import unittest
from text_paste import *


class Test_api(unittest.TestCase):

    def setUp(self):
    
        self.MAIN_API_URL = 'http://text-share.com/api/'
        self.paste_create_url = 'http://text-share.com/api/create'
        self.list_available_languages_url = 'http://text-share.com/api/langs'
        self.paste_random_url = 'http://text-share.com/api/random'
        self.paste_id_url = 'http://text-share.com/api/paste/[pasteid]'


    def test_creating_the_paste(self):
        '''Creating the paste with specific parameters'''
        self.assertTrue(create_paste(self.paste_create_url, data={'text': 'something', 'name': 'Alexx', 'lang': 'Text', 'private': 1}))


    def test_creating_the_paste_with_expire_time(self):
        '''Creating the paste with expire time'''
        self.assertTrue(create_paste(self.paste_create_url, data={'text': 'something expire time', 'expire': 5}))


    def test_inputting_zero_as_expire_time(self):
        '''Inputting zero as expire time value'''
        self.assertFalse(create_paste(self.paste_create_url, data={'text': 'test 0', 'expire': 0}))


    def test_inputting_negative_value_as_expire_time(self):
        '''Inputting negative value as expire time'''
        self.assertFalse(create_paste(self.paste_create_url, data={'text': 'test -10', 'expire': -10}))


    def test_inputting_the_string_instead_of_int(self):
        '''Iputting the string instead of int'''
        self.assertFalse(create_paste(self.paste_create_url, data={'text': 'something', 'expire': 'text'}))


    def test_inputting_no_language(self):
        '''Inputting no language'''
        self.assertFalse(create_paste(self.paste_create_url, data={'text': 'something', 'lang': 'No lang'}))


    def test_creating_the_private_paste(self):
        '''Creating the private paste'''
        self.assertTrue(create_paste(self.paste_create_url, data={'text': 'another test', 'private': 0}))


    def test_inputting_the_text_value_in_private_field(self):
        '''Inputting the text value in private field'''
        self.assertFalse(create_paste(self.paste_create_url, data={'text': 'something', 'private': 'text'}))


    def test_creating_the_paste_without_required_fields(self):
        '''Creating the paste without required field'''
        self.assertFalse(create_paste(self.paste_create_url, data={'text': ''}))


    def test_getting_the_url_after_creating_the_paste(self):
        '''Getting the url after creating the paste'''
        self.assertTrue(self.paste_create_url, requests.codes.ok)


    def test_getting_the_response_for_paste(self):
        '''Getting the response for paste as the text'''
        self.response_create_paste = requests.post(self.paste_create_url)
        self.assertTrue(self.response_create_paste.text, requests.codes.ok)


    def test_getting_the_list_of_languages(self):
        '''Getting the list of available languages'''
        self.assertTrue(get_list_available_languages(), requests.codes.ok)


    def test_getting_the_response_in_json_of_languages(self):
        '''Getting the response in json of available languages'''
        self.response_langs = requests.get(self.list_available_languages_url)
        self.assertTrue(self.response_langs.json(), requests.codes.ok)


    def test_getting_the_random_paste(self):
        '''Getting the random paste'''
        self.assertTrue(self.paste_random_url, requests.codes.ok)


    def test_getting_the_random_response_json(self):
        '''Getting the random paste as json'''
        self.response_random = requests.get(self.paste_random_url)
        self.assertTrue(self.response_random.json(), requests.codes.ok)
    
    
    def test_getting_the_paste_id(self):
        '''Getting the paste url with id'''
        self.assertTrue(self.paste_id_url[27:], requests.codes.ok)


    def test_getting_the_paste_response_json(self):
        '''Getting the paste response url and id as json'''
        self.response_paste_id = requests.get('{}paste/{}'.format(MAIN_API_URL, 'pasteid'))
        self.assertTrue(self.response_paste_id.json(), requests.codes.ok)


    def test_getting_the_paste_raw_text(self):
        '''Getting the paste url as raw text'''
        self.response_paste_id = requests.get(self.paste_id_url)
        self.assertTrue(self.response_paste_id.raw, requests.codes.ok)


    def test_getting_the_paste_content(self):
        '''Getting the paste url content'''
        self.response_paste_id = requests.get(self.paste_id_url)
        self.assertTrue(self.response_paste_id.content, requests.codes.ok)


if __name__ == '__main__':
    unittest.main()
