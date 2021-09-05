# class ParserInterface:
#     def load(self, path, filename):
#         pass
#     def extract_text(self, name):
#         pass

# class PdfParser(ParserInterface):
#     def load(self, path, filename):
#         print("pdf load")
#     def extract_text(self, name):
#         print("pdf extract")

# class EmailParser(ParserInterface):
#     def load(self, path, filename):
#         print("email load")
#     def extract_text(self, name):
#         print("email extract")

# parsers = [PdfParser(), EmailParser()]
# for item in parsers:
#     item.extract_text("text")
##############################
# import abc


# class ParserInterface(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def load(self, path, filename):
#         raise NotImplementedError

#     @abc.abstractmethod
#     def extract_text(self, name):
#         raise NotImplementedError


# class PdfParser(ParserInterface):
#     def load(self, path, filename):
#         print("pdf load")

#     def extract_text(self, name):
#         print("pdf extract")


# class EmailParser(ParserInterface):
#     def load(self, path, filename):
#         print("email load")

#     def extract_text(self, name):
#         print("email extract")


# parsers = [PdfParser(), EmailParser()]
# for item in parsers:
#     item.extract_text("text")
#####################################################
# class Person:
#     def __init__(self, name, last, number):
#         self.name = name
#         self.last = last
#         self.number = number


# class Student(Person):
#     UNDERGRADUATE, POSTGRADUATE = range(2)

#     def __init__(self, student_type, *args, **kwargs):
#         self.student_type = student_type
#         self.classes = []
#         super().__init__(*args, **kwargs)

#     def enrol(self, course):
#         self.classes.append(course)


# class Staff(Person):
#     PERMANENT, TEMPRORY =  range(2)
#     def __init__(self, employment_type, *args, **kwargs):
#         self.student_type = employment_type
#         self.classes = []
#         super().__init__(*args, **kwargs)


# class Lecturer(Staff):
#     def __init__(self, employment_type, *args, **kwargs):
#         self.courses_taught = []
#         super().__init__(*args, **kwargs)

#     def add_course(self, course):
#         self.courses_taught.append(course)
###################################################
# class Person:
#     def __init__(self, name, last, number):
#         self.name = name
#         self.last = last
#         self.number = number


# class LearningMixin:

#     def __init__(self):
#         self.classes = []

#     def enrol(self, course):
#         self.classes.append(course)

# class TeacherMixin:
#     def __init__(self):
#         self.courses_taught = []

#     def add_course(self, course):
#         self.courses_taught.append(course)

# class PhdStudent(Person,LearningMixin, TeacherMixin ):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

# print(PhdStudent.__mro__)
########################################
# SOLID

# S
# import json
# class News:
#     def __init__(self, title, info):
#         self.title = title
#         self.info = info
#     def update(self, info):
#         self.info = info
#     def to_HTML(self):
#         return f"""
#                 <div>
#                     <h1>{self.title}</h1>
#                     <p>{self.info}</p>
#                 </div>
#                 """
#     def to_json(self):
#         return json.dumps(self.__dict__, indent=4)

# news = News(title = "Olympic Games", info="USA won hte games")

# print(news.to_HTML())
# print(news.to_json())
###########################################
# import json


# class News:
#     def __init__(self, title, info):
#         self.title = title
#         self.info = info

#     def update(self, info):
#         self.info = info


# class Printer:
#     def __init__(self, news):
#         self.news = news

#     def to_HTML(self):
#         return f"""
#                 <div>
#                     <h1>{self.news.title}</h1>
#                     <p>{self.news.info}</p>
#                 </div>
#                 """

#     def to_json(self):
#         return json.dumps(self.news.__dict__, indent=4)


# news = News(title="Olympic Games", info="USA won hte games")
# printer = Printer(news)
# print(printer.to_json())
# print(printer.to_HTML())
#####################################################
# O
# import math
# from functools import reduce


# class Square:
#     def __init__(self, size):
#         self.size = size
#         self.type = "Square"


# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h


# class Circle:
#     def __init__(self, r):
#         self.r = r
#         self.type = "Circle"


# class AreaCalc:
#     def __init__(self, figures):
#         self.figures = figures

#     @staticmethod
#     def __inner_sum(acc, figure):
#         if figure.type == "Square":
#             t = acc + figure.size ** 2
#         elif figure.type == "Circle":
#             t = acc + math.pi * figure.r ** 2
#         return t

#     def sum_of_areas(self):
#         return reduce(AreaCalc.__inner_sum, self.figures, 0)


# calc = AreaCalc([Circle(3), Circle(4), Square(5)])

# print(calc.sum_of_areas())
#########################
# import math
# from functools import reduce
# import abc


# class Figure(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def area(self):
#         raise NotImplementedError()


# class Square(Figure):
#     def __init__(self, size):
#         self.size = size
#     def area(self):
#         return self.size**2

# class Rectangle(Figure):
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#     def area(self):
#         return self.w*self.h

# class Circle(Figure):
#     def __init__(self, r):
#         self.r = r
#     def area(self):
#         return math.pi*self.r**2

# class AreaCalc:
#     def __init__(self, figures):
#         self.figures = figures

#     def sum_of_areas(self):
#         return reduce(lambda acc, fig: acc + fig.area(), self.figures, 0)


# calc = AreaCalc([Circle(3), Circle(4), Square(5)], Rectangle(5,6))

# print(calc.sum_of_areas())
#####################################################
#I
# class PlaySongs:
#     def __init__(self, title):
#         self.title = title
#     def play_guitar(self):
#         print("guitar")
#     def play_drums(self):
#         print("drums")
#     def play_lyrics(self):
#         print("lyrics")
        
# class PlayRockSongs(PlaySongs):
#         def play_guitar(self):
#             print("guitar solo")

# class PlayInstrumnetalSongs(PlaySongs):
#         def play_lyrics(self):
#             raise Exception("No lyrics")
#############################

# class PlaySongsLyrics():
#     def play_lyrics(self):
#         print("lyrics")
        
        
# class PlaySongsMusic():      
#     def play_guitar(self):
#         print("guitar")
#     def play_drums(self):
#         print("drums")
        
        
# class PlayRockSongs(PlaySongsLyrics, PlaySongsMusic):
#     def play_guitar(self):
#         print("guitar solo")

# class PlayInstrumnetalSongs(PlaySongsMusic):
#     pass
########################################
#DRY
#KISS
########################################
print(3)
