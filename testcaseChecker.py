__author__ = 'girish'



import argparse
import os
import subprocess


def parse_args():
    global argparser
    argparser = argparse.ArgumentParser(
        description="tool for compititive coders to provide test cases from file and provide an output file. \n"
                    "And then the program will check if the test case succeeds."
                    "This programs can be used to check ur programs output based on testcases given by websites such "
                    "as hackerrank")
    argparser.add_argument("-i", action='store', dest='inputfile', help="the input program which you wanna test",required=True)
    argparser.add_argument("-t", "--test", action='store', dest='testfile', help='the testcases in a txt file',required =True)
    argparser.add_argument("-o", "--out", action='store', dest='output', help='the output expected in a txt file',required =True)

    return argparser.parse_args()

def get_output(args):
    infile = subprocess.Popen("python {}".format(args.inputfile),stdin=subprocess.PIPE,stdout=subprocess.PIPE)
    with open(args.testfile) as testfile:
        out = infile.communicate(input="".join(testfile.readlines()).encode())
        return _format_input(out)

def _format_input(input_tuple):
    out = input_tuple[0].decode()
    out= out.splitlines()
    return out


def check_result_against_out(args,out_tuple):
    with open(args) as outfile:
        counter=1
        bo=True
        for word in outfile.readlines():
            word = word.strip()
            if word != out_tuple[counter -1]:
                print("OUTPUT fails at {} \n \t EXPECTED : {} \t GOT: {} \n\n".format(counter,word,out_tuple[counter-1]))
                bo=False
            counter+=1
        print("Test Case Passed") if bo else print("Test Case Failed")



args = parse_args()
tup = get_output(args)
check_result_against_out(args.output,tup)

