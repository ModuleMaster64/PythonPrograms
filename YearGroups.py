# Selection commands

# Subroutine to output Key Stage
def YearGroup(Year):
    if Year >= 1 and Year <13:
        print("Key Stage 1-3!")
    else:
        print("Key Stage 4-5")

# Main program
YearGroup(11)
