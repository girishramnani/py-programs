__author__ = 'Girish'

import re

class SpoolCleaner(object):

    def __init__(self,file):
        self.file = file
        self.SQL_regex =  re.compile(r"""SQL>""")
        self.Error_regex = re.compile("ORA")


    def clean(self,outfile):
        buffer =[]
        has_error = False
        with open(outfile,'w') as output_stream:
            with open(self.file,'r') as input_stream:

                for line in input_stream.readlines():


                    if self.SQL_regex.match(line):
                        if len(buffer):
                            if not has_error:
                                output_stream.writelines(buffer)
                            has_error = False
                            buffer.clear()
                    elif self.Error_regex.match(line):
                        has_error=True

                    buffer.append(line)
            if len(buffer):
                output_stream.writelines(buffer)


