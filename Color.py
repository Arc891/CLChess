from abc import ABC, abstractmethod, abstractproperty

class Color(ABC):
    @property
    @abstractmethod
    def code(self) -> str:
        pass

    @property
    @abstractmethod
    def selected(self) -> str:
        pass

class White(Color):
    code = "\x1b[1;37m"
    selected = "\x1b[1;4;37;45m"

class Black(Color):
    code = "\x1b[1;30m"
    selected = "\x1b[1;4;30;45m"

class NoColor(Color):
    code = "\x1b[33m"
    selected = "\x1b[4;37;42m"