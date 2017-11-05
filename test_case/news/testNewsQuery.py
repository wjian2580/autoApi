#!/usr/bin/python
# coding=utf-8

import unittest
from public.setup import req
class TestNewsQuery(unittest.TestCase):
		
	def test_news_query(self):
		r = req('资讯查询')
		self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
	unittest.main()


