import unittest
from public.setup import MyRequest
class TestTradeQuery(unittest.TestCase):
		
	def test_trade_query(self):
		r = MyRequest().req('交易查询')
		assert r.status_code == 200
		json = r.json()
		assert json['cljg'][0]['code'] == 'MP1B000000'

if __name__ == '__main__':
	unittest.main()



