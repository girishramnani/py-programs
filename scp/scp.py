from optparse import OptionParser
import os

def parse_args(args=None):
    parser = OptionParser()
    parser.add_option("-v","--verbose",action="store_true",default=False,dest="verbose",help="print each file that has been copied")
    parser.add_option("-p","--path",dest="path",\
            help="the file or the directory you want to copy",default=os.path.curdir)
    parser.add_option("-d","--dest",dest="dest",help="""Server ip and location in format <user>@<ip>:<path> , similar to what is prefered by scp""") 
    parser.add_option("-i",dest="pem_file",help="""pem file for  the server when required extra security""")

    if args:
        return parser.parse_args(args)
    return parser.parse_args() 


class PathError(Exception):
    def __init__(self,*args,**kwargs):
        super(PathError,self).__init__(*args,**kwargs)

class SCP(object):

    def __init__(self,pem_file=None,verbose=False,test=False):
        self.test= test
        self.pem_file=pem_file
        self.verbose = verbose

    def show_message(self,message):
        if self.verbose:
            print(message)
    
    def send_directory(self,directory,dest_dir):
        if not os.path.isdir(directory):
            raise PathError("{} is not a directory".format(directory))
        for dirname,_,filename in os.walk(directory):
            for file in filename:
                combined_name = "".join((dirname,os.path.sep,file))
                yield self.send_file(combined_name,dest_dir)

            
    def send_file(self,file,dest):
        command_list = ["scp"]
        if self.pem_file:
            command_file.extend(["-i",self.pem_file])
        command_list.extend((file,dest))

        return " ".join(command_list)

    def execute(self,command):
        return os.system(command)




    
    
