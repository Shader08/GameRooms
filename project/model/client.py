from model.game import Game

class Client:
    def __init__(self,id:int,name:str, phone_number:str, games:list): 
        self.id=id
        self.name=name
        self.phone_number=phone_number
        self.games=games
    
    def add_game(self, game:Game):
        self.games.append(game)
        
    def get_categories(self):
        return [game.category for game in self.games]

    def get_name(self):
        return self.name
    def set_games(self,games:list):
        self.games=games
    def get_games(self):
        return self.games
    def get_id(self):
        return self.id
    def __str__(self):
        return f"{self.id} {self.name} {self.phone_number} \n Games: {self.games}\n"
    def __repr__(self) -> str:
        return str(self)



