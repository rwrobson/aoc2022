programString = """
noop
addx 3
addx -5"""

programTokens = [y.split(" ") for y in [x.strip() for x in programString.split("\n") if not x.strip() == ""]]

registerXduringCycle = [1]
registerX = 1

for token in programTokens:
    op = token[0]
    assert op == "addx" or op == "noop"
    if op == "noop":
        registerXduringCycle.append(registerX)
    if op == "addx":
        registerXduringCycle.append(registerX)
        registerXduringCycle.append(registerX)
        registerX += int(token[1])

signalStrengthTotal = 0
for cycleNumber in range(20, len(registerXduringCycle), 40):
    signalStrength = cycleNumber * registerXduringCycle[cycleNumber]
    signalStrengthTotal += signalStrength
    print("During the %dth cycle, register X has the value %d, so the signal strength is %d * %d = %d" % (cycleNumber, registerXduringCycle[cycleNumber], cycleNumber, registerXduringCycle[cycleNumber], cycleNumber * registerXduringCycle[cycleNumber]))

print("Part 1: The sum of the signal strengths is %d" % signalStrengthTotal)

line = ""
position = 0
for cycleNumber in range(1, len(registerXduringCycle)):
    x = registerXduringCycle[cycleNumber]
    if position == x - 1 or position == x or position == x + 1:
        line += "#"
    else:
        line += "."
    position += 1
    if cycleNumber % 40 == 0:
        print(line)
        line = ""
        position = 0