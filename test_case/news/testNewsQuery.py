#!/usr/bin/python
# coding=utf-8

import unittest
from public.setup import Request
class TestNewsQuery(unittest.TestCase):
		
	def test_news_query(self):
		r = Request('资讯查询').req()
		self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
	unittest.main()


