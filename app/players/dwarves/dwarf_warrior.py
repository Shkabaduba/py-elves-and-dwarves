from .dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self, nickname: str, favourite_dish: str, hummer_level:int):
        self._hummer_level = hummer_level
        super().__init__(nickname, favourite_dish )

    def player_info(self):
        return f"Dwarf warrior {self.nickname}. {self.nickname} has a hummer of the {self._hummer_level} level"

    def get_rating(self):
        return self._hummer_level + 4

    def declared(self):
        pass