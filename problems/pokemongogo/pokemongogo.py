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
        return "'" + str(self.position) + ': ' + self.pokemon + "'"

    __repr__ = __str__

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main():
    # Get input:
    num_stops = int(input())
    stops = []
    unique_pokemon = []
    pokemon_stop_list = []
    for i in range(num_stops):
        line = input().split()
        position = (int(line[0]), int(line[1]))
        pokemon = line[2]
        stop = Pokestop(position, pokemon)
        if pokemon not in unique_pokemon:
            pokemon_stop_list.append((pokemon, [stop]))
            unique_pokemon.append(pokemon)
        else:
            pokemon_stop_list[unique_pokemon.index(pokemon)][1].append(stop)
        stops.append(stop)
    eprint(f'Unique Pokemon: {unique_pokemon}')
    eprint(f'Pokemon stop list: {pokemon_stop_list}')

    # Get each combination of pokestops:
    num_pokemon = len(unique_pokemon)
    eprint(f"Num pokemon: {num_pokemon}")
    last_entry = None
    combinations = []
    while True:
        if last_entry == None:
            last_entry = [0 for _ in range(num_pokemon)]
            combinations.append(last_entry.copy())
            continue
        done = False
        for pokemon in unique_pokemon:
            index = unique_pokemon.index(pokemon)
            if len(pokemon_stop_list[index][1]) > last_entry[index] + 1:
                last_entry[index] += 1
                combinations.append(last_entry.copy())
                break
            elif index == num_pokemon - 1:
                done = True
                break
        if done:
            break
    eprint(f'Combinations: {combinations}')

    min_steps = float('inf')
    for combo in combinations:
        current = (0, 0)
        stop_list = []
        index = 0
        for x in combo:
            stop_list.append(pokemon_stop_list[index][1][x])
            index += 1
        eprint(f"Stop list for {combo}: {stop_list}")
        steps = 0
        while stop_list != []:
            stop_list = sorted(stop_list, key=lambda stop: stop.distance_from(current))
            stop = stop_list.pop(0)
            dist = stop.distance_from(current)
            eprint(f'Moving from {current} to {stop.position}: {dist}')
            steps += dist
            current = stop.position
        steps += abs(current[0]) + abs(current[1])
        eprint(f"Total steps for {combo}: {steps}")
        if steps < min_steps:
            min_steps = steps
    eprint(f"Minimum steps: {min_steps}")
    print(min_steps)


"""
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
