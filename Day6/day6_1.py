"""
@author MrNo

Summary:
It's... an exponential growth problem, with a bit of a twist so you can't just use a
standard exponential growth formula but instead have to store state.

Each fish has an "time to spawn," each "generation" decrement TTS, if 0 before decrementing reset to 6
and spawn new one at 8
"""
MAX_TTS = 8
GENS = 80


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

    print(f"{sum(fish)}")


if __name__ == '__main__':
    main()
