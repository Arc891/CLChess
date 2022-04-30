from abc import ABC, abstractmethod, abstractproperty

class Color(ABC):
    @property
    @abstractmethod
    def code(self):
        pass

class White(Color):
    code = "\x1b[1;37m"

class Black(Color):
    code = "\x1b[1;30m"

class NoColor(Color):
    code = "\x1b[33m"