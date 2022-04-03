from abc import ABC, abstractproperty, abstractmethod 

class GrafAbstrakcyjny(ABC):

    @abstractproperty
    def stany(self):
        pass
    
    @abstractmethod
    def step(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def czykoncowy(self):
        pass

class TuringMachine(GrafAbstrakcyjny):

    def __init__(self, data, text, state=0):
        self.state = str(state)
        self.dict = {}
        self.tape = ''.join(['_']*100)
        self.head = 100 // 2
        self.tape = self.tape[:self.head] + text + self.tape[self.head:]
        for line in data.splitlines():
            a, b, c, d, e = line.split(' ')
            self.dict[a,b] = (c, d, e)

    @property
    def stany(self):
        return self.state
    
    def step(self):
        if self.czykoncowy(self.state):
            a = self.tape[self.head]
            action = self.dict.get((self.state, a))
            if action:
                c, d, e = action
                self.tape = self.tape[:self.head] + c + self.tape[self.head+1:]
                if d != '*':
                    self.head = self.head + (1 if d == 'r' else -1)
                self.state = e

    def run(self):
        i = 0
        while self.czykoncowy(self.state):
           self.step()
           i += 1
        print(self.tape.replace('_', ''))

    def czykoncowy(self, stan):
        if stan != 'H':
            return True
        else: 
            return False
            
text = 'aba'
if len(text)!=text.count("a")+text.count("b"):
    raise Exception('wpisano znaki z poza alfabetu {a,b}')
data = open ("C:\\Users\\Jakub\\Desktop\\python\\mt.txt").read()

TuringMachine(data, text).run()