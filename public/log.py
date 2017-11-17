import logging,os,time
from public import cpm

day = time.strftime("%Y-%m-%d")
time = time.strftime('%H_%M_%S')
log_path = os.path.join('C:\\Users\\wang\\Desktop\\autoApi\\test_result',day)
if not os.path.exists(log_path):
	os.mkdir(log_path)

class Log():
	def __init__(self):
		self.logname = os.path.join(log_path, '%s.log' % time)
		self.logger = logging.getLogger()
		self.logger.setLevel(logging.DEBUG)
		self.formatter = logging.Formatter('[%(asctime)s] - %(name)s] - %(levelname)s: %(message)s')

			
		if not self.logger.handlers:
			# 创建一个FileHandler，用于写到本地文件
			fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')
			fh.setLevel(logging.DEBUG)
			fh.setFormatter(self.formatter)
			self.logger.addHandler(fh)

			# 创建一个StreamHandler,用于输出到控制台
			ch = logging.StreamHandler()
			ch.setLevel(logging.DEBUG)
			ch.setFormatter(self.formatter)
			self.logger.addHandler(ch)

		#fh.close()

	def debug(self, message):
		self.logger.debug(message)

	def info(self, message):
		self.logger.info(message)

	def warning(self, message):
		self.logger.warning(message)

	def error(self, message):
		self.logger.error(message)

if __name__ == "__main__":
	log = Log()
	log.info("---测试开始----")
	log.info("操作步骤1,2,3")
	log.info("----测试结束----")
	

