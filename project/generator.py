from project.model.room import Room
from project.model.game import Game
from project.model.client import Client
from random import randint
import copy
class Generator:
    games=[Game(1,"Assasins Creed", "RPG"),Game(2,"Fifa 23","Sports"),Game(3,"Age of Empires IV","Strategy"),
     Game(4,"Total War","Strategy"), Game(5,"Baldur's Gate","RPG")]
    clients=[]
    names=["Ionel","Marcel","John","Costel","Eliza","Maria","Radu","Oana"]
    numbers=["0789123456","0754657494","0789123220","078912383","0760200900"]
    availability={f"{i}-{i+1}":0 for i in range(7,21)}
    def generate_clients(self):
        if self.clients:
                return self.clients
        number_of_clients=randint(5,20)
        for index in range(number_of_clients):
            random_first_index=randint(0,len(self.names)-1)
            random_second_index=randint(0,len(self.names)-1)
            phone_number_index=randint(0,len(self.numbers)-1)
            client=Client(index,f"{self.names[random_first_index]} {self.names[random_second_index]}",self.numbers[phone_number_index],
            self.get_random_list_games()
            )
            self.clients.append(client)

        else:
            print("Clients initialization done......")
        return self.clients


    def generate_room(self):
        rooms_list=[]
        if not self.clients:
            self.generate_clients()
        for index in range(0,3):
            random_limit=randint(1, len(self.clients)-1)
            number_of_clients=randint(0,random_limit)
            room=Room(index,random_limit)
            # for each client need to assign a time
            # room.set_room_clients([
            #     self.clients[randint(0,len(self.clients)-1)]   for _ in range(0,number_of_clients)
            # ])
            copy_availabilty= copy.deepcopy(self.availability)
            clients_list=[]
            for _ in range(0, number_of_clients):
                index=randint(0,len(self.clients)-1)
                client=self.clients[index]
                clients_list.append(client)
                availability_random_position=randint(0,len(self.availability)-1)
                copy_availabilty[list(self.availability.keys())[availability_random_position]]=client.get_id()

            room.set_room_clients(clients_list)
            room.set_availability(copy_availabilty)
            rooms_list.append(room)
        return rooms_list
            




    def get_random_list_games(self):
        games_random_list=[]
        number_of_games=randint(0,len(self.games)-1)
        for index in range(number_of_games):
            games_random_list.append(self.games[index])
        return games_random_list

# gen=Generator()
# gen.generate_clients()
# print(gen.clients)
# print(gen.generate_room())