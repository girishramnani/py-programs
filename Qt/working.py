import logging
import sys
import traceback

class StreamToLogger(object):

    def __init__(self, logger, log_level, std):
        self.logger = logger
        self.log_level = log_level
        self.linebuf = ''
        self.std = std

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())
            self.std.write(line+"\n")
            self.std.flush()

    def flush(self):
        return

logging.basicConfig(
   level=logging.DEBUG,
   format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
   filename="history.log",
   filemode='a'
)

stdout_logger = logging.getLogger('STDOUT')
sl = StreamToLogger(stdout_logger, logging.INFO, sys.__stdout__)
sys.stdout = sl

stderr_logger = logging.getLogger('STDERR')
sl = StreamToLogger(stderr_logger, logging.ERROR, sys.__stderr__)
sys.stderr = sl

sl.write("hello working this is ?")

