import math


def calculateDistanceBetweenPoints():
    while True:
        try:
            x = int(input("Input a value for x: "))
            y = int(input("Input a value for y: "))
            x1 = int(input("Input a value for x1: "))
            y1 = int(input("Input a value for y1: "))
            x_distance = abs(x - x1)
            y_distance = abs(y - y1)
            break

        except ValueError:
            print("You must input an integer")

    print("The distance between x and x1 is " + str(x_distance))
    print("The distance between y and y1 is " + str(y_distance))
    print("")
    return x_distance, y_distance


def convertUsToCan():
    keep_going = "y"
    # Will loop until the user selects "n" to exit
    while keep_going == "y":

        try:
            usd = float(input("Enter in USD to Convert to CAD: "))
            exchange_rate = input("Enter the exchange rate from USD to CAD: ")
            if exchange_rate == "":
                exchange_rate = 1.5
                print("The Default Exchange rate is 1.5")
            exchange_rate = float(exchange_rate)
            cad = usd * exchange_rate
            print("$", usd, " USD is $", cad, " CAD")

        # if the user inputs anything other than a float it will be caught and loop again
        except ValueError:
            print("Oops You didn't enter a valid number")

        # asks the user if they want to loop again
        keep_going = input("Would you like to convert again? y/n ?: ")
        # loops until the user inputs a valid option which can only be a "y" or "n"
        while keep_going != "y" and keep_going != "n":
            print(keep_going, " is not a valid option")
            keep_going = input("Would you like to convert again? y/n ?: ")

        print("")

    print("Done Converting USD to CAD")
    print("")


def calculateAreaOfCircle():
    # Begins the first loop
    keep_going = "y"
    # Will loop until the user selects "n" to exit
    while keep_going == "y":
        while True:
            try:
                radius = float(input("Enter the Radius of a circle: "))
                # the equation to find the area of a circle is  (A = π r²)
                area = math.pi * pow(radius, 2)
                print("The area of a circle that has a radius of ", radius, " is ", area)
                break

            # if the user inputs anything other than a float it will be caught and loop again
            except ValueError:
                print("Oops You didn't enter a valid number")

        # asks the user if they want to loop again
        keep_going = input("Would you like to calculate the area of another circle? y/n ? : ")
        # loops until the user inputs a valid option which can only be a "y" or "n"
        while keep_going != "y" and keep_going != "n":
            print(keep_going, " is not a valid option")
            keep_going = input("Would you like to calculate the area of another circle? y/n ? : ")

        print("")

    print("Done Calculating the Area of a Circle")
    print("")


def convertFahrenheitToCelsius():
    # Begins the first loop
    keep_going = "y"
    # Will loop until the user selects "n" to exit
    while keep_going == "y":

        while True:
            try:
                fahrenheit = input("Enter a degree in Fahrenheit to convert to Celsius :")
                if fahrenheit == "":
                    fahrenheit = 0
                    print("The Default value is 0")
                    break
                fahrenheit = float(fahrenheit)
                is_float = True
                break
            except ValueError:
                print("Oops You didn't enter a valid number")

        # I based the equation off information from this site https://www.mathsisfun.com/temperature-conversion.html
        celsius = ((fahrenheit - 32) * 5) / 9
        print(fahrenheit, " degrees fahrenheit is ", celsius, " degrees celsius")

        # asks the user if they want to loop again
        keep_going = input("Would you like to convert again? y/n ? : ")
        # loops until the user inputs a valid option which can only be a "y" or "n"
        while keep_going != "y" and keep_going != "n":
            print(keep_going, " is not a valid option")
            keep_going = input("Would you like to convert again? y/n ?: ")

        print("")

    print("Done converting Fahrenheit to Celsius")
    print("")
