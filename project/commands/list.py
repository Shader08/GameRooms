from commands.command import Command

from colorama import Fore
class ListCommand(Command):
    def __init__(self,rooms,games,clients):
        self.rooms=rooms
        self.games=games
        self.clients=clients
    def show_help(self):
        print(Fore.GREEN+"""ommand format is: iist rooms || list games 
        This command wil show the list of rooms with their details 
        or the all games available
        """)
    def run(self,args:list):
        #checking errors for parsing args
        if args[1]=='rooms':
            print(self.rooms)
        elif args[1]=='games':
            print(self.games)
        elif args[1]=='clients':
            print(self.clients)
        elif args[1]=='help':
            self.show_help()
        else:
            print('unkown format of list command.\n For help type: list help')