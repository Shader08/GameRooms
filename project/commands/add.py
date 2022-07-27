from random import randint
from commands.command import Command
from colorama import Fore
from model.game import Game
class AddCommand(Command):
    def __init__(self,games):
        self.games=games
    def show_help(self):
          print(Fore.GREEN+"""Command format is: add game_name game_category
        This command will add new game in all games list
        """)
    def run(self, args: list):

        match args[1]:
            case 'help':
                self.show_help()    
            case _:
                #if length args==3 : 
                #checking type of args[1] & args[2] to be strings else print("unkonew format")
                self.games.append(Game(randint(100,10000),args[1],args[2]))
    def get_games(self):
        return self.games