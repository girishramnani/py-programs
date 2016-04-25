from watchdog.observers import Observer

class DirectoryWatcher(object):

	def __init__(self,path,recursive=True,max_level=-1):
		self.path = path
		self.recursive = recursive
		self.max_level = max_level
		
	
	def watch(self):
		pass
		
		
