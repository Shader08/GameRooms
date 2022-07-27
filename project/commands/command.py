from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def show_help(self):
        pass
    @abstractmethod
    def run(self,args:list):
        pass
