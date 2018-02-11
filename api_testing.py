import unittest
from text_paste import *


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.MAIN_API_URL = 'http://text-share.com/api/'
        self.paste_create_url = 'http://text-share.com/api/create'
        self.list_available_languages_url = 'http://text-share.com/api/langs'
        self.paste_random_url = 'http://text-share.com/api/random'
        self.paste_id_url = 'http://text-share.com/api/paste/[pasteid]'

    def test_create_paste(self):
        '''Verify that user can create a paste with particular parameters'''
        self.assertTrue(create_paste(self.paste_create_url, data={'text': 'text for test', 'name': 'Ahmed', 'lang': 'Text', 'private': 1}))

    def test_create_paste_with_expire_time(self):
        '''Verify that user can create a paste with with expire time'''
        self.assertTrue(create_paste(self.paste_create_url, data={'text': 'text for test expire time', 'expire': 5}))

    def test_paste_expire_time_zero(self):
        '''BUG#1: User can input zero as expire time value.
       Verify that User can't input ZERO as expire time value
       Expected result: user can't input zero as expire time value
       Actual result: user can input zero as value'''
        self.assertFalse(create_paste(self.paste_create_url, data={'text': 'test zero', 'expire': 0}))

    def test_expire_time_minus(self):
        '''BUG#2: User can input negative value as expire time.
       Verify that user can't input negative value (-1) as expire time
       Expected result: user can't input -1 as expire time
       Actual result: user can input -1 as expire time'''
        self.assertFalse(create_paste(self.paste_create_url, data={'text': 'test -1', 'expire': -1}))

    def test_expire_time_type(self):
        '''BUG#3: User can input a string instead of int as Expire value.
       Verify that user can't input a string (abc) instead of int as Expire value
       Expected result: user can't input string instead of int
       Actual result: User can input string, create a paste and get url in response'''
        self.assertFalse(create_paste(self.paste_create_url, data={'text': 'this is test', 'expire': 'abc'}))

    def test_create_paste_with_unknown_language(self):
        '''BUG#4: User can create paste by inputting unknown language (lang = No lang).
       Verify that user can't create a paste when he inputs unknown language (lang = No lang)
       Expected result: user should input language from available language list
       Actual result: user can input any string as language value'''
        self.assertFalse(create_paste(self.paste_create_url, data={'text': 'another test', 'lang': 'No lang'}))

    def test_paste_privacy(self):
        '''Verify that user can create a private paste'''
        self.assertTrue(create_paste(self.paste_create_url, data={'text': 'another test', 'private': 0}))

    def test_privacy_input(self):
        '''BUG#5: User can create paste by inputting a string instead of int as Privacy value (Private = word).
       Verify that user can't input a string instead of int as a Privacy value (Private = word)
       Expected result: user should input 0 or 1 as value for Private
       Actual result: User can input string as privacy value and create paste'''
        self.assertFalse(create_paste(self.paste_create_url, data={'text': 'another test', 'private': 'word'}))

    def test_empty_content(self):
        '''BUG#6: User can create a paste and get url in response without filling the required field (content field).
       Verify that user cannot create a paste without filling the paste field (this field is required)
       Expected result: user should fill (content field) to create a paste
       Actual result: user can create a paste with empty content'''
        self.assertFalse(create_paste(self.paste_create_url, data={'text': ''}))

    def test_paste_url(self):
        '''Verify that user can get url after creating a paste'''
        self.assertTrue(self.paste_create_url, requests.codes.ok)

    def test_paste_response(self):
        '''Verify that user can get response for his paste as a text'''
        self.response_create_paste = requests.post(self.paste_create_url)
        self.assertTrue(self.response_create_paste.text, requests.codes.ok)

    def test_available_languages(self):
        '''Verify that user can get the list of available languages'''
        self.assertTrue(get_list_available_languages(), requests.codes.ok)

    def test_language_response_json(self):
        '''Verify that user get response in json of available languages'''
        self.response_langs = requests.get(self.list_available_languages_url)
        self.assertTrue(self.response_langs.json(), requests.codes.ok)

    def test_random_paste(self):
        '''Verify that user can get a random paste'''
        self.assertTrue(self.paste_random_url, requests.codes.ok)

    def test_random_response_json(self):
        '''Verify that user can get a random paste as json'''
        self.response_random = requests.get(self.paste_random_url)
        self.assertTrue(self.response_random.json(), requests.codes.ok)
    
    def test_get_paste_id(self):
        '''Verify that user can get paste url with id'''
        self.assertTrue(self.paste_id_url[27:], requests.codes.ok)

    def test_get_paste_response_json(self):
        '''Verify that user gets paste response url and id as json'''
        self.response_paste_id = requests.get('{}paste/{}'.format(MAIN_API_URL, 'pasteid'))
        self.assertTrue(self.response_paste_id.json(), requests.codes.ok)

    def test_get_paste_raw_text(self):
        '''Verify that user can get paste url as raw text'''
        self.response_paste_id = requests.get(self.paste_id_url)
        self.assertTrue(self.response_paste_id.raw, requests.codes.ok)

    def test_get_paste_content(self):
        '''Verify that user will not get paste url content'''
        self.response_paste_id = requests.get(self.paste_id_url)
        self.assertTrue(self.response_paste_id.content, requests.codes.ok)


if __name__ == '__main__':
    unittest.main()
