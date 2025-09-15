#Exercice 3 : determines is a number is odd or even

def IsOdd(number):
    return True if number % 2 == 1 else False

def IsEven(number):
    return True if number % 2 == 0 else False

def main():
    assert IsOdd(42) == False
    assert IsOdd(9999) == True
    assert IsOdd(-10) == False
    assert IsOdd(-11) == True
    assert IsOdd(3.1415) == False
    assert IsEven(42) == True
    assert IsEven(9999) == False
    assert IsEven(-10) == True
    assert IsEven(-11) == False
    assert IsEven(3.1415) == False

    print ("All tests passed!")

if __name__ == "__main__":
    main()