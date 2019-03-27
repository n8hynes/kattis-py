import sys

class Pokestop:
    def __init__(self, position, pokemon):
        self.position = position
        self.pokemon = pokemon
    
    def distance_from(self, position):
        dist = 0
        dist += abs(self.position[0] - position[0])
        dist += abs(self.position[1] - position[1])
        return dist

    def __str__(self):
        return str(self.position) + ': ' + self.pokemon

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main():
    num_stops = int(input())
    current = (0, 0)
    stops = []
    unique_pokemon = []
    for i in range(num_stops):
        line = input().split()
        position = (int(line[0]), int(line[1]))
        pokemon = line[2]
        if pokemon not in unique_pokemon: unique_pokemon.append(pokemon)
        stops.append(Pokestop(position, pokemon))

    steps_travelled = 0
    found_pokemon = []
    for _ in range(len(unique_pokemon)):
        stops = sorted(stops, key=lambda stop: stop.distance_from(current))
        for stop in stops:
            if stop.pokemon not in found_pokemon:
                found_pokemon.append(stop.pokemon)
                distance = stop.distance_from(current)
                eprint(f'Moving from {current} to {stop.position}: {distance}')
                steps_travelled += distance
                current = stop.position
                eprint(f'Found: {stop.pokemon}')
                break
    # Go back to origin:
    steps_travelled += abs(current[0]) + abs(current[1])
    print(steps_travelled)


"""


    for pokemon in unique_pokemon:
        next_step = find_closest(stops, pokemon, current)
        eprint(f'Going to {next_step[1]} to find {pokemon}')
        steps_travelled += next_step[0]
        current[0] = next_step[1][0][0]
        current[1] = next_step[1][0][1]
    print(steps_travelled)
"""

main()
