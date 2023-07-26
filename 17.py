shapes = [
            ["####"],
            [".#.",
             "###",
             ".#."],
            ["..#",
             "..#",
             "###"],
            ["#",
             "#",
             "#"],
            ["#",
             "##",
             "##"]
        ]

test_jet_pattern = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

real_jet_pattern = "><<<<><<>><<>><><<<>>><<<<>>>><<>>><>>><<<>><<<><<<><><><>>>><<>>><<<<>>><>><<<<>><><<<<>>><<<>>>" \
                   "<<>><<<>>><>>>><<<<>>>><<<<><>><<<>>><<<<>><<<<>>>><<<<>>><<>>><<<>>><>>><<<<>>><<<<>>>><>>>><<>>" \
                   "><<><<<>>>><><<<<>>>><>><<>><<<><<<<>><<><<<<>>><>><<><<<>>><<<>>><<><<<<>><>><<<><<<>>>><>>>><<<" \
                   ">><<<<>>>><<<>>>><><<<<>>>><<<<>>>><<<<><<<>>>><><<<>>><<<><<><<<>>><<<><<>>>><<<>>>><<<>>><<><>>" \
                   "><<><>>>><><><<>>><<<>><<<>><><>>><<<>>><<<<><>><>>>><<><<<>>>><<><<<<>>><><<>>>><<<<>>>><<><<<<>" \
                   "><<><><>>>><<>><<>><<<<><>>><><<<>><<<>><><>>>><<<>><<<<>>><<><>>>><>>>><<<>>><<<<>>><><<<<>>><>>" \
                   ">><>>><<>>>><<>><<>>><<>><><>><<<<>>><<><<>><<<<><<<>>>><>>><>>><<<>>><<<>>>><<>>><<<<>><<>>>><><" \
                   "<<><>><<<><<<<>>><><<<><<<<>><>><<<<><<<>><>>><<<<>>>><<>>>><<<<>>><><<<>>><<<<><>><<<>><<<<><>>>" \
                   "<>>>><<>>><<<>>>><<>>><><<<><<<<><<><>>>><><>>>><<>>><<<<>><<<<><<>>><<><<<><<<<>>><><<<>>>><>>>>" \
                   "<<<><<<>><<><<<>>>><<<<>><><<<<>>>><<>>>><<>><<>><<<>><<<<>><>>><<<<>>>><><<>>><<>>><>>><<<<>>><<" \
                   "<<>>><<>><>><<<>><<<>>>><<<>>>><<>><<<><><>>><<<<>><<>>>><<><><<<><>>>><<<>><<<>>>><<<<><<>>><<>>" \
                   ">><<><<<<>><<>>><<<<>><>>><<>>>><<<<><><>>><<<<>>>><>>>><<>>>><<<<><<>><<<><<<>><<<>>>><<<><<<<>>" \
                   "<<<<>><<<<>>>><<<>>>><>><<<>>>><<<>>><<><><<<>><<<>><>>><>><><<<<>><<<<>>>><<<>>><>>><<><><<>>>><" \
                   "<<<><><<<>>>><<>><<>>><<<<>>>><>>>><>><<<>><<<<>>>><><<><<>>>><<<>><<>>><<<<>><<>>><<<<>>>><<<>>>" \
                   "<<<><>><<><>>>><<>>>><<<><>>><>>>><<<<>>><<<>><<>>><<<<><<<>>><<>>><<<<>>><<>><<<><>>><><>>>><<>>" \
                   ">><<>><<<<><<<>>><<<<>><<<>><>><<<>><>>><<<>>>><>><><<>>><<>>><<<>>><<>><<<<>>>><<>><<>>><<>>><<>" \
                   ">><<>><><<<>>>><>>>><><<<>>><>>><<<<>>><<<<><>>>><<<<><<><<<>>>><<<>><<<><><<<<>>><<>>><<<<>>>><<" \
                   ">>><<<><<<<>>>><<<<>><<<><<>>><>><<>><<<<>><>>>><<>><<<>>><<<><<>>><<<><<<<><<<<><<>><>>>><>><>><" \
                   "<>>><<<<>>>><<<<>>><<<<><<<<><<<><>>><>>><<<<>><<>>>><><>>><>>>><><>>>><<<>><<>><<<<><>>>><<<><<<" \
                   "<><>>>><<>>><<<>>>><<>>>><<<<><<<<>>>><<><<<<>><<<>><>>><<<<><<>><<<>>><>><<<<>>>><<>>><<<>>><>><" \
                   "<<>>>><>><<<><<<<>>><<<<>><<>>><<<>>>><<<>>><><<><<<><<>>>><<>>><<>>>><>>>><<<<><><>>>><<<>>><<<>" \
                   ">>><<>><<<<><<<>>><<<>>>><>><<>>><<<>>>><>><><<<<>>>><>><<<<>>>><<<<>><>>>><<><<<<>><><<<>>><<<<>" \
                   "<<<<><>><>>>><<<>>>><<<>><<>>>><>><<<>>><<<>>><<<<>>><<<<><<>><<<<>><>>><>>><<>>><<<><<<<>>>><<<>" \
                   ">><<>>><<<<>><><<<>>>><><<<<>>><<<>>><<<>><<>>>><<>>><<<<>>><<>>><>>>><<>><<<>>>><<<<>>>><<<<><<>" \
                   "<><<>>>><<<<><<>>><<<<>>><<<<>><<><>>><>><<>>>><<<<>><<<>>><<<<>><<>><<><<>>><<<>><<<>>>><<>>><<<" \
                   ">>>><<<<>>><<<<>><<>>>><<<>>>><>><<<<>>><>>><<><<>>>><<<>>><>>><<<>><<<<><><<<>>><<<><<<>><<<<><<" \
                   "<>><<<<>>>><>><>><>>>><<<><<<>>><<<><<<<>>>><<>>>><<<>><<>><<<<>><>><<<><<<<>><<<>>>><<>>>><<>>>>" \
                   "<>>>><<<<>>><<>>>><<>>>><<>><<<>>><>>>><<<<><>>>><<<<><>>>><<<>>>><<<<>>><<<<>><><<<<>>><><>><<<<" \
                   ">>><<<>>><><<<>>>><<<>>>><<><<<<><<<<><<><<<<>>><>>>><<>>>><<<>>>><<<>>><<<<>>><>><<<><<<<>>>><<<" \
                   "<>>><<<<>>>><<<<><<<>><<<>>>><<<><<<<><>><<<<>><><<<>>><>><<<>>><<>><<>>><>><>>><<>>><<<>>>><>><<" \
                   "<>><<>>><<<<>>>><>><><<>><>><<<<><><<>>><<<<>>>><<>>><<<<>>><<<<><>>><<<>>>><<<<>>><<<>>>><<<>><<" \
                   "><><<<<>>><<>>>><<>>><<><<<<>>>><>><<>><<<<>><>>><<<<>><<>>>><<<<>>><<>><>><>><><<<>>>><<<>>><<>>" \
                   "<><<>>>><<<>>><<<>>>><<<<><<<>><>>><>>>><<<<><<<<>>>><<<>><<<<><<<<>>><<<<>>>><>>><<<<>>>><<<>><<" \
                   "<>><<<>>><<<<>>><<<>>>><>>><><<>>><>>>><<>>><<>>>><<<>><<<><<>>><<>>>><<<<>><><<<<><<<>><>>>><<<<" \
                   ">>>><<<<>>><<<<><><>>>><<>><>>><<>>>><<>>>><<<<>>><><<>>><<<<><<<><<>>><>>><>><>>>><>><<<>>>><<>>" \
                   "><<<>>><<>><<<<>>><<>>><<><<<<><<>>>><<<<><>>>><<<>><<><<<<><<><<>>>><<><<<<>>><<>>><>><>>><>>>><" \
                   ">>>><<>><<<<><<<<>>>><>>><<>>>><<<<>>><<><<<<>>><<<<>><>>>><>><<<<>>><<>><<<>><<>>><<<<>>>><<<>>>" \
                   "><>>>><>>>><<<<><>>><>>>><<<>><>><<><<<><<>>>><<<<>><<>>><<>>><<<<>><<<<><<<>>>><<<>><<>>>><<<>>>" \
                   "><<><><<<<>>>><><<>>><<>>>><<<>>><<>><<><<<><<<>>>><><<<>>><<<<>><>>>><<<><<><<<<>>>><<><<<<>>>><" \
                   "<<>><><<>>>><>>>><<<<><<<><<<>>>><<>><>>><<<>>>><<>>>><>><<<><<><<<<>>>><<>>>><<<>><<>><<<<><<>><" \
                   "<<>>>><<><<<>>><<<<>>><<<<><<>><<<>>>><>>>><<<<>>><>><<<<>>>><<<><<<<>>>><<<>>>><<><<<<>>>><<<<><" \
                   "<>>>><<><<><>>><>>><>>><>>>><<<<><<<<>>>><>><<<<>><<<<>>><<<<>>>><>><<<>>>><>>>><>>>><<>>>><>><<<" \
                   ">><><<>><<>>><>><><>>>><>>>><>>>><<<>><<><<<<>>>><><>>><><>><>><<>>><<>><<>>><<<<><<<>>><<<<>>>><" \
                   "<<<><<<>>><<<<>>>><<<<>>>><>>><><>><<<<>>>><<<<>><<><><<<><<>><<<<>><<<>><<<>>><<<>><<<>><><<>>>>" \
                   "<<<<><<>>>><<><<<>><<<<>>><<<>>><<<>><>><<<<>><<<<><<<<>><<<<><>>><<<<>><<<<>>><<<<><<><>><<<>><>" \
                   ">>><>>>><>>>><<<<>><<<<><<>>><>>>><<<<>>><<<><<<>>><<<>><<><<>>><<<>>>><<<>>>><<<<>><>>>><<<<>>><" \
                   ">>><<>>>><<>>>><>>><<<><>>><<<><>>>><<<<>>><<<>><<<>>>><<<<>>>><<><><><<<><<>>>><<<<><<<>><<>><<<" \
                   "<>>><<>>><<<><<<>>>><<>><>>><>>><<<<><<<>>><<<><<<><<<>><<>>><<><<>>>><<<<>>><<<>>>><<>><<<<>>>><" \
                   "<><<<<><<>>><<<><>>>><<<><<>>>><>>><<>>><<<<>><<>>>><<<>>><<<>>>><<<<>>>><<<><<<>>><<<><<<>>><<<<" \
                   "><<>>>><>>>><<<>>>><>>><>>>><<<>><<<<><<<<><<<<>><<<<><<<<><>><<><<<<>>><<<<>>><<>>><<<>>>><<<>>>" \
                   "><<<>><<<>><<<><<<>>><<>>>><><<<>><<<>>><<>><<<<><<>>><>><<<>>>><<<<>>>><<>>><<>><<><<<<><<<>>>><" \
                   "<<<>>>><<>>><<>><<<>>><>>>><<<>><>>>><<>>>><<<<>><<<<>>>><<>><>>><><<><<>>>><<>><<><>>>><<>><<<<>" \
                   ">>><>>><><<<<>>><<<<>>>><<>>>><<>>>><<<<>><<<>>><<>>><>>>><<<><<<><<<>><>><><>>>><<>><<<<>><<<<>>" \
                   "<><>><<>>>><<<><<<><>>><<<>>><<<>>>><<<>>><<<>>>><>>>><<<>><>>>><<<>>>><<<>>>><<<<><>>>><<<<>>>><" \
                   ">>><<<>>><<>><<><<<>>>><<<>>>><<<>><>><<<<>><<<>><<<>>><<<<><<<<>>>><<<<>>><<<<>><<<<>><<><>>><<<" \
                   ">>><<<<><<<>>><<<<><>>><<<>>>><>>>><><<<<>>>><><>><<>>>><>>><<<<>>><<<>><>><<<<><<<<>>><><<<<>>>>" \
                   "<>><>><<<<>><<>><<<<>><<>>><<>>><<<>>>><<>>><<>><<<<>>><<>>>><<><<>><<<<>>><<<<><<<<><<<><>>><<>>" \
                   "<<<<><<<>>>><>>>><><<<><<><<<<>><<<>><>>>><<<<>><<><<<><<<<>>>><<<><<>>>><><<><<<<><<<<>>><<<<>>>" \
                   "><<>>><<<><<<>>>><><<>>>><><<><<<<><<>>>><><<>><<>><>>><<><<<>><<>>>><<<<><<<<><><>>>><<<<>>><<<<" \
                   ">>><<>>>><<<><<<>><<<>>>><<<<><<<<>><<<<>>><<<<>>><>>><<<><<><<<<>>>><>><<>>><>><<<<>>><>>>><<>>>" \
                   "><<<<><<>>><<<<><<>><><<>>>><>><<>><<<<>><<>><<<<><<<<>>>><<<>><<>>><<><<<<>>>><<<>>>><<>>>><>>><" \
                   "<<>>><><<>><<>>><>>><>>>><<>>><<<>>>><><<<<><<>><<<<>>>><>><<<<><<<<><<<<>>>><<<><<<<>><<<>>>><<<" \
                   "<>><>>>><>><<<<>><>>><><<<>><><<<<>>><>>><<<>>>><<<>><<<<><<><<<><>>><>>>><<>>>><<<<>>><>>>><>>>>" \
                   "<<>><<>>><<<<>>><<>>><<>>>><<<><<>>>><<<<>><>><<<>>><<<<>>>><>>><<<>>>><<<>><<>><<>>>><<<>>><<<>>" \
                   ">><>><<>><<<<><>>>><>><<>><>><>><>><<<>><<><>>>><>>><<<<>>><<<>><<<<>><<<<>><><<<<><<<<>><<<<>>><" \
                   "<>>>><><<<<>><<<<>><<<<>><>><>>><<><<>>><<<><<<>>><>>><><<<>>>><<<<><<<>>>><<>><>>><<><<>><<<>><<" \
                   "<<><<<<>>><>>><<><<>>>><<<><<><<<<>>>><<<<><<>><>>><<<<><<<>>>><<>><<<><<<>>><>>>><>>><<>>><>>><<" \
                   "<<>><>>>><<><>>>><<<><<><<<<>>><<<>>>><<><><<>><<<<><<>><<><<<<>><<><<><<<<>><>><<<>>><<><<<>>><<" \
                   "<<>>><>>><><><<>>>><<><<<<><>><>>>><<<<><<<<>>><<<<>>>><>><<<>><<<>><<<<>>><<>>><<<<>>>><<<<>><<>" \
                   "><<>><<<<>><>>>><<><>>>><<<>>>><<<>><>>>><<<>>><<>>><<>><><<<<>>><<>><<<<>><<<><<>>><<<>>>><<>>><" \
                   "<>>>><<<<>>>><>>><><<<<>>><<<>>><<<>><<>>><<<<><<<>><<<>><<><>>><<<<><<>><<<<>><<><<><>>>><>>><<>" \
                   ">>><<<<>>><<><<<>><<<>>>><<>>>><>>>><<>><<<>>><>>>><<>><<<>>>><<<>><<<<>>>><<<<><<>>><>>><<<><<>>" \
                   "<>>><>>><<<>><<<<>><<<>>><>><<<>><<<<>>><<><><<<<>><<<><<<<>>><>>>><<<><<<<>><<<>><<><<<>>>><<<<>" \
                   "><>>><<<>><<>>><<<>><<<>>>><<<>>><<<<><<>><><<<>>><<<<>>>><<>>><>>>><<>>><<<<>>><>><<<>><>><<<<>>" \
                   "<<<<><<>>><<><<>>>><<<><>>>><<<>>><<<>>><<>><<<<>>><<>>>><<<<>>><<><<<>><<>>>><<<<><<<<>>>><<<<>>" \
                   "><<<>><<>>><<<><>>><<>>><><>>>><<>><>><<<<>>>><<<>>><<<<>>>><>><<<<>><<>><<<>>><<<<>>><<<>>><<>><" \
                   "<<>>>><<>>><<>><<<><<<>>><<>>><<<>>>><<<<>><<<<>><<<>>><<<>>><<>>>><<<<>>>><<><<<<><>><>>>><<><<>" \
                   ">><<<<><<<<>>>><>>><<<><>><<>>><<<<>>><<>>>><<<>>>><>>>><<<>><><<>>><<><<<>><<>><>>><<<<>><>>>><<" \
                   ">><>>><<<<>><<>>>><<><<<<>>>><<<>>><>>><<<><>>><>><<<<><>>>><<<<><<<<>>><>>><><<>>><<>>><><<<<><<" \
                   "<><>><>>>><<<>>>><><>><><>><<<<><<<><<<>>>><<<>>><<>>><<<>><<<><<>>><>>>><<><<>>>><<<<>><<>><>>><" \
                   "<<<>>><<<>>>><<<<>><<<<>>>><<>><<<>><<<>><<<>>>><<<<>>>><>><<<<>>>><><><>>><>>><<<>>><>><<<<>>>><" \
                   "<><<<>>>><<>>><<<><<<<>><<<><>>><<>>><<<<>>>><><<<<>><<<>><<<>><<<>><<>>>><<<>>>><<<>>><<<><<<><<" \
                   "<><<<<><>><<>>><><<<><<<>>><<<<>>>><<<>>><>>><><<<>><<<>>>><<><><<<<>>>><<><<<>>>><<<>>>><<><<<<>" \
                   ">>><<<><<<>>>><<>>>><<><><<<<>>><<<><<<><><<>>>><<>>>><<<>>>><<>><<><>>>><<<<>>>><<<<>>><<<<>><<<" \
                   "><<><>><<<>>>><>><>><<<<><><><><<<<>>><<<<>><<>><>><<>><<<>>>><<<>>>><<<<>>>><<<>><<<>>>><<>>>><<" \
                   "<><<<>>><>>><<<>>><<<<>>><<<<>>><>>><<<<>>><<<<>>><<<>><<<<><<<>>><<<<>><<<><<<>>><<<<>><<>><<<<>" \
                   "<<<<><><>>><<>><><<<<>>>><<>>><<<>><<><><>>><>>>><>>>><<<<>>><<<<>>>><<>>><<<<><<<<>>>><<>><<<>>>" \
                   "<<>>>><<<>><<<<>><><<<<>>><<>><<<<>>><<<<>>><>>><>>><<<<>>><<<<>>>><>>>><<<<>>><><<><>>>><><<<<>>" \
                   "><>>>><<>>>><<><<<<>>><<<>>>><<<>>><<<<>><<<><<<<><<<<>><<<>>>><<<<>>><<<><<<<>>><<<<>>><<>>><<<>" \
                   ">>><>>>><<>>><<<><<<><<<<>><<<<>>>><<>>><<<>>>><<<>><<<<><<<>>>><<<<>><<<<><<><<<<>>><<<>>>><<<><" \
                   ">><<<>><>><<>>><<><<<><><<<>><<>>>><<><>><<<>>><<>>>><>>>><<<<>>><<>>>><<>>><<>><<<><<<<><>>><<><" \
                   "<><>>><<<<>>>><<<>>>><<>>>><<<<>>>><<<><<<<><>>><<>><<<><<>>><>>><<<>>><<>>><<>>>><<><<<<>>><>><>" \
                   "><<<><<<<>><<<<>>>><>>><<>>>><<<<>><<>>>><<><>><<<>><<<><<<>>>><<>><<<>>><<<<>>><>>><>>><<<<>>>><" \
                   "<<>><<<>><<<<><<<>><<<>>><<>><<<>><<>><<<>>><<<<><<>>>><<><>><<>>><<<>>>><><>>>><>>>><><<<<>>>><<" \
                   ">><<>><>>>><<>><<>><<<<>><<>><<<<>>>><>><<<<><><>><<>><<<<>>><<<<>><<<><<<>><<<><<<>><<<<>>>><>>>" \
                   "<<<>>>><<<>>>><<<>>>><<>>>><<>><>>>><<<>>><<<<>><>>><<<>><>>><<<>>>><<<<><>><<<<><<>>>><<<>>>><<<" \
                   "<>>><>>><<<<><<>><>>><<<>>><>>>><<<>>><<<>><><>><<>>><<<>><<<>><>><<>>><<<>>><><>>><<<>>>><<><>>>" \
                   "<<>>>><<<<>>>><<<<>><<<<><<>>>><<<>><<>>>><<>>><<>>><<>>><<><<<<><<<>>><<<><>>><<<<><<<>>>><<<>>>" \
                   "><<<<><<>>>><<<>><<<>>>><<<<>>>><<<<>>><>>><<><<<><<<>>><<<<>>>><<<<>>>><<><><<<<>>>><<>><<<<>>><" \
                   "<<>><>>><<<>>><>><<<>>><>><<<><<>><>>><<<>><<>><>><<>>><>><<<><<<>>><<<<>><<<<>>><>>>><<<<><<<<>>" \
                   ">><>>><><<<<>>><<<<>>>><>><<>>>><<<<>>><<<<>><><<>>>><<>>><<<<>><<<>>><<<><<<<>>>><>><<>>><<>>><>" \
                   ">><<>>><<>><<<<>><<>>>><<<<>><<>>><<>><<>>><>>><<<>>>><<<>>>><<<<>>><>><<<>>><<<><<>>>><><<<>>>><" \
                   "<>><<>>>><>>><<>>>><><<>>><<<><>><<<>><>>>><>>>><<<>><<>>>><>><<>>>><<>><<<<>>>><<<<><>>><>>>><<>" \
                   "><<><<<><<><<<<>>><<<<>>>><<>><<>>><><<<>><>>>><<<>>><><<><<<>>><<<<>>><>>><<><<><<>><>><<><<>>><" \
                   "<<<"

