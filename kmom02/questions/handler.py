#!/usr/bin/env python3
"""
Contains the handler/manager class for the questions.
"""

from questions import Question, QuestionRadio, QuestionCheck

class QuestionManager():
    """handle all questions and player points"""

    def __init__(self, score=None, quest_count=None):
        """create object with questions"""
        self.score = score if score else 0
        self.quest_count = quest_count if quest_count else 0
        self.max_score = 9
        self.questions = []
        self.add_default_questions()

    def get_score(self):
        """returns player score"""
        return self.score

    def get_max_score(self):
        """returns game max score"""
        return self.max_score

    def has_next(self):
        """if there are more questions than return true"""
        #quest_count = 2, len = 3
        return bool(self.quest_count <= len(self.questions) - 1)

    def get_next(self):
        """returns next question"""
        return self.questions[self.quest_count]

    def get_quest_count(self):
        """returns quest level"""
        return self.quest_count

    def write_session(self, session):
        """
        write self data to session
        store score and quest_count
        session is a dict
        """
        session["game"] = self.to_json()
        #print(session["game"]) #kolla så at to_json fungerar. en dict.

    def read_session(self, session):
        """read data from session"""
        try:
            temp = self.from_json(session["game"]) #your "new object"
            self.score = temp.score
            self.quest_count = temp.quest_count
        except KeyError:
            self.score = self.get_score()
            self.quest_count = self.get_quest_count()

    def to_json(self):
        """serialise data. return a dict"""
        return {
            "score" : self.score,
            "count" : self.quest_count
        }

    @classmethod
    def from_json(cls, json):
        """deserialise the data. return a class"""
        return cls(json["score"], json["count"])

    def reset(self, session):
        """reset SESSION"""
        for key in list(session["game"].keys()):
            session["game"].pop(key)

        self.score = 0
        self.quest_count = 0


    def correct_answer(self, form):
        """check if choice is correct"""
        respons = form["answer"]

        self.score += self.questions[self.quest_count].\
                check_answer(respons)

        self.quest_count += 1

        # self.respons.append(form["answer"])
        # self.score += self.questions[self.quest_count].
        # check_answer(self.respons)


    def add_default_questions(self):
        """add default questions"""

        q1 = Question(
            'LoL',
            'How is Laughing out Loud shortned?',
            '')

        q2 = Question(
            'Cartman',
            "In South Park, what is Eric's last name?",
            '')

        q3 = Question(
            'Bartz',
            'Who is the main character of "Final Fantasy V"?',
            '')

        q4 = QuestionRadio(
            'Clancy',
            'In "The Simpsons" what is the first name of Chief Wiggum?',
            ('David', 'Bart', 'Clancy', 'Arthur'))

        q5 = QuestionRadio(
            'Barry Trotter',
            '"Bored of the Rings" is a parody of "Lord of the \
            Rings". "Harry Potter" has a similar parody in almost \
            the same style. What is the title of this book? ', \
            ('Arry Halfmass', 'Derek Otter', 'Carry on Potter', \
            'Barry Trotter'))

        q6 = QuestionRadio(
            'Capricciosa',
            'How do you spell the pizza with salami and mushrooms?',\
            ('Capprichiosa', 'Caprisiosa', 'Capricciosa'))

        q7 = QuestionCheck(
            'Gul Richard',
            "Which ones are swedish apples?",
            ('Anna Book', 'Funny', 'Gul Richard', 'Crisps', 'Yummy', ))

        q8 = QuestionCheck(
            'Batman',
            "Superheroes?",
            ('Batman', 'Catman', 'Fatman', 'Hatman', 'Chatman', ))

        q9 = QuestionCheck(
            'Algeria',
            "The tenth biggest country in the world (Area)?",
            ('China', 'Algeria', 'Kazakhstan', 'Australia', 'India', 'Russia'))

        self.questions.append(q1)
        self.questions.append(q2)
        self.questions.append(q3)
        self.questions.append(q4)
        self.questions.append(q5)
        self.questions.append(q6)
        self.questions.append(q7)
        self.questions.append(q8)
        self.questions.append(q9)
