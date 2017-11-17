#!/usr/bin/python
# coding=utf-8

import unittest
from public.setup import Request
import requests
class TestSpeed(unittest.TestCase):
		
	def test_speed(self):
		r = Request('测速').req()
		self.assertEqual(r.status_code, 200)





