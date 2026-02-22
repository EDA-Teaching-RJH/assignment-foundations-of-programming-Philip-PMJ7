def init_database():
    names = ["Picard", "Riker", "Data", "Worf", "Spock"]
    ranks = ["Captain", "Commander", "Lt.Commander", "Lieutenant", "Commander"]
    divs = ["Command", "Command", "Operations", "Security", "Science"]
    ids = [1,  2, 3, 4, 5]
    return names, ranks, divs, ids


def main():
    names, ranks, divs, ids = init_database()

main()