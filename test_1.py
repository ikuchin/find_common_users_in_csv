import random
from unittest import TestCase
from solution import find_users
import hashlib

from generate_files import GenerateFile
from memory_profiler import memory_usage


class TestFindUsers(TestCase):
    def test_1KiB(self):
        random.seed(1)

        GenerateFile('1_1KiB.csv', '1 KiB')
        GenerateFile('2_1KiB.csv', '1 KiB')

        mem_usage_now = memory_usage(max_usage=True)
        (mem_usage, common) = memory_usage(
            (find_users, ('1_1KiB.csv', '2_1KiB.csv')),
            max_usage=True,
            retval=True,
            max_iterations=1,
        )

        self.assertLess(mem_usage - mem_usage_now, 0.006, 'Function using too much memory')

        self.assertEqual([0, 7, 11, 14, 16], sorted(common))

    def test_1MiB(self):
        random.seed(1)

        GenerateFile('1_1MiB.csv', '1 MiB')
        GenerateFile('2_1MiB.csv', '1 MiB')

        mem_usage_now = memory_usage(max_usage=True)
        (mem_usage, common) = memory_usage(
            (find_users, ('1_1MiB.csv', '2_1MiB.csv')),
            max_usage=True,
            retval=True,
            max_iterations=1,
        )

        self.assertLess(mem_usage - mem_usage_now, 0.4, 'Function using too much memory')

        r = hashlib.sha1()
        for x in sorted(common):
            r.update(f'{x}'.encode())

        self.assertEqual('359ad08cd4223557c6d6d24b9257c0d40a021eb1', r.hexdigest())

    def test_1GiB(self):
        random.seed(1)

        GenerateFile('1_1GiB.csv', '1 GiB')
        GenerateFile('2_1GiB.csv', '1 GiB')

        mem_usage_now = memory_usage(max_usage=True)
        (mem_usage, common) = memory_usage(
            (find_users, ('1_1GiB.csv', '2_1GiB.csv')),
            max_usage=True,
            retval=True,
            max_iterations=1,
        )

        # Nuts! function that processing 1Gb file, using over 1.5Gb memory! Long live Python!
        self.assertLess(mem_usage - mem_usage_now, 1500, 'Function using too much memory')

        r = hashlib.sha1()
        for x in sorted(common):
            r.update(f'{x}'.encode())

        self.assertEqual('9091b7238511de5f10c7d71190b8c89d3bf95df0', r.hexdigest())
