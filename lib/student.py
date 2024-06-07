#!/usr/bin/env python

from user import User

class Student(User):

    def __init__(self, first_name, last_name):
        
        super().__init__(first_name, last_name)

        self.knowledge = []
    
    def learn(self, student_string):
        pass
        return self.knowledge.append(student_string)


mike = Student("Mike", "Sonko")

print(mike.first_name, mike.last_name)

mike.learn("JavaScript")

print(mike.knowledge)

        