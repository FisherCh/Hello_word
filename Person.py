#first class
class PERSON(object):
    def __init__(self,name = 'Fisher',Age = 1):
        self.name = name
        self.Age = Age
        self.full = 50
        self.hapiness = 50
        print 'initial complete! Hello, world!'
        
    def eat(self,food):
        if food == 'rice':
            self.full += 5
            self.happiness += 1
        elif food == 'soup':
            self.full += 1
            self.happiness +=2
        print 'full='+self.full
