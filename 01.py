class ElfList:
    def __init__(self, first_item):
        self.items = [ first_item ]
        self.total_calories = first_item

    def add_item(self, item):
        self.items.append(item)
        self.total_calories += item
        
    def __repr__(self):
        return self.total_calories

elves = []
elf_with_most_calories = None
current_elf = None

calorie_list = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


for calorie_string in calorie_list.split("\n"):
    if calorie_string == "":
        current_elf = None
    else:
        calorie_value = int(calorie_string)
        if not current_elf:
            current_elf = ElfList(calorie_value)
            elves.append(current_elf)
        else:
            current_elf.add_item(calorie_value)
    if current_elf and (not elf_with_most_calories or current_elf.total_calories > elf_with_most_calories.total_calories):
        elf_with_most_calories = current_elf

elf_cals = [x.total_calories for x in elves]
elf_cals_sorted = list(reversed(sorted(elf_cals)))

print (elf_cals)
print (elf_cals_sorted)
print (elf_cals_sorted[0] + elf_cals_sorted[1] + elf_cals_sorted[2] )
