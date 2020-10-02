import json


class QuizzQuestion(object):
    def __init__(self):
        self.question = ""
        self.answers = []
        self.correct_answer = ""

    def __init__(self, question, answers, correct_answer):
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer

    def __str__(self):
        return json.dumps(self.__dict__)

    def add_answers(self, answers):
        self.answers.extend(answers)

    def modify_correct_answer(self, new_correct):
        self.correct_answer = new_correct

    def get_correct_answer(self):
        return self.correct_answer

    def __eq__(self, other):
        if not isinstance(other, QuizzQuestion):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.question == other.question and self.answers == other.answers \
               and self.correct_answer == other.correct_answer
