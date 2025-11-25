# adventura/engine.py

import json
import textwrap
from adventura.hra import Hra


class Engine:
    def __init__(self, hra, intro, outro):
        self._hra = hra
        self._intro = intro
        self._outro = outro

    # -------------------------------------------------------
    # TOVÁRENSKÉ METÓDY
    # -------------------------------------------------------

    @classmethod
    def from_dict(cls, data):
        hra = Hra.from_dict(data)
        return cls(hra, data['intro'], data['outro'])

    @classmethod
    def load_game(cls, json_path):
        with open(json_path, encoding='utf-8') as json_file:
            data = json.load(json_file)
            return Engine.from_dict(data)

    # -------------------------------------------------------
    # HERNÁ LOGIKA
    # -------------------------------------------------------

    def intro(self):
        print(self._intro)
        input()

    def game_over(self, msg):
        print()
        print("!!!!!!!!!!!! GAME OVER !!!!!!!!!!!!")
        print(msg)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(self._outro)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")

    def describe(self):
        room = self._hra.active_room()
        print("-" * 74)
        print(f"Nachádzaš sa: {room.label}")
        print("-" * 74)
        # zalomený popis
        print(textwrap.fill(room.desc, width=70))
        print()
        print(f"Môžeš ísť: {', '.join(room.exits)}")
        print("-" * 74)

    def action(self):
        try:
            commands = input("Čo chceš urobiť?: ").split()
            if not commands:
                return  # prázdny vstup, ignorujeme

            # rozdelenie na verb a noun
            verb = commands[0]
            noun = commands[1] if len(commands) > 1 else None

            # HELP
            if verb == "help":
                print()
                print("!!!!!!!!!!!! HELP !!!!!!!!!!!!!!!!!!!!")
                print("Pre ukončenie hry napíš exit")
                print("Z miestnosti sa vieš presunúť príkazom go a smer, napríklad go vychod.")
                print("Alebo stačí napísať len smer, napríklad vychod.")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

            # EXIT
            elif verb == "exit":
                return True

            # GO <smer>
            elif verb == "go" and noun:
                room = self._hra.active_room()
                exit_info = room.exit(noun)
                if exit_info:
                    self._hra.player.room_id = exit_info['room_id']
                else:
                    print(f"Nie je možné ísť smerom '{noun}'!")

            # priamo <smer>
            else:
                room = self._hra.active_room()
                exit_info = room.exit(verb)
                if exit_info:
                    self._hra.player.room_id = exit_info['room_id']
                else:
                    print(f"Nie je možné ísť smerom '{verb}'!")

        except KeyboardInterrupt:
            return True

        except Exception:
            print()
            print("!!!!!!!!!!!! CHYBA !!!!!!!!!!!!!!!!!!!!")
            print("Nerozumiem príkazu. Ak si nevieš dať rady, napíš help")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    def play(self):
        self.intro()
        while True:
            self.describe()

            game_over_msg = self._hra.game_over()
            if game_over_msg:
                self.game_over(game_over_msg)
                break

            should_quit = self.action()
            if should_quit:
                self.game_over("Vzdal si to skôr ako si stihol nájsť poklad!")
                break
