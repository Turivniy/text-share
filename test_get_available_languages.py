import pytest
from text_paste import get_list_available_languages
from tools import tools_get_list_available_languages


def test_get_list_available_languages():
    assert(tools_get_list_available_languages())
