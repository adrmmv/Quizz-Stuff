import unittest
from unittest import TestCase

from test_rest import QuizzQuestion


def generate_question():
    question = "Carlos es tonto?"
    answers = ["Si", "No"]
    correct_answer = "Si"
    return QuizzQuestion(question, answers, correct_answer)


class TestQuestion(TestCase):
    expected_question = "Carlos es tonto?"

    def test_add_answers(self):
        expected_answers = ["Si", "No", "Puede", "Quizas"]
        expected_correct_answer = "Si"
        expected_question = QuizzQuestion(self.expected_question, expected_answers, expected_correct_answer)
        question = generate_question()
        question.add_answers(["Puede", "Quizas"])
        self.assertEqual(question, expected_question)

    def test_modify_correct_answer(self):
        expected_answers = ["Si", "No"]
        expected_correct_answer = "No"
        expected_question = QuizzQuestion(self.expected_question, expected_answers, expected_correct_answer)
        question = generate_question()
        question.modify_correct_answer("No")
        self.assertEqual(question, expected_question)

    def test_get_correct_answer(self):
        expected_correct_answer = "Si"
        question = generate_question()
        self.assertEqual(question.get_correct_answer(), expected_correct_answer)


if __name__ == "__main__":
    tests = unittest.TestLoader().loadTestsFromTestCase(TestQuestion)
    unittest.TextTestRunner(verbosity=2).run(tests)
