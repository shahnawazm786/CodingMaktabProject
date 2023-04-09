import pytest
@pytest.fixture
def test_fixture_one():
    val=51
    return val
def test_fixture_two(test_fixture_one):
    a=test_fixture_one/2
    print(a)
    assert a == 25.5

def test_fixture_three(test_fixture_one):
    assert test_fixture_one/3 == 0

def test_fixture_four(test_fixture_one):
    assert test_fixture_one/4 == 3

def test_fixture_five(test_fixture_one):
    assert test_fixture_one/5 == 1



