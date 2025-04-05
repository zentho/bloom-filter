import pytest
from bloom_filter import BloomFilter


def test_empty_bloom_filter():
    bf = BloomFilter(m=1000, expected=100)
    assert bf.exists("test") is False


def test_single_insertion():

    bf = BloomFilter(m=1000, expected=100)
    bf.add("apple")

    assert bf.exists("apple") is True

    # typically a very low false positive chance
    # but verified externally either way, so usable for test case
    assert bf.exists("banana") is False


def test_multiple_insertions():

    bf = BloomFilter(m=1000, expected=100)
    items = ["apple", "banana", "cherry"]
    for item in items:
        bf.add(item)
    for item in items:
        assert bf.exists(item) is True

    # checked externally again like mentioned above
    assert bf.exists("date") is False


def test_non_string_items():

    bf = BloomFilter(m=1000, expected=100)
    items = [42, 3.14, (1, 2)]

    # checks if diverse types work
    for item in items:
        bf.add(item)
    for item in items:
        assert bf.exists(item) is True


def test_salt_variation():

    bf1 = BloomFilter(m=1000, expected=100, salt="salt1")
    bf2 = BloomFilter(m=1000, expected=100, salt="salt2")
    bf1.add("apple")
    bf2.add("apple")
    assert bf1.exists("apple") is True
    assert bf2.exists("apple") is True


def test_invalid_parameters():

    with pytest.raises(ZeroDivisionError):
        BloomFilter(m=1000, expected=0)
