rucksack_contents = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

def split_in_half(full_string):
    halfway = len(full_string) // 2
    return [ full_string[0:halfway], full_string[-halfway:]]

assert(split_in_half("") == ["", ""])
assert(split_in_half("ab") == [ "a", "b" ])
assert(split_in_half("abb") == [ "a", "b" ])
assert(split_in_half("aaaabb") == [ "aaa", "abb" ])

def eliminate_repeats(full_string):
    output = ""
    last = ""
    for char in full_string:
        if not last==char:
            output = output + char
        last = char
    return output

assert(eliminate_repeats("") == "")
assert(eliminate_repeats("abc") == "abc")
assert(eliminate_repeats("abbccca") == "abca")

def get_intersection(string1, string2):
    string1_chars = eliminate_repeats("".join(sorted(string1)))
    string2_chars = eliminate_repeats("".join(sorted(string2)))
    pos1 = 0
    pos2 = 0
    output = ""
    while pos1 < len(string1_chars) and pos2 < len(string2_chars):
        char1 = string1_chars[pos1]
        char2 = string2_chars[pos2]
        if char1 == char2:
            output = output + char1
        if char1 <= char2:
            pos1 = pos1 + 1
        if char1 >= char2:
            pos2 = pos2 + 1
    return output

assert (get_intersection("", "") == "")
assert (get_intersection("abc", "def") == "")
assert (get_intersection("abcd", "bdef") == "bd")
assert (get_intersection("hello", "world") == "lo")

def get_priority(char):
    ORD_SMALL_A = ord("a")
    ORD_CAP_A = ord("A")
    code = ord(char)
    if code >= ORD_SMALL_A:
        return code - ORD_SMALL_A + 1
    else:
        return code - ORD_CAP_A + 27

assert (get_priority("a") == 1)
assert (get_priority("b") == 2)
assert (get_priority("z") == 26)
assert (get_priority("A") == 27)
assert (get_priority("Z") == 52)

total_priority = 0

elf_inventories = []

for rucksack_content in rucksack_contents.split("\n"):
    rucksack_content_clean = rucksack_content.strip()
    if not rucksack_content_clean == "":
        elf_inventories.append(rucksack_content_clean)
        halves = split_in_half(rucksack_content_clean)
        intersection = get_intersection(halves[0], halves[1])
        total_priority = total_priority + get_priority(intersection[0])
    
print ("Sum of priorities in part 1: %d" % total_priority)

total_priority = 0

for line in range(0, len(elf_inventories), 3):
    group_inventory = [ elf_inventories[line],
                        elf_inventories[line+1],
                        elf_inventories[line+2] ]
    intersection = get_intersection(group_inventory[0], group_inventory[1])
    intersection2 = get_intersection(intersection, group_inventory[2])
    total_priority = total_priority + get_priority(intersection2[0])

print ("Sum of priorities in part 2: %d" % total_priority)
