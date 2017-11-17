#!/usr/bin/python
# coding=utf-8

import unittest
from public.setup import Request
class TestIpo(unittest.TestCase):
		
	def test_ipo(self):
		r = Request('IPO').req()
		self.assertEqual(r.status_code, 201)




