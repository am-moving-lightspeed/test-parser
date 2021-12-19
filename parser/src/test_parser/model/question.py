from typing import AnyStr
from typing import Dict
from typing import List
from uuid import uuid4


class Question:

    def __init__(self, question: AnyStr):
        self._q: AnyStr = question
        self._wrong: List[AnyStr] = []
        self._correct: List[AnyStr] = []


    def add_wrong_option(self, option: AnyStr) -> 'Question':
        if option not in self._wrong:
            self._wrong.append(option)
        return self


    def add_correct_option(self, option: AnyStr) -> 'Question':
        if option not in self._correct:
            self._correct.append(option)
        return self


    def to_dict(self) -> Dict:
        answers: List[Dict] = []
        for ans in self._wrong:
            answers.append(self._answer_to_dict(ans))
        for ans in self._correct:
            answers.append(self._answer_to_dict(ans, is_correct = True))

        return {
          'Id':      str(uuid4()),
          'Name':    self._q,
          'Answers': answers
        }


    @staticmethod
    def _answer_to_dict(answer: AnyStr, is_correct = False) -> Dict:
        return {
          'Id':     str(uuid4()),
          'Name':   answer,
          'IsTrue': is_correct
        }
