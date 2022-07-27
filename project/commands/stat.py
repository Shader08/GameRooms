from commands.command import Command
from colorama import Fore
class StatsCommand(Command):
    games_stats={}
    def __init__(self,clients):
        self.clients=clients

    def show_help(self):
         print(Fore.GREEN+"""Command format is: stats 
        This command show the list of most plyed 3 games
        """)

    def run(self, args: list):
        if not args:
            games_dictionary={}
            for client in self.clients:
                for game in client.get_games():
                    games_dictionary[game.get_name()]=games_dictionary.get(game.get_name(),0)+1
            marklist = sorted(games_dictionary.items(), key=lambda x:x[1], reverse=True)
            print(marklist[:3])
        elif args[1]=='help':
            self.show_help()
        else:
            print("unknow format of stats command")

            
            