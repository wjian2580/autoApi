#!/usr/bin/python
# coding=utf-8

import unittest
from public.setup import req
class TestHotSearch(unittest.TestCase):
		
	def test_hot_search(self):
		r = req('热搜')
		self.assertEqual(r.status_code, 200)




