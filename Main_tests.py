# !/usr/local/bin/python
# -*- coding: utf-8 -*-
import unittest
from . import BaseElement, BaseAction, BasePage 

class TestMethos(unittest.TestCase):
    def test_CreateElement(self):
        self.assertEqual('foo', 'foo')

    def test_CreateAction(self):
        self.assertEqual('foo', 'foo')

    def test_CreatePage(self):
        self.assertEqual('foo', 'foo')

if __name__ == '__main__':
    unittest.main()
