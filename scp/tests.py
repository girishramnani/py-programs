import unittest
import scp
import os
class ArgParse_Test(unittest.TestCase):

    def setUp(self):
        self.url ="ubuntu@52.0.1.54:~/" 
    

    def test_only_destination_dir(self):
        args,li = scp.parse_args(["-d",self.url])
        
        self.assertEqual(args.dest,self.url)

    def test_destination_and_host_file(self):
        args,li = scp.parse_args(["-p","scp.py","-d",self.url])
        self.assertEqual(args.path,"scp.py")
        self.assertEqual(args.dest,self.url)
        self.assertEqual(args.verbose,False)

    def test_verbose(self):
        args,li = scp.parse_args(['-v'])
        self.assertEqual(args.verbose,True)
    
    def test_pem_file(self):
        args,li = scp.parse_args(["-i","girish.pem"])
        self.assertEqual(args.pem_file,"girish.pem")


class  SCP_Test(unittest.TestCase):
    def setUp(self):
        self.scp = scp.SCP()
        self.url = "ubuntu@54.0.1.52:~/"

    def test_simple_file_send(self):
        shell_command = self.scp.send_file("testfiles/demo.js","ubuntu@54.0.1.52:~/")
        self.assertEqual(shell_command,"scp testfiles/demo.js {}".format(self.url))
        
    def test_directory_upload(self):
        shell_commands = self.scp.send_directory("testfiles",self.url)
        command = "scp {} {}"
        actual_commands = [command.format("".join(["testfiles/demo-",str(i),".js"]),self.url) for i in range(1,5)]
        self.assertListEqual(actual_commands,list(sorted(shell_commands)))
    

if __name__== "__main__":
    unittest.main()

