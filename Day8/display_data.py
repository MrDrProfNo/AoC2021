class DisplaySet:

    def __init__(self, input):
        part1, part2 = input.split(" | ")
        self.unique_signal_patterns = [Digit(segments) for segments in part1.split(" ")]
        self.output_values = [Digit(segments) for segments in part2.split(" ")]
        self.known_patterns: list[Digit] = [None for _ in range(10)]
        self.__get_patterns()

        # self.as_int = sum(self.known_patterns.index(output) * (10 ** (len(self.output_values) - pos)) for pos, output in enumerate(self.unique_signal_patterns))
        self.as_int = 0
        for pos, output in enumerate(self.output_values):
            self.as_int += self.known_patterns.index(output) * (10 ** (len(self.output_values) - pos - 1))

    def __get_patterns(self):
        for pattern in self.unique_signal_patterns:
            if len(pattern) == 2:
                self.known_patterns[1] = pattern
            elif len(pattern) == 4:
                self.known_patterns[4] = pattern
            elif len(pattern) == 3:
                self.known_patterns[7] = pattern
            elif len(pattern) == 7:
                self.known_patterns[8] = pattern

        # the guaranteed ones have been found; I can do comparisons with
        # the others now
        for pattern in self.unique_signal_patterns:
            if len(pattern) == 5:
                # 3 and 5 overlap in 3 places, 2 overlaps in 2
                if len(pattern.segments & self.known_patterns[4].segments) == 3:
                    # only 3 overlaps in 2 places
                    if len(pattern.segments & self.known_patterns[1].segments) == 2:
                        self.known_patterns[3] = pattern
                    else:
                        self.known_patterns[5] = pattern
                else:
                    self.known_patterns[2] = pattern
            elif len(pattern) == 6:
                # 0 and 9 overlap with 1 in 2 places, 6 overlaps in 1
                if len(pattern.segments & self.known_patterns[1].segments) == 2:
                    # 0 overlaps with 4 in 3 places, 9 overlaps in 4
                    if len(pattern.segments & self.known_patterns[4].segments) == 3:
                        self.known_patterns[0] = pattern
                    else:
                        self.known_patterns[9] = pattern
                else:
                    self.known_patterns[6] = pattern

    def __int__(self):
        return self.as_int


class Digit:
    def __init__(self, segments):
        self.segments = {segment for segment in segments}

    def __repr__(self):
        return ",".join(self.segments)

    def __len__(self):
        return len(self.segments)

    def __eq__(self, other):
        return other.segments == self.segments if isinstance(other, Digit) else False
