class Player:
    def __init__(self, start_room_id):
        self._room_id = start_room_id

    @property
    def room_id(self):
        return self._room_id

    @room_id.setter
    def room_id(self, new_room_id):
        self._room_id = new_room_id

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

def test():
    test_player = Player.from_dict({"start_room_id": 1})
    test_player.room_id = 2
    print("Test player.py: ", test_player.room_id)

test()