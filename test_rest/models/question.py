import json


class Question(object):
    def __init__(self):
        self.question = ""
        self.answers = []
        self.correctAnswer = ""

    def __init__(self, question, answers, correctAnswer):
        self.question = question
        self.answers = answers
        self.correctAnswer = correctAnswer

    def __str__(self):
        return json.dumps(self.__dict__)

    def addAnswers(self, answers):
        self.answers.extend(answers)

    def modifyCorrectAnswer(self,newCorrect):
        self.correctAnswer = newCorrect

    def getCorrectAnswer(self):
        return self.correctAnswer