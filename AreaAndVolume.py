#Exercice 4 : calculates area, perimeter, surface area and volume

def Area(length, width):
    return length * width

def Perimeter(length, width):
    return (length + width) * 2

def Volume(length, width, height):
    return length * width * height

def SurfaceArea(length, width, height):
    return (length * width * 2) + (length * height * 2) + (width * height * 2)

def main():
    assert Area(10, 10) == 100
    assert Area(0, 9999) == 0
    assert Area(5, 8) == 40
    assert Perimeter(10, 10) == 40
    assert Perimeter(0, 9999) == 19998
    assert Perimeter(5, 8) == 26
    assert Volume(10, 10, 10) == 1000
    assert Volume(9999, 0, 9999) == 0
    assert Volume(5, 8, 10) == 400
    assert SurfaceArea(10, 10, 10) == 600
    assert SurfaceArea(9999, 0, 9999) == 199960002
    assert SurfaceArea(5, 8, 10) == 340

    print("All tests passed!")

if __name__ == "__main__":
    main()