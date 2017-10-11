import routeing.py
import Queue


title_art = """/
                __________  __  _______  _________ ____ 
               / ____/ __ \/  |/  / __ \/  _/ ___// __ \
              / /   / / / / /|_/ / / / // / \__ \/ / / /
              / /___/ /_/ / /  / / /_/ // / ___/ / /_/ / 
              \____/\____/_/  /_/_____/___//____/\___\_\ 
"""

class Message:
    def __init__(self, origin, text, timestamp):
        self.origin = origin
        self.text = text
        self.timestamp = timestamp

class Manager:
    def __init__(self):
        router = Router()
        messageQueue = Queue(10) 
        messageHistory = Queue(10)

    def displayMenu():
        os.system('clear')
        print(title_art)
        print("1. Start " + menuSelect[0])
        print("2. Stop " + menuSelect[1])
        print("3. Settings " + menuSelect[2])
        print("4. Logs " + menuSelect[3]) 
        print("5. Info " + menuSelect[4])
        
    def messageHandler():
        while true:
            if self.messageQueue.len > 0:
                currentMessage = self.messageQueue.pop
                router.handle(currentMessage)
                messageHistory.push(currentMessage)

    def messageMonitor():
        print "Not Yet Implemented"


