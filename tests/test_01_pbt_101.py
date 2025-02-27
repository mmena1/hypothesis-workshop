"""
These exercises are meant to give you an idea of how Hypothesis work.
You will also write your first property-bases test and get up to speed
for the upcoming exercises.
"""

import pytest
from hypothesis import given, strategies as st

@given(
    st.characters()
)
def test_char_to_ascii_to_char(value):
    assert chr(ord(value)) == value

# Exercise 2: Open a Python shell (with your venv activated)
# Inspect the values generated by the intergers strategy by using the .example() method.
# Do it multiple times.
#
# >>> import hypothesis.strategies as st
# >>> numbers = st.integers()
# >>> numbers.example()
# 0
# >>> numbers.example()
# 1262821532
# >>> numbers.example()
# -42
# ...

# Exercise 3: Replace the tests of the "square" function with one or more Hypothesis tests.
# Use the "integers" strategy to ask Hypothesis for random integer values.
# See https://hypothesis.readthedocs.io/en/latest/data.html#hypothesis.strategies.integers
# Thanks to @seifertm for this excercise

def square(i: int) -> int:
    return i*i

@pytest.mark.skip
def test_square_positive_number():
    number = 5
    result = square(number)
    assert result == 25


@pytest.mark.skip
def test_square_negative_number():
    number = -10
    result = square(number)
    assert result == 100


@pytest.mark.skip
def test_square_zero():
    number = 0
    result = square(number)
    assert result == 0

# Your strategy goes here
@given(st.integers())
def test_square(value):
    assert square(value) == value**2
    # Your code goes here


# Exercise 4: Replace the unit tests of the "sort" built-in Python function, for a property based function.
# Tip 1: Use the one_of strategy (https://hypothesis.readthedocs.io/en/latest/data.html#hypothesis.strategies.one_of)
# along with the lists one (https://hypothesis.readthedocs.io/en/latest/data.html#hypothesis.strategies.lists)
# Tip 2: remember that the last element of a sorted list is equal to the max element of the that list.

@pytest.mark.skip
def test_sorted_numeric_list():
    numeric_list = [0, -45, 2, 10]
    assert sorted(numeric_list) == [-45, 0, 2, 10]

@pytest.mark.skip
def test_sorted_char_list():
    char_list = ['z', 's', 'a', 'm']
    assert sorted(char_list) == ['a', 'm', 's', 'z']

@pytest.mark.skip
def test_sorted_char_list():
    float_list = [100.23, 0.1, -1232.4232, 2321]
    assert sorted(float_list) == [-1232.4232, 0.1, 100.23, 2321]

# strategy goes here
@given(
        st.one_of(st.lists(st.characters(), min_size=1),
                  st.lists(st.integers(), min_size=1),
                  st.lists(st.floats(allow_nan=False), min_size=1))
)
def test_sorted_list(value):
    assert sorted(value)[-1] == max(value)
    # Your code goes here


# Exercise 5: Open a Python shell (with your venv activated)
# Inspect the values generated by the strategy above by using the .example() method.
# Do it multiple times.
#
# >>> import hypothesis.strategies as st
# >>> elements = your_strategy_here
# >>> elements.example()
# >>> ????