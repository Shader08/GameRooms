class Room:
    def __init__(self,id:int,limit:int):
        self.id=id
        self.limit=limit
        self.room_clients=[]
        self.availability={}
 
        
    def book_time(self,client_id:int ,key:str):
        #to do throw exception in case o fail
        if self.availability[key]==0:
            self.availability[key]=client_id
            print("booking was succesfully done :)")
        else:
            print("Time is not available")
            
    def set_room_clients(self,clients_list:list):
        self.room_clients=clients_list
    def set_availability(self, available:dict):
        self.availability=available
    def get_availability(self):
        return self.availability
    def get_id(self):
        return self.id
    
    def __str__(self):
        return f"""Room:{ self.id} \n Load: {len(self.room_clients)}/{self.limit} \n 
        {sorted(self.availability.items(), key=lambda x: (x[1], int(x[0].split('-')[0])))} \n"""
    def __repr__(self) -> str:
        return str(self)


    

      