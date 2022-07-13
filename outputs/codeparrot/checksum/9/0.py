
def checksum(string):
    """
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo 64, add the integer value of lowercase u, and then convert that integer back
    into its corresponding character (the checksum character).
    The program must print "Check sum is X", where X is replaced by the correct checksum character.
    """

def main():
    """
    Main function.
    """
    if len(sys.argv) != 2:
        print "Usage: %s <file.txt>" % sys.argv[0]
        sys.exit(1)

    file = open(sys.argv[1], 'r')
    lines = file.readlines()
    file.close()

    for line in lines:
        line = line.strip()
        if line == "":
            continue
        if line[0] == '#':
            continue
        if line[0] == '0':
            continue
        if line[0] == '1':
            continue
        if line[0] == '2':
            continue
        if line[0] == '3':
            continue
        if line[0] == '4':
            continue
        if line[0] == '5':
            continue
        if line[0] == '6':
            continue
        if line[0] == '7':
            continue
        if line[0] == '8':
            continue
        if line[0] == '9':
            continue
        if line[0] == '10':
            continue
        if line[0] == '11':
            continue
        if line[0] == '12':
            continue
        if line[0] == '13':
            continue
        if line[0] == '14':
            continue
        if line[0] == '15':
            continue
        if line[0] == '16':
            continue
        if line[0] == '17':
            continue
        if line[0] == '18':
            continue
        if line[0] == '19':
            continue
        if line[0] == '20':
            continue
        if line[0] == '21':
            continue
        if line[0] == '22':
            continue
        if line[0] == '23':
            continue
        if line[0] == '24':
            continue
        if line[0] == '25':
            continue
        if line[0] == '26':
            continue