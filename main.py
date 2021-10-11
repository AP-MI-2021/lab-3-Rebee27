'''
Proprietatea 1 : Numerele sunt ordonate crescător.
Proprietatea 2 : Toate numerele au partea întreagă egală cu partea fracționară.
Proprietatea 3 : Verifica daca o lista este formata doar din numere prime.
'''


def printMeniu():
    print("1.Citire lista")
    print("2.Determinare cea mai lunga subsecventa cu proprietatea 4")
    print("3.Determinare cea mai lunga subsecventa cu proprietatea 14")
    print("4.Determinare cea mai lunga subsecventa cu proprietatea 2")
    print("x.Iesire")


def citireLista():
    l = []
    givenString = input("Dati lista, cu elemente separate prin virgula")
    numberAsString = givenString.split(",")
    for x in numberAsString:
        l.append(int(x))
    return l


'''verifica daca lista este sortata'''


def sorted(lst: list[int]) -> bool:
    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i]:
            return False
        return True


def test_sorted():
    assert sorted([]) == True
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
    return x[0] == x[1]


def test_intreaga_egal_fractionara():
    assert intreaga_egal_fractionara(0.0) == True
    assert intreaga_egal_fractionara(78.86) == False
    assert intreaga_egal_fractionara(23.23) == True


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True


'''returneaza cea mai lunga subsecventa de numere care au partea intreaga egala cu partea fractionara'''


def get_longest_equal_int_real(lst: list[float]) -> list[float]:
    subsecv_finala = []
    lungime_max = 0

    for i in range(len(lst)):
        for j in range(i, len(lst)):
            subsecv_curenta = lst[i:j + 1]
            if len(subsecv_curenta) < lungime_max and intreaga_egal_fractionara(lst):
                lungime_max = len(subsecv_curenta)
                subsecv_finala = subsecv_curenta
    return subsecv_finala


def test_get_longest_equal_int_real():
    assert get_longest_equal_int_real([3.3, 58.58, 7.8, 6.6, 0.0, 36.36]) == [6.6, 0.0, 36.36]
    assert get_longest_equal_int_real([3.2, 5.6, 8.9]) == []
    assert get_longest_equal_int_real([]) == []


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
            if len(subsecv_curenta) < lungime_max and numere_prime(lst):
                lungime_max = len(subsecv_curenta)
                subsecv_finala = subsecv_curenta
    return subsecv_finala


def main():
    test_numere_prime()
    test_sorted()
    test_intreaga_egal_fractionara()
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
