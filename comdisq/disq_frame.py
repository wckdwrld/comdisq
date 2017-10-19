import sys
import os


class DisqFrame:

    def __init__(self, op_code, text, user):
        self.op_code = op_code
        self.context = text
        self.contact = user
        self.recipient = ''

    def getOpCode():
        return self.op_code

    def setOpCode(code):
        self.op_code = code

    def getContext():
        return context

    def setContext(word_list):
        context = word_list

    def getContact():
        return contact

    def setContact(user):
        self.contact = user
    
    def setRecipient(self, recipient):
        self.recipient = recipient

