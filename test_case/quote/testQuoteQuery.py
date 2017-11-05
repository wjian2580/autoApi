#!/usr/bin/python
# coding=utf-8

import unittest
from public.setup import req
class TestQuoteQuery(unittest.TestCase):
		
	def test_trade_query(self):
		r = req('交易查询')
		self.assertEqual(r.status_code, 200)




