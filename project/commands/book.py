from time import gmtime
from commands.command import Command
from colorama import Fore
class BookingCommand(Command):
    def __init__(self, rooms,client,games):
        self.rooms=rooms
        self.client=client
        self.games=games
    def show_help(self):
        print(Fore.GREEN+"""Command format is: book <room_id> <time_interval> <game_id> 
        This command will book a place in a room for playing a game
        """)
    def run(self,args:list):
        if args[1]=='help':
            self.show_help()
        else:
        #to do errors checking  for conversion
            room_number=int(args[1])
            time=args[2]
            game_id=int(args[3])
            found_game=[game for game in self.games if game.get_id()==game_id]
            room_index= next((i for i in range(0,len(self.rooms)-1) if self.rooms[i].get_id()==room_number),None)
            self.rooms[room_index].book_time(self.client.get_id(),time)
            #to do: checking if found_game is not empty throw exception
            self.client.add_game(found_game[0])

        
