NO_OP = 0
JOIN_OP = 1
CONV_OP = 2

from nltk.stem.snowball import SnowballStemmer
from nltk import word_tokenize
from nltk.corpus import stopwords
from operation_frame import OpFrame

class LangProc(self):

    def initialProc(message):
        stemmer = SnowballStemmer('english')
        tokenized_message = word_tokenize(message)
        for token in tokenized_message:
            if token in stopwords:
                tokenized_message.remove(token)
            token = stemmer.stem(token)
        return tokenized_message
    

    def deriveOperation(message, contact):
        op_frame = OpFrame(NO_OP, "", contact)
        tokenized_message = self.initialProc(message)   

        contextMode = checkContext(contact)

        
        if 'join' and 'network' in tokenized_message:
            op_frame.setOpCode(JOIN_OP)

        elif ('start' or 'begin' or 'create') and 'conversation' in tokenized_message:
            op_frame.setOpCode(CONV_OP)
            messageContext = self.deriveMeaning(tokenized_message)
            op_frame.setContext(messageContext)

        return op_frame

    def deriveMeaning(tokenized_message):
        print "Not Yet Implemented, returning original tokenized_message"
        return tokenized_message
        
    def checkContext(op_frame):
        print "Not Yet Implemented"
        return 0
 
