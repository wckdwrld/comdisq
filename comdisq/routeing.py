from sms import SMServer 
import sys

class router:

    def __init__(self):
        self.groups = []
        self.users  = []
        server = SMServer("/dev/ttyUSB0")
        try:
            server.connect()
        except:
            print "SMS Connection Error: " + sys.exc_info()[0]
            raise
    


    def add(contact):
        self.users.append(contact)
    
    def remove(contact):
        self.users.remove(contact)

    def initGroups():
        shuffled_users = random.shuffle(self.users)
        group_size = 5
        num_groups = 0
        num_users = self.users.len()
        x = group_size  

        while group_size > 1:
            if (group_size % num_users == 0):
                num_groups = (num_users / group_size)
                break
            else:
                --group_size
        
        while x < group_size:
            --x
            self.groups.append(Group(x))
        

        x = 0

        for user in shuffled_user:
            self.groups[x].append(user) 
            if x == 4:
                x = 0
            else: 
                ++x

    def killGroups():
        groups = []
        for user in users:
            user.cleanseGroup()

    def sendMessage(contact, text):
        server.sendMessage(contact.number, text)

    def getMessage():
        return server.getMessage()

    def broadcast(group, text):
        for contact in group:
            server.sendMessage(contact.number, text)


    def publicBroadcast():
        for contact in self.users:
            server.sendMessage(contaxt.number, text)

class Group:

    def __init__(self, contact_list):
        self.members = contact_list

    def add(contact):
        self.members.append(contact)

    def remove(contact):
        self.members.remove(contact)

class User:

    def __init__(self, mobile, username):
        self.username = username
        self.mobile = mobile
        self.group = []


    def changeMobile(mobile):
        self.mobile = mobile

    def setGroup(group):
        self.group = group.remove(self)

    def cleanseGroup():
        self.group = []
