CAMELOT = {
    "Abm": "1A", "Ebm": "2A", "Bbm": "3A", "Fm": "4A",
    "Cm": "5A", "Gm": "6A", "Dm": "7A", "Am": "8A",
    "Em": "9A", "Bm": "10A", "Gbm": "11A", "Dbm": "12A",
    "B": "1B", "Gb": "2B", "Db": "3B", "Ab": "4B",
    "Eb": "5B", "Bb": "6B", "F": "7B", "C": "8B",
    "G": "9B", "D": "10B", "A": "11B", "E": "12B",
}

def compatible(key1, key2):
    code1 = CAMELOT[key1]
    code2 = CAMELOT[key2]

    num1, letter1 = int(code1[:-1]), code1[-1]
    num2, letter2 = int(code2[:-1]), code2[-1]

    # Rule 1: same code
    if code1 == code2:
        return True

    # Rule 2: same letter, numbers one apart (12 and 1 count as neighbors)
    if letter1 == letter2 and abs(num1 - num2) in (1,11):
        return True

    # Rule 3: same number, different letter
    if num1 == num2:
        return True

    return False


print(compatible("Am", "Em"))   # should print True
print(compatible("Am", "Fm"))   # should print False
print(compatible("Dbm", "Abm"))