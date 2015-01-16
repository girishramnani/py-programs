__author__ = 'Girish'
import socketserver,time
def now():
    return time.ctime(time.time())
class MyClientHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.client_address,now())
        time.sleep(3)
        while True:
            data = self.request.recv(1024)
            if not data:break
            reply = "Echo => {} at {}".format(data,now())
            self.request.send(reply.encode())
        self.request.close()


myaddr = ("",50007)
server = socketserver.ForkingTCPServer(myaddr,MyClientHandler)
server.serve_forever()