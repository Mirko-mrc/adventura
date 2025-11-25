from adventura.player import Player
from adventura.room import Room

class Hra:
    def __init__(self, player, rooms):
        self._player = player
        self._rooms = rooms

    @property
    def player(self):
        return self._player

    @classmethod
    def from_dict(cls, data):
        player = Player.from_dict(data['player'])
        rooms = {room["room_id"]: Room.from_dict(room) for room in data['rooms']}
        return cls(player, rooms)

    def active_room(self):
        return self._rooms.get(self._player.room_id)

    def game_over(self):
        room = self.active_room()
        return room.game_over if room else None

def test():
    test_hra = Hra.from_dict({"player": {"start_room_id": "1"},
                            "rooms": [{"room_id": "1",
                                        "label": "Čistinka",
                                        "desc": "Stojíš na kraji čistinky",
                                        "exits": [{
                                            "label": "zapad",
                                            "room_id": "2"
                                        }, {
                                            "label": "vychod",
                                            "room_id": "3"}]}]})
    print(test_hra.player.room_id)
    print(test_hra.active_room().label)

test()