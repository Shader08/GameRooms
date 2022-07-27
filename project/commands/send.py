from setuptools import Command


from commands.command import Command
from model.game import Game
class SendCommand(Command):
    def __init__(self,clients:list,game:Game):
        self.clients=clients
        self.game=game
    def show_help(self):
        return super().show_help()
    def run(self, args: list):
        for client in self.clients:
            if self.game.get_category() in client.get_categories():
                print(f'send notification with new {self.game.get_name()} to {client.get_name()}')