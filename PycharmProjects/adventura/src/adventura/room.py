class Room:
    def __init__(self, room_id, label, desc, exits=None, game_over=None):
        self._room_id = room_id
        self._label = label
        self._desc = desc
        self._game_over = game_over
        if exits is None:
            exits = []

        self._exits = {exit["label"]: exit for exit in exits}


    @property
    def game_over(self):
        return self._game_over

    @property
    def desc(self):
        return self._desc

    @property
    def label(self):
        return self._label

    @property
    def exits(self):
        return list(self._exits.keys())

    def exit(self, direction):
        return self._exits.get(direction)

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

def test():
    test_room = Room.from_dict({"room_id": "1",
                                "label": "Čistinka",
                                "desc": "Stojíš na kraji čistinky",
                                "exits": [{
                                    "label": "zapad",
                                    "room_id": "2"
                                }, {
                                    "label": "vychod",
                                    "room_id": "3"}]})
    print(test_room.label, test_room.desc, test_room.game_over)
    print(test_room.exits)
    print(test_room.exit("zapad"))

test()
