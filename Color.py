from abc import ABC, abstractmethod

class Color(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def code(self) -> str:
        pass

    @property
    @abstractmethod
    def selected(self) -> str:
        pass

    def __str__(self):
        return self.name

class White(Color):
    name = "White"
    code = "\x1b[1;37m"
    selected = "\x1b[1;4;37;45m"

class Black(Color):
    name = "Black"
    code = "\x1b[1;30m"
    selected = "\x1b[1;4;30;45m"

class NoColor(Color):
    name = "Empty"
    code = "\x1b[33m"
    selected = "\x1b[4;37;42m"