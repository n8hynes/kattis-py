import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main():
    line = sys.stdin.readline()
    gold, silver, copper = [int(x) for x in line.split()]
    buying_power = gold*3 + silver*2 + copper*1

    if buying_power >= 8:
        best_victory = "Province"
    elif buying_power >= 5:
        best_victory = "Duchy"
    elif buying_power >= 2:
        best_victory = "Estate"
    else:
        best_victory = "None"

    if buying_power >= 6:
        best_treasure = "Gold"
    elif buying_power >= 3:
        best_treasure = "Silver"
    else:
        best_treasure = "Copper"

    if best_victory == "None":
        print(best_treasure)
    else:
        print(f"{best_victory} or {best_treasure}")

main()
