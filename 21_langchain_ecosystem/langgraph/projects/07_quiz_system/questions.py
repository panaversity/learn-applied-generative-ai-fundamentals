from abc import ABC, abstractmethod
from user import User

class QuestionBank:
    def __init__(self, questionBankID:str, user: User, subpath: str, questionBankTitle:str) -> None:
        self.questionBankID:str = questionBankID
        self.user: User = user
        self.subpath: str = subpath
        self.questionBankTitle : str = questionBankTitle
        self.topics: list[Topic]= []


class Topic:
    def __init__(self, questionBankID: str, topicID:str, title: str, desc: str) -> None:
        self.questionBankID: str = questionBankID
        self.topicID: str = topicID
        self.title: str = title
        self.desc : str = desc
        self.subtopics : list[Topic] = []
        self.questions : list[Question] = []


class Question(ABC):
    def __init__(self, questionBankID: str, topicID: str, questionID:str, title:str, text: str, points: int = 1) -> None:
        self.questionBankID: str = questionBankID
        self.topicID: str = topicID
        self.questionID: str = questionID
        self.title: str = title
        self.text: str = text
        self.points: int = points

    def getPoints(self)-> int:
        return self.points

    def getQuestionCount(self)-> int:
        return 1

class Option:
    def __init__(self, questionBankID: str, questionID: str, optionID: str, text: str, correct:bool) -> None:
        self.questionBankID = questionBankID
        self.questionID = questionID
        self.optionID = optionID
        self.text = text
        self.correct: bool = correct

class MCQ(Question):
    def __init__(self, questionBankID: str, topicID: str, questionID: str, title:str, text: str) -> None:
        super().__init__(questionBankID, topicID, questionID, title, text)
        self.options: list[Option]= []

    def getOptions(self)-> list[Option]:
        return self.options
    
class SingleSelectMCQ(MCQ):
    def __init__(self, questionBankID: str, topicID: str, questionID:str, title:str, text: str) -> None:
        super().__init__(questionBankID, topicID, questionID, title, text)

class MultipleSelectMCQ(MCQ):
    def __init__(self, questionBankID: str, topicID: str, questionID: str, title:str, text: str) -> None:
        super().__init__(questionBankID, topicID, questionID, title, text)

class CaseStudy(Question):
    def __init__(self, questionBankID: str, topicID: str, questionID: str, title:str, text: str) -> None:
        super().__init__(questionBankID, topicID, questionID, title, text)
        self.text: str = text
        self.mcqs: list[Question]= []

    def getQuestions(self)-> list[Question]:
        return self.mcqs

    def getPoints(self)-> int:
        points: int = 0
        for q in self.mcqs:
            points += q.getPoints()
        return points
    
    def getQuestionCount(self)-> int:
        return len(self.mcqs)

class FreeTextQuestion(Question):
    def __init__(self, questionBankID: str, topicID: str, questionID: str, title:str, text: str, points: int, correctAnswer: str) -> None:
        super().__init__(questionBankID, topicID, questionID, title, text, points)
        self.correctAnswer = correctAnswer
    
    
        