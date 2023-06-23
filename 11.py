class Monkey:
    def __init__(self, items: list[int], operation: str, operation_amount: int, test_divisor: int, true_destination: int, false_destination: int, number: int = None) -> None:
        self.items = items
        self.operation = operation
        self.operation_amount = operation_amount
        self.test_divisor = test_divisor
        self.true_destination = true_destination
        self.false_destination = false_destination
        self.number = number
        self.inspections = 0

    def take_turn(self, verbose: bool = False) -> None:
        if verbose:
            print("Monkey%s:" % (" #%d" % self.number if self.number else ""))
        for item in self.items:
            self.inspections += 1
            item_value = item
            if verbose:
                print("  Monkey inspects an item with a worry level of %d." % item_value)
            if self.operation == "*":
                item_value *= self.operation_amount
                if verbose:
                    print("    Worry level is multiplied by %d to %d." % (self.operation_amount, item_value))
            else:
                if self.operation == "+":
                    item_value += self.operation_amount
                    if verbose:
                        print("    Worry level increases by %d to %d." % (self.operation_amount, item_value))
                else:
                    item_value *= item_value
                    if verbose:
                        print("    Worry level is multiplied by itself to %d." % (item_value))
            item_value //= 3
            if verbose:
                print("    Monkey gets bored with item. Worry level is divided by 3 to %d." % item_value)
            if item_value % self.test_divisor == 0:
                monkeys[self.true_destination].items.append(item_value)
                if verbose:
                    print("    Current worry level is divisible by %d." % self.test_divisor)
                    print("    Item with worry level %d is thrown to monkey %d." % (item_value, self.true_destination))
            else:
                monkeys[self.false_destination].items.append(item_value)
                if verbose:
                    print("    Current worry level is not divisible by %d." % self.test_divisor)
                    print("    Item with worry level %d is thrown to monkey %d." % (item_value, self.false_destination))
        self.items = []

    def __repr__(self):
        return "Monkey%s([%s], %s%s, %d, %d, %d)" % (" #%d" % self.number if self.number else "",
                                                 ",".join([str(x) for x in self.items]),
                                                 self.operation,
                                                 str(self.operation_amount) if self.operation_amount else "",
                                                 self.true_destination,
                                                 self.false_destination,
                                                 self.inspections)


def parse_monkeys(puzzle_input_text: str) -> list[Monkey]:
    def is_integer(n: str) -> bool:
        try:
            float(n)
        except ValueError:
            return False
        else:
            return float(n).is_integer()

    puzzle_input_tokens = [y.split(" ") for y in [x.strip() for x in puzzle_input_text.split("\n") if not x.strip() == ""]]

    output = []
    for monkey_input_start_line_number in range(0, len(puzzle_input_tokens), 6):
        tokens = puzzle_input_tokens[monkey_input_start_line_number:monkey_input_start_line_number+6]

        assert tokens[0][0] == "Monkey"
        assert int(tokens[0][1][:-1]) == len(output)
        assert len(tokens[0]) == 2

        assert " ".join(tokens[1][0:2]) == "Starting items:"
        assert len(tokens[1]) >= 2
        input_items = [int(x[:-1]) if x[-1] == "," else int(x)  for x in tokens[1][2:]]

        assert " ".join(tokens[2][0:4]) == "Operation: new = old"
        assert tokens[2][4] == "*" or tokens[2][4] == "+"
        assert is_integer(tokens[2][5]) or " ".join(tokens[2][4:6]) == "* old"
        assert len(tokens[2]) == 6
        input_operation = tokens[2][4]
        if " ".join(tokens[2][4:6]) == "* old":
            input_operation_amount = None
            input_operation = "**2"
        else:
            input_operation_amount = int(tokens[2][5])

        assert " ".join(tokens[3][0:3]) == "Test: divisible by"
        assert is_integer(tokens[3][3])
        assert len(tokens[3]) == 4
        input_test_divisor = int(tokens[3][3])

        assert " ".join(tokens[4][0:5]) == "If true: throw to monkey"
        assert is_integer(tokens[4][5])
        assert len(tokens[4]) == 6
        input_true_destination = int(tokens[4][5])

        assert " ".join(tokens[5][0:5]) == "If false: throw to monkey"
        assert is_integer(tokens[5][5])
        assert len(tokens[5]) == 6
        input_false_destination = int(tokens[5][5])

        output.append(Monkey(input_items,
                             input_operation,
                             input_operation_amount,
                             input_test_divisor,
                             input_true_destination,
                             input_false_destination,
                             len(output)))

    return output


monkeys = parse_monkeys("""
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""")

print(monkeys)

for monkey in monkeys:
    monkey.take_turn(True)

print(monkeys)

for i in range(2, 21):
    for monkey in monkeys:
        monkey.take_turn()

    print(monkeys)

inspections = []
for monkey in monkeys:
    inspections.append(monkey.inspections)

sorted_inspections = sorted(inspections)

monkey_business = sorted_inspections[-1] * sorted_inspections[-2]

print("Part 1: level of monkey business = %d" % monkey_business)

