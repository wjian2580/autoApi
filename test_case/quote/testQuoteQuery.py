#!/usr/bin/python
# coding=utf-8

import unittest
from public.setup import Request
class TestQuoteQuery(unittest.TestCase):
		
	def test_trade_query(self):
		r = Request('行情查询').req()
		self.assertEqual(r.status_code, 200)




