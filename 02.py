## Rock Paper Scissors https://adventofcode.com/2022/day/2

strategy_guide = """
A Y
B X
C Z
"""

ROUND_SCORES_ROUND1 = {
    "AX": 3 + 1,  # they rock,     you rock     => tie (3)  plus 1 for rock
    "AY": 6 + 2,  # they rock,     you paper    => win (6)  plus 2 for paper
    "AZ": 0 + 3,  # they rock,     you scissors => lose (0) plus 3 for scissors
    "BX": 0 + 1,  # they paper,    you rock     => lose (0) plus 1 for rock
    "BY": 3 + 2,  # they paper,    you paper    => tie (3)  plus 2 for paper
    "BZ": 6 + 3,  # they paper,    you scissors => win (6)  plus 3 for scissors
    "CX": 6 + 1,  # they scissors, you rock     => win (6)  plus 1 for rock
    "CY": 0 + 2,  # they scissors, you paper    => lose (0) plus 2 for paper
    "CZ": 3 + 3   # they scissors, you scissors => tie (3)  plus 3 for scissors
}

ROUND_SCORES_ROUND2 = {
    "AX": 0 + 3,  # they rock,     you need to lose, so you play scissors  => lose (0) plus 3 for scissors
    "AY": 3 + 1,  # they rock,     you need to draw, so you play rock      => tie (3)  plus 1 for rock
    "AZ": 6 + 2,  # they rock,     you need to win,  so you play paper     => win (6)  plus 2 for paper
    "BX": 0 + 1,  # they paper,    you need to lose, so you play rock      => lose (0) plus 1 for rock
    "BY": 3 + 2,  # they paper,    you need to draw, so you play paper     => tie (3)  plus 2 for paper
    "BZ": 6 + 3,  # they paper,    you need to win,  so you play scissors  => win (6)  plus 3 for scissors
    "CX": 0 + 2,  # they scissors, you need to lose, so you play paper     => lose (0) plus 2 for paper
    "CY": 3 + 3,  # they scissors, you need to draw, so you play scissors  => tie (3)  plus 3 for scissors
    "CZ": 6 + 1   # they scissors, you need to win,  so you play rock      => win (6)  plus 1 for rock
}

total_score_round1 = 0
total_score_round2 = 0

for round_string in strategy_guide.split("\n"):
    round_score = 0
    if not round_string.strip() == "":
        round_plays = round_string.strip().split(" ")
        if len(round_plays) == 2:
            total_score_round1 = total_score_round1 + ROUND_SCORES_ROUND1["".join(round_plays)]
            total_score_round2 = total_score_round2 + ROUND_SCORES_ROUND2["".join(round_plays)]

print("Total score (round 1 rules): %d" % total_score_round1)
print("Total score (round 2 rules): %d" % total_score_round2)