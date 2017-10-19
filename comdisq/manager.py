from disqusser import Disqusser
from threading import Thread
import os


title_art = """/
                __________  __  _______  _________ ____ 
               / ____/ __ \/  |/  / __ \/  _/ ___// __ \
              / /   / / / / /|_/ / / / // / \__ \/ / / /
              / /___/ /_/ / /  / / /_/ // / ___/ / /_/ / 
              \____/\____/_/  /_/_____/___//____/\___\_\ 
"""


class Manager:
    def __init__(self):
        disqusser = Disqusser()

    def displayMenu():
        os.system('clear')
        print(title_art)
        print("1. Start " + menuSelect[0])
        print("2. Stop " + menuSelect[1])
        print("3. Settings " + menuSelect[2])
        print("4. Logs " + menuSelect[3]) 
        print("5. Info " + menuSelect[4])
        
    def start():
        disqusser_thread = Thread(target = self.disqusser.run, args = ())
        disqusser_thread.start()
        disqusser_thread.join()



