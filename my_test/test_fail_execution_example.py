import pytest

@pytest.mark.xfail
@pytest.mark.great
def test_greater():
   num = 100
   assert num > 100


@pytest.mark.xfail
@pytest.mark.great
def test_greater_equal():
   num = 100
   assert num >= 100

@pytest.mark.skip
@pytest.mark.great
def test_less():
   num = 100
   assert num < 200