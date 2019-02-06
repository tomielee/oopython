#!/usr/bin/env python3

"""
Contains all classes for the different types of questions

QUESTION - has a
    answer
    text (the question)
    alternatives (the choices)
    type
TYPE1 - isa - QUESTION
"""

class Question():
    """create question objects TYPE TEXT"""

    TYPE = 'text'

    def __init__(self, answer, text, alternatives):
        """init object"""
        self.answer = answer
        self.text = text
        self.alternatives = alternatives

    def get_text(self):
        """returns text"""
        return self.text

    def get_alternatives(self):
        """returns list of alternatives"""
        return self.alternatives

    def check_answer(self, respons):
        """check if respons == answer """
        x = 0
        if respons.lower().strip() == self.answer.lower():
            x = 1
        else:
            x = 0

        return x

    @classmethod
    def get_type(cls):
        """returns type"""
        return cls.TYPE

class QuestionRadio(Question):
    """inherit from Question. class for Radiobutton"""
    TYPE = 'radiobutton'

    def __init__(self, answer, text, alternatives):
        super().__init__(answer, text, alternatives)


class QuestionCheck(Question):
    """inherit from Question. class for Checkbox"""
    TYPE = 'checkbox'

    def __init__(self, answer, text, alternatives):
        super().__init__(answer, text, alternatives)

    # def check_answer(self, respons):
    #     """check if respons == answer """
    #     if respons.lower().strip() == self.answer.lower():
    #         return 1
    #     else:
    #         return 0


# q1 = Question('svar1', 'är svaret 1?', ('alt1', 'alt2', 'alt3'))
# q2 = QuestionRadio('svar2', 'är svaret 2?', ('alt1', 'alt2', 'alt3'))
# q3 = QuestionCheck('svar3', 'är svaret 3?', ('alt1', 'alt2', 'alt3'))
#
# print(q1.type)
# print(q2.type)
# print(q3.type)
