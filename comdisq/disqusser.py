
from threading import Thread
from router import Router
from langage import LangProc
from disq_frame import DisqFrame

class Member():

    def __init__(self, contact_num, date_stamp):
        self.identifier = contact_num
        self.date_joined = date_stamp
        self.group_requests = []
        self.group = ''
        
    def getIdentifier(self):
        return self.identifier
    
    def getDateJoined(self):
        return self.date_joined

    def setGroup(self, group):
        self.group = group

    def exitGroup(self):
        self.group = ""
    
    def addGroupRequest(self, group):
        self.group_requests.add(group)

class Group():

    def __init__(self, leader, topic):
        self.topic = topic
        self.leader = leader
        self.members = []
        self.addMember(leader)
        " Maybe add random moderator "

    def addMember(self, member):
        if member not in self.members:
            self.members.add(member)
            member.setGroup(self)
            return true
        else:
            return false
    
    def removeMember(self, member):
        if member in self.members:
            self.members.remove(member)
            member.exitGroup()
            return true
        else:
            return false
    def dissolve(self):
        for member in self.members:
            self.members.remove(member)
            member.exitGroup()
        
class Disqusser():
    
    def __init__(self):
        self.recieve_queue = []
        self.send_queue    = []
        
        self.router = Router()
        self.language = LangProc()

        self.members = []
        self.groups = []

    def run(self):

        router.run(recieve_queue, send_queue)

        disq_frame = DisqFrame()
        while true:
            if recieve_queue.len > 0:
                
                disq_frame = recieve_queue.pop
                disq_frame = language.process(disq_frame)
                self.decideOperation(disq_frame)
                


    def decideOperation(self, disq_frame):
        op_code = disq_frame.getOpCode()
        usr_id = disq_frame.getContact()
        member = self.findMember(usr_id)

        if op_code == JOIN_OP:
           registerMember(usr_id) 
            

        elif op_code == MSG_OP:
            if member.group is not '':
                recipients = member.getGroup()
                recipients.remove(member)
                for recipient in recipients:
                    disq_frame.setRecipient(recipient)
                    self.send_queue.push(disq_frame)
        elif op_code == LFG_OP:
            group = self.constructGroup(member, topic)  
            self.groups.append(group)
            
    def constructGroup(self, leader, topic):
        group = Group(leader, topic)
        for member in self.members:
            if not member.getGroup:
                sendGroupRequest(group, member)
        return group
    
    def sendGroupRequest(self, group, member):
        usr_id = member.getContact()
        topic = group.getTopic()
        disq_frame = DisqFrame(REQ_OP, "Would You Like to Join: " + topic, usr_id)
        member.addGroupRequest(group)
        self.send_queue.push(disq_frame)
   

    def registerMember(self, usr_id):
        member = Member(disq_frame.user, '')
        self.members.add(member)
        self.sendMessage("Thanks for joining", usr_id)

    def findMember(usr_id):
        for member in self.members:
            if member.identifier == usr_id:
                return member

    def sendMessage(self, text, usr_id):
        disq_frame = DisqFrame(MSG_OP, text, usr_id)
        self.send_queue.push(disq_frame)
