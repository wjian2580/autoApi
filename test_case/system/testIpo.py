#!/usr/bin/python
# coding=utf-8

import unittest
from public.setup import req
class TestIpo(unittest.TestCase):
		
	def test_ipo(self):
		r = req('IPO')
		self.assertEqual(r.status_code, 200)




