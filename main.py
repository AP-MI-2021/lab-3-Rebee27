'''
Proprietatea 1 : Numerele sunt ordonate crescător.
Proprietatea 2 : Toate numerele au partea întreagă egală cu partea fracționară.
Proprietatea 3 : Verifica daca o lista este formata doar din numere prime.
'''


def printMeniu():
    print("1.Citire lista")
    print("2.Determinare cea mai lunga subsecventa cu proprietatea 1: Numerele sunt ordonate crescător")
    print("3.Determinare cea mai lunga subsecventa cu proprietatea 2: Toate numerele au partea întreagă egală cu partea fracționară")
    print("4.Determinare cea mai lunga subsecventa cu proprietatea 3: Verifica daca o lista este formata doar din numere prime")
    print("x.Iesire")


def citireLista():
    l = []
    givenString = input("Dati lista, cu elemente separate prin virgula")
    numberAsString = givenString.split(",")
    for x in numberAsString:
        l.append(x)
    return l


'''verifica daca lista este sortata'''


def sorted(lst: list[int]) -> bool:
    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i]:
            return False
    return True


def test_sorted():
    assert sorted([1, 2, 3, 4, 5]) == True
    assert sorted([4, 5, 2, 9]) == False


'''returneaza cea mai lunga subsecventa sortata ascendent'''


def get_longest_sorted_asc(lst: list[int]) -> list[int]:
    subsecv_finala = []
    lungime_max = 0

    for i in range(len(lst)):
        for j in range(i, len(lst)):
            subsecv_curenta = lst[i:j + 1]
            if len(subsecv_curenta) > lungime_max and sorted(lst):
                lungime_max = len(subsecv_curenta)
                subsecv_finala = subsecv_curenta
    return subsecv_finala


'''verifica daca partea intreaga a unui numar este egala cu partea fractionara'''
def intreaga_egal_fractionara(n: float) -> bool:
    x = str(n).split('.')
    if x[0] == x[1]:
        return True
    return False


def test_intreaga_egal_fractionara():
    assert intreaga_egal_fractionara(1.1) == True
    assert intreaga_egal_fractionara(78.86) == False
    assert intreaga_egal_fractionara(23.23) == True
    assert intreaga_egal_fractionara(23.233) == False


def lista_intreaga_egal_fractionara(lst: list[float]) -> bool:
    for x in lst:
        if not intreaga_egal_fractionara(x):
            return False

    return True


def test_lista_intreaga_egal_fractionara():
    assert lista_intreaga_egal_fractionara([33.33, 44.44, 56.56]) == True
    assert lista_intreaga_egal_fractionara([]) == True
    assert lista_intreaga_egal_fractionara([43.23, 54.89, 23.63, 85.88]) == False
    assert lista_intreaga_egal_fractionara([1.1]) == True


'''returneaza cea mai lunga subsecventa de numere care au partea intreaga egala cu partea fractionara'''
def get_longest_equal_int_real(lst: list[float]) -> list[float]:
    subsecv_finala = []
    lungime_max = 0

    for i in range(len(lst)):
        for j in range(i, len(lst)):
            subsecv_curenta = lst[i:j + 1]
            if len(subsecv_curenta) > lungime_max and lista_intreaga_egal_fractionara(subsecv_curenta):
                lungime_max = len(subsecv_curenta)
                subsecv_finala = subsecv_curenta
    return subsecv_finala


def test_get_longest_equal_int_real():
    assert get_longest_equal_int_real([52.52, 41.41, 21.21, 14.2, 54.54, 13.3]) == [52.52, 41.41, 21.21]
    assert get_longest_equal_int_real([3.2, 5.6, 8.9]) == []
    assert get_longest_equal_int_real([3.2, 5.6, 8.9, 3.3]) == [3.3]
    assert get_longest_equal_int_real([]) == []


def is_prime(n: int) -> bool:
    if int(n) < 2:
        return False

    for i in range(2, int(n) // 2 + 1):
        if int(n) % i == 0:
            return False

    return True


def numere_prime(lst: list[int]) -> bool:
    for x in lst:
        if not is_prime(x):
            return False

    return True


def test_numere_prime():
    assert numere_prime([]) == True
    assert numere_prime([2, 3, 7, 11]) == True
    assert numere_prime([4, 7, 9]) == False


'''returneaza cea mai lunga subsecventa a unei liste care are toate elementele prime'''
def get_longest_all_primes(lst: list[int]) -> list[int]:
    subsecv_finala = []
    lungime_max = 0

    for i in range(len(lst)):
        for j in range(i, len(lst)):
            subsecv_curenta = lst[i:j + 1]
            if len(subsecv_curenta) > lungime_max and numere_prime(subsecv_curenta):
                lungime_max = len(subsecv_curenta)
                subsecv_finala = subsecv_curenta
    return subsecv_finala


def main():
    test_sorted()
    test_numere_prime()
    test_intreaga_egal_fractionara()
    test_lista_intreaga_egal_fractionara()
    test_get_longest_equal_int_real()
    l = []
    while True:
        printMeniu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
            print(get_longest_sorted_asc(l))
        elif optiune == "3":
            print(get_longest_equal_int_real(l))
        elif optiune == "4":
            print(get_longest_all_primes(l))
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati!")


main()
