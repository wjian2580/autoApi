#!/usr/bin/python
# coding=utf-8

import unittest
from public.setup import Request
class TestTradeQuery(unittest.TestCase):
		
	def test_trade_query(self):
		r = Request('交易查询').req()
		self.assertEqual(r.status_code, 200)






