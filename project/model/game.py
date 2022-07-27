class Game:
    def __init__(self,id:int,name:str,category:str):
        self._id=id
        self._name=name
        self._category=category

    def get_id(self):
        return self._id
    def get_category(self):
        return self._category
    def get_name(self):
        return self._name
    def __str__(self) -> str:
        return f"{self._id} {self._name} {self._category} \n"
    def __repr__(self) -> str:
        return str(self)
    