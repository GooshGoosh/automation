#!/usr/bin/env python3

from 'test_file' import 'test_function'
import unittest


class Test(unittest.TestCase):
	# Test case structure
	def test_basic(self):
		self.assertEqual(test_function(params_to_pass), expected_result)

	# Error test structure
	def test_error(self):
		self.assertRaises(expected_error, test_function, params_to_pass, expected_result)

unittest.main()
