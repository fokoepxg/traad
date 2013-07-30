import os
import unittest

from traad.rope import findit
from traad.test import common


class FinditTests(unittest.TestCase):
    def setUp(self):
        self.proj = common.activate_project({
            'main': ['basic'],
        })

    def tearDown(self):
        common.deactivate()

    def test_find_occurrences(self):
        # Find occurrences of the Foo class
        occ = findit.find_occurrences(
            self.proj,
            8,
            'basic/foo.py')
        self.assertEqual(len(occ), 3)

    def test_find_implementations(self):
        impls = findit.find_implementations(
            self.proj,
            33,
            'basic/overrides.py')
        self.assertEqual(len(impls), 1)

    def test_find_definition(self):
        path = os.path.join(
            common.activated_path('main'),
            'basic', 'bar.py')
        with open(path, 'r') as f:
            code = f.read()
        loc = findit.find_definition(self.proj,
                                     code,
                                     142,
                                     os.path.join('basic', 'bar.py'))
        self.assertEqual(
            loc,
            (os.path.join('basic', 'bar.py'),
             (91, 100), 91, False, 7))

if __name__ == '__main__':
    unittest.main()
