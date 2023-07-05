def predictPartyVictory( senate: str) -> str:
    R_BANS = 0
    D_BANS = 0

    new_senate = []

    while True:
        for senator in senate:
            if senator == 'R':
                if R_BANS > 0:
                    R_BANS -= 1
                    continue
                D_BANS += 1
                new_senate.append('R')
            else:
                if D_BANS > 0:
                    D_BANS -= 1
                    continue
                R_BANS += 1
                new_senate.append('D')

        if len(new_senate) == len(senate):
            return "Radiant" if new_senate[0] == 'R' else 'Dire'

        senate = new_senate
        new_senate = []