from typing import Optional

import requests
import pytest
import numpy as np
import pandas as pd
from unittest import mock

def test_case_1():
    pass


def test_case_2():
    assert 1 == 1


# this function is usually define in a separate file
# you need to do import like from some_file import return_one
def return_one():
    return 1


def test_return_one():
    assert return_one() == 1


# it will take stuff like
# `Frank Xia` -> `Frank`
# `Frank_Xia` -> `Frank`
# `FrankXia` -> Raise
def parse_first_name(first_last_mix: str) -> str:
    # Optional[str] means str or None
    first_last_mix = first_last_mix.replace('_', ' ').replace('-', ' ')
    splits = first_last_mix.split(' ')
    if len(splits) < 2:
        raise ValueError('cannot parse first name')
    return splits[0]



@pytest.mark.parametrize(
    "input_name, expected_output",
    [
        ("Frank Xia", "Frank"),
        ("Frank_Xia", "Frank"),
        ("Frank-Xia", "Frank"),
    ]
)
def test_parse_first_name_smarter(input_name: str, expected_output: Optional[str]):
    assert parse_first_name(input_name) == expected_output


@pytest.mark.parametrize(
    "input_name",
    [
        ("FrankXia"),
        ("Frank/Xia"),
        ("Frank'Xia"),
        # ("Frank Xia"),  # this will fail the test case as no valueerror will be raised
    ]
)
def test_parse_first_name_expect_failure(input_name: str):
    with pytest.raises(ValueError):
        parse_first_name(input_name)


def long_function():
    import time
    time.sleep(100000000)
    return np.random.rand(1)


def return_long_function():
    return long_function()


def test_return_long_function():
    # assume `long_function` is tested, and mock it's behavior:
    with mock.patch(__name__ + '.long_function', return_value=5):
        assert return_long_function() == 5


def process_data(file_name: str) -> tuple:
    df = pd.read_csv(file_name)
    return df.shape


def test_process_data():
    df = pd.DataFrame({"a": [1,2], "b": [1,2]})
    with mock.patch('pandas.read_csv', return_value=df):
        assert process_data('this can be anything') == df.shape


def scrape_website():
    return requests.get('www.google.com')


def test_scrape_website():
    response = 'sdflkjasdf asf '
    with mock.patch('requests.get', return_value=response):
        assert scrape_website() == response


# fixture
@pytest.fixture
def my_fruit():
    return 'apple'


@pytest.fixture
def fruit_basket(my_fruit):
    return [my_fruit, 'banana']


def test_my_fruit_in_basket(my_fruit, fruit_basket):
    assert my_fruit in fruit_basket
