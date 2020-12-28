#!/usr/bin/env python3

from kumon import *

import unittest


class TestKumon(unittest.TestCase):
    """
    Test class
    """

    def test_div(self):
        """
        Test div function
        """
        testcase = "17 5"
        expected = "3R2"
        self.assertEqual(div(testcase), expected)

    def test_improper2mixed(self):
        """
        Test improper2mixed function
        """
        testcase = "17 5"
        expected = "3 2/5"
        self.assertEqual(improper2mixed(testcase), expected)

    def test_mixed2improper(self):
        """
        Test mixed2improper function
        """
        testcase = "3 2 5"
        expected = "17/5"
        self.assertEqual(mixed2improper(testcase), expected)


unittest.main()
