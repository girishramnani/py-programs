import logging
import sys
import traceback
import logging.handlers

class gi:
	def __init__(self,message):
		self.message=message
	def getMessage(self):
		return self.message
	def setMessage(self,message):
		self.message = message
class StreamToLogger(object):

    def __init__(self, logger, log_level, std, handler):
        self.handler = handler
        self.logger = logger
        self.log_level = log_level
        self.linebuf = ''
        self.std = std
        self.gi = gi("")

    def write(self, buf):
        for line in buf.rstrip().splitlines():
        	self.gi.setMessage(line)
			self.logger.log(self.log_level, line.rstrip())
			self.std.write(line+"\n")
			hand.flush()
			self.std.flush()

    def flush(self):
    		self.std.flush()


logging.basicConfig(
   level=logging.DEBUG,
   format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
   filename="history.log",
   filemode='a'
)
hand = logging.handlers.TimedRotatingFileHandler("bot.log", when="S", interval=20)
#my attempt at handling


stdout_logger = logging.getLogger('STDOUT')
sl = StreamToLogger(stdout_logger, logging.INFO, sys.__stdout__, hand)

stderr_logger = logging.getLogger('STDERR')
sl = StreamToLogger(stderr_logger, logging.ERROR, sys.__stderr__, hand)


for i in range(2):
	sl.write("is this working")
