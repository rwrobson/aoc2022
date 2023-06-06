assignment_string = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

assignment_strings = [x.strip() for x in assignment_string.split("\n") if not x.strip() == ""]

class assignment_pair:
    def __init__(self, assignment_string):
        pair_strings = assignment_string.split(",")
        pairs = [ x.split("-") for x in pair_strings ]
        self.a_lower = int(pairs[0][0])
        self.a_upper = int(pairs[0][1])
        self.b_lower = int(pairs[1][0])
        self.b_upper = int(pairs[1][1])
        self.lowers_equal = (self.a_lower == self.b_lower)
        self.uppers_equal = (self.a_upper == self.b_upper)
        self.exactly_equal = self.lowers_equal and self.uppers_equal
        self.a_contains_b = ((self.a_lower <= self.b_lower) and (self.b_upper <= self.a_upper))
        self.b_contains_a = ((self.b_lower <= self.a_lower) and (self.a_upper <= self.b_upper))
        self.contains = self.a_contains_b or self.b_contains_a
        self.a_upper_overlaps_b_lower = (self.a_lower <= self.b_lower) and (self.b_lower <= self.a_upper) and (self.a_upper <= self.b_upper)
        self.b_upper_overlaps_a_lower = (self.b_lower <= self.a_lower) and (self.a_lower <= self.b_upper) and (self.b_upper <= self.a_upper)
        self.overlaps = self.a_upper_overlaps_b_lower or self.b_upper_overlaps_a_lower or self.contains

    def __repr__(self):
        if self.exactly_equal:
            return "Exactly equal"
        if self.contains:
            return "Contains"
        if self.overlaps:
            return "Overlaps"
        return "Distinct"


assert str(assignment_pair("2-4,6-8")) == "Distinct"
assert str(assignment_pair("2-3,4-5")) == "Distinct"
assert str(assignment_pair("5-7,7-9")) == "Overlaps"
assert str(assignment_pair("2-8,3-7")) == "Contains"
assert str(assignment_pair("6-6,4-6")) == "Contains"
assert str(assignment_pair("2-6,4-8")) == "Overlaps"

assert str(assignment_pair("6-8,2-4")) == "Distinct"
assert str(assignment_pair("4-5,2-3")) == "Distinct"
assert str(assignment_pair("7-9,5-7")) == "Overlaps"
assert str(assignment_pair("3-7,2-8")) == "Contains"
assert str(assignment_pair("4-6,6-6")) == "Contains"
assert str(assignment_pair("4-8,2-6")) == "Overlaps"

count_of_contains = 0
count_of_overlaps = 0

for assignment in [assignment_pair(x) for x in assignment_strings]:
    if assignment.contains:
        count_of_contains += 1
    if assignment.overlaps:
        count_of_overlaps += 1

print ("Part 1: One range fully contains the other in %d assignment pairs." % count_of_contains)
print ("Part 2: One range overlaps the other in %d assignment pairs." % count_of_overlaps)