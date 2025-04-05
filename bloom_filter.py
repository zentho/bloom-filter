# CITATION:
# both formulas copied from https://en.wikipedia.org/wiki/Bloom_filter

import hashlib
import math


class BloomFilter:
    def __init__(self, m, expected, salt=None):
        """
        m (int): size of array
        expected (int): number of expected items
        salt (string): salt for hashes
        """

        self.m = m
        self.n = 0
        self.arr = [False] * m
        self.salt = salt or ''

        # FORMULA 1: mathematically optimal hash count k
        self.k = int((m / expected) * math.log(2))

    def add(self, item):
        for i in range(self.k):

            ind = self._hash(item, i)
            self.arr[ind] = True

        self.n += 1

    def exists(self, item):
        for i in range(self.k):

            ind = self._hash(item, i)

            if not self.arr[ind]:
                print("This item has not yet been seen")
                return False

        # FORMULA 2: approximate probability of false positive
        prob = (1 - math.exp(-self.k * self.n / self.m)) ** self.k
        print(
            f"This item potentially has been seen with false positive chance of {prob * 100}%")
        return True

    def _hash(self, item, i):
        s = f"{self.salt}_{item}_{i}"
        return int(hashlib.sha1(s.encode('utf-8')).hexdigest(), 16) % self.m
