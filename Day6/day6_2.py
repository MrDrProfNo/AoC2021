"""
@author MrNo

Summary:
This is just part 1, except simulate for more days. Only the constant at the top is changed.
"""
MAX_TTS = 8
GENS = 256


def main():

    # don't need to track individual fish, just how many fish are in each bracket.
    fish = [0 for _ in range(MAX_TTS + 1)]

    with open("inputs.txt", "r+") as file:
        for TTS in file.readline().strip().split(","):
            fish[int(TTS)] += 1

    print(f"Initial State: {fish}, total: {sum(fish)}")

    for generation in range(GENS):
        spawning = fish[0]

        for pos_previous, count in enumerate(fish[1:]):
            # indexing fish using index from enumerate, but enumerate started 1 later,
            # so this is the index of the element before count
            fish[pos_previous] = count

        fish[6] += spawning
        fish[8] = spawning

        print(f"Generation {generation + 1}: {fish}, total: {sum(fish)}")

    print(f"After {GENS} generations, there were {sum(fish)} fish")


if __name__ == '__main__':
    main()
