def IntegerInput():
    number = 0
    while 1:
        try:
            number = int(input())
            break
        except:
            print("Podano błędną wartość, spróbuj ponownie:")
    return number

def main():
    choice = 0
    errorText = "Podano błędną wartość, spróbuj ponownie:"

    print("Wybierz podzadanie:")
    print("1. Kalkulator")
    print("2. Konwerter temperatur")
    print("3. Średnia ocen")
    while 1:
        choice = IntegerInput()
        if choice == 1 or choice == 2 or choice == 3:
            print()
            break
        else:
            print(errorText)

    if choice == 1:

        a = 0
        b = 0
        mathOperator = ''
        print("Podaj liczbę całkowitą a:")
        a = IntegerInput()
        print("Podaj liczbę całkowitą b:")
        b = IntegerInput()
        print("Wybierz operację: +, -, * lub /:")
        while 1:
            try:
                mathOperator = input()
                if mathOperator == "+" or mathOperator == "-" or mathOperator == "*" or mathOperator == "/":
                    break
                else:
                    print(errorText)
            except:
                print(errorText)
        
        if mathOperator == "+":
            print("Wynik: " + str(a+b))
        elif mathOperator == "-":
            print("Wynik: " + str(a-b))
        elif mathOperator == "*":
            print("Wynik: " + str(a*b))
        elif mathOperator == "/":
            print("Wynik: " + str(a/b))
        

    elif choice == 2:

        temperature = 0
        convertionType = ''

        print("Wybierz opcję konwersji temperatury:")
        print("C - ze stopni Celciusza na Fahrenheita")
        print("F - ze stopni Fahrenheita na Celciusza")
        while 1:
            try:
                convertionType = str(input())
                if convertionType == "C" or convertionType == "F":
                    break
                else:
                    print(errorText)
            except:
                print(errorText)
        print("Podaj temperaturę (°" + convertionType + "):")
        temperature = IntegerInput()

        if convertionType == "C":
            print(str(temperature) + "°C = " + str(temperature * 1.8 + 32) + "°F")
        elif convertionType == "F":
            print(str(temperature) + "°F = " + str((temperature - 32) / 1.8) + "°C")


    elif choice == 3:
        
        gradeCount = 0
        gradeNext = 0
        gradeSum = 0
        gradeAverage = 0

        print("Podaj liczbę ocen, które chcesz wprowadzić:")
        while 1:
            gradeCount = IntegerInput()
            if gradeCount > 0:
                break
            else:
                print(errorText)
        
        for i in range(gradeCount):
            print("Podaj ocenę nr. " + str(i+1) + " (skala ocen: 1-6):")
            while 1:
                gradeNext = IntegerInput()
                if gradeNext == 1 or gradeNext == 2 or gradeNext == 3 or gradeNext == 4 or gradeNext == 5 or gradeNext == 6:
                    break
                else:
                    print(errorText)
            gradeSum += gradeNext

        gradeAverage = gradeSum / gradeCount
        print("Średnia: " + str(gradeAverage))
        if gradeAverage >= 3:
            print("Uczeń zdał.")
        else:
            print("Uczeń nie zdał.")


if __name__ == "__main__":
    main()