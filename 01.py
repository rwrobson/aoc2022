## Calorie counting https://adventofcode.com/2022/day/1

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

new_total = True
elf_calorie_totals = []

for calorie_string in calorie_list.split("\n"):
    if calorie_string == "":
        new_total = True
    else:
        calorie_value = int(calorie_string)
        if new_total:
            elf_calorie_totals.append(calorie_value)
            new_total = False
        else:
            elf_calorie_totals[-1] = elf_calorie_totals[-1] + calorie_value

elf_calorie_totals_sorted = list(reversed(sorted(elf_calorie_totals)))

print ("Answer to part 1: %d" % elf_calorie_totals_sorted[0])

print ("Answer to part 2: %d" % (elf_calorie_totals_sorted[0] + elf_calorie_totals_sorted[1] + elf_calorie_totals_sorted[2]))
