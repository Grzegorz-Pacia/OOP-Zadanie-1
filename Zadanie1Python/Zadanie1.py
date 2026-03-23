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
        

    #elif choice == 2:
    #elif choice == 3:


if __name__ == "__main__":
    main()