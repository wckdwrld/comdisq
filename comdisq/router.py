from sms import SMServer 
from disq_frame import DisqFrame
from threading import Thread
import sys

class Router:

    def __init__(self):
        server = SMServer("/dev/ttyUSB0")
        try:
            server.connect()
        except:
            print "SMS Connection Error: " + sys.exc_info()[0]
        raise


    def run(recieve_queue, send_queue):
        sender_thread = Thread(target = sender, args = (send_queue, ))
        reciever_thread = Thread(target = reciever, args = (recieve_queue, ))

        sender_thread.start()
        reciever_thread.start()

        sender_thread.join()
        reciever_thread.join()

    def sender(self, send_queue):
        disq_frame = DisqFrame()
        while true:
            if send_queue.len > 0:
                disq_frame = send_queue.pop()
                "SEND WITH SMS"
                for contact in disq_frame.recipients:
                    server.sendMessage(contact, disq_frame.msg)

    def reciever(self, recieve_queue):
        disq_frame = DisqFrame()
        while true:
            messages = self.server.getMessage()
            for message in messages:
                disq_frame = DisqFrame(NO_OP, messages[0], messages[1])
                recieve_queue.push(disq_frame)

            
            

    


