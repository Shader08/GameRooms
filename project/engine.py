
from random import randint
from generator import Generator
from commands.list import ListCommand
from commands.add import AddCommand
from commands.book import BookingCommand
from commands.stat import StatsCommand
from colorama import Fore
from commands.send import SendCommand

class Engine:
    def main(self):
        gen=Generator()
        clients=gen.clients
        rooms=gen.generate_room()
        games=gen.games
        cuurent_client_index=randint(0,len(clients)-1)
        current_client=clients[cuurent_client_index]
        print(current_client)
        while True:
            self.show_menu()
            choice=input("Command: \n")
            args=choice.split(" ")
            match args[0]:
                case 'list':
                    list_com=ListCommand(rooms,games,clients)
                    list_com.run(args)
                case 'book':
                     booking_com=BookingCommand(rooms,current_client,games)
                     booking_com.run(args)
                     rooms=booking_com.rooms
                     clients[cuurent_client_index]=booking_com.client
                case 'add':
                    add_com=AddCommand(games)
                    add_com.run(args)
                    games=add_com.get_games()
                    SendCommand(clients,games[-1]).run([])
                case 'stats':
                    StatsCommand(clients).run([])
                case 'exit':
                    return 0
                case _:
                    print("unknown command")                    
            
    def show_menu(self):
        print(Fore.WHITE+"""  
                    1.List rooms 
                    2.Book room time game 
                    3.List games 
                    4.add new game
                    5.stats
                    6.exit
                """)

Engine().main()