def calculate_team_total_rating(players) -> int:
    total = 0
    for player in players:
        total = total + player.get_rating()
    return total

def elves_concert(elves) -> None:
    for elf in elves:
        elf.play_elf_song()

def feast_of_the_dwarves(dwarves) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
