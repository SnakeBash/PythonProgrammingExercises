#Defines conversion functions and runs asserts
def ConvertToFahrenheit(degreesCelsius):
    return degreesCelsius * (9/5) + 32

def ConvertToCelsius(degreesFahrenheit):
    return (degreesFahrenheit - 32) * (5/9)

def main():
    assert ConvertToCelsius(0) == -17.77777777777778
    assert ConvertToCelsius(180) == 82.22222222222223
    assert ConvertToFahrenheit(0) == 32
    assert ConvertToFahrenheit(100) == 212
    assert ConvertToCelsius(ConvertToFahrenheit(15)) == 15

    # Rounding errors cause a slight discrepancy:
    assert ConvertToCelsius(ConvertToFahrenheit(42)) == 42.00000000000001

    print("All passed!")

if __name__ == '__main__':
    main()