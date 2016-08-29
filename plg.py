
import base64


class PlagerismEvader(object):

    def __init__(self,filename):
        self.filename = filename

    
    def write(self,base64_string):
        template = \
        """import base64;
output = base64.b64decode("{}").decode()
eval(output)
        """

        return template.format(base64_string)
    
    def evade(self,filename):
        with open(filename,"w") as f:
            f.write(self.write(self.encode()))
        
    def encode(self):
        text = open(self.filename).read()
        return base64.b64encode(text.encode())
    

plger = PlagerismEvader("test.py") # the python file you want to plagerise
plger.evade("test2.py") # the  filename you want to keep
