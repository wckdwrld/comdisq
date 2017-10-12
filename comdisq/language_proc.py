from nltk import word_tokenize
from nltk.corpus import stopwords

class LangProc(self):

    def initialProc(message):
        tokenized_message = word_tokenize(message)
        for token in tokenized_message:
            if token in stopwords:
                tokenized_message.remove(token)
        return tokenized_message


    def langRouter(message):
        tokenized_message = self.initialProc(message)    
        
        if 'join' in tokenized_message:
            return 1

        if 'conversation' in tokenized_message:
            return 2

    return 3
