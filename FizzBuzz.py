#Exercice 5 : FizzBuzz famous exercise

def FizzBuzz(upTo):
    for number in range(1, upTo + 1) :
        if(number % 3 == 0 and number % 5 == 0):
            print("FizzBuzz", end=" ")
        elif (number % 3 == 0):
            print("Fizz", end=" ")
        elif (number % 5 == 0):
            print("Buzz", end=" ")
        else :
            print(str(number), end=" ")

def main():
    print("Welcome to FizzBuzz!")
    print("Please enter a number for the range of FizzBuzz :")
    upTo = input('>')
    upTo = int(upTo)
    FizzBuzz(upTo)

if __name__ == "__main__":
    main()