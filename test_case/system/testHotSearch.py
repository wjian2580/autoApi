#!/usr/bin/python
# coding=utf-8

import unittest
from public.setup import Request
class TestHotSearch(unittest.TestCase):
		
	def test_hot_search(self):
		r = Request('热搜').req()
		self.assertEqual(r.status_code, 200)




