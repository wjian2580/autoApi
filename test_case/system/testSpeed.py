#!/usr/bin/python
# coding=utf-8

import unittest
from public.setup import req
class TestSpeed(unittest.TestCase):
		
	def test_speed(self):
		r = req('测速')
		self.assertEqual(r.status_code, 200)





