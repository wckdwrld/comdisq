
from threading import Thread
from router import Router
from langage import LangProc
from disq_frame import DisqFrame

class Disqusser():
    
    def __init__(self):
        recieve_queue = []
        send_queue    = []

        router = Router()
        language = LangProc()

    def run():

        router.run(recieve_queue, send_queue)

        disq_frame = DisqFrame()
        while true:
            if recieve_queue.len > 0:
                
                disq_frame = recieve_queue.pop
                disq_frame = language.process(disq_frame)
                send_queue.push(disq_frame)


    
