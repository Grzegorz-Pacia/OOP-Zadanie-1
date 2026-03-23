using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Serialization;

namespace Zadanie1C_
{
    internal class Program
    {
        static int IntegerInput()
        {
            int number;
            while (true) {
                try
                {
                    number = Int32.Parse(Console.ReadLine());
                    break;
                }
                catch
                {
                    Console.WriteLine("Podano błędną wartość, spróbuj ponownie:");
                }
            }
            return number;
        }
        static void Main(string[] args)
        {
            int choice;
            String errorText = "Podano błędną wartość, spróbuj ponownie:";

            Console.WriteLine("Wybierz podzadanie:\n" +
                                  "1. Kalkulator\n" +
                                  "2. Konwerter temperatur\n" +
                                  "3. Średnia ocen");
            while (true)
            {
                choice = IntegerInput();
                if (choice == 1 || choice == 2 || choice == 3)
                {
                    Console.WriteLine();
                    break;
                }
                else
                {
                    Console.WriteLine(errorText);
                }
            }


            switch(choice)
            {
                case 1:

                    int a, b;
                    char mathOperator;

                    Console.WriteLine("Podaj liczbę całkowitą a:");
                    a = IntegerInput();
                    Console.WriteLine("Podaj liczbę całkowitą b:");
                    b = IntegerInput();
                    Console.WriteLine("Wybierz operację: +, -, * lub /:");
                    while (true)
                    {
                        try
                        {
                            mathOperator = Char.Parse(Console.ReadLine());
                            if (mathOperator == '+' || mathOperator == '-' || mathOperator == '*' || mathOperator == '/')
                            {
                                break;
                            }
                            else
                            {
                                Console.WriteLine(errorText);
                            }
                        }
                        catch
                        {
                            Console.WriteLine(errorText);
                        }
                    }

                    if (mathOperator == '+')
                    {
                        Console.WriteLine("Wynik: " + (a+b));
                    }
                    else if (mathOperator == '-')
                    {
                        Console.WriteLine("Wynik: " + (a-b));
                    }
                    else if (mathOperator == '*')
                    {
                        Console.WriteLine("Wynik: " + (a*b));
                    }
                    else if (mathOperator == '/')
                    {
                        Console.WriteLine("Wynik: " + (Convert.ToDouble(a) / Convert.ToDouble(b)));
                    }

                    break;


                case 2:

                    int temperature;
                    char convertionType;

                    Console.WriteLine("Wybierz opcję konwersji temperatury:\n" +
                                      "C - ze stopni Celciusza na Fahrenheita\n" +
                                      "F - ze stopni Fahrenheita na Celciusza");
                    while(true)
                    {
                        try
                        {
                            convertionType = Char.Parse(Console.ReadLine());
                            if (convertionType == 'C' || convertionType == 'F')
                            {
                                break;
                            }
                            else
                            {
                                Console.WriteLine(errorText);
                            }
                        }
                        catch
                        {
                            Console.WriteLine(errorText);
                        }
                    }
                    Console.WriteLine("Podaj temperaturę (°" + convertionType + "):");
                    temperature = IntegerInput();

                    if (convertionType == 'C')
                    {
                        Console.WriteLine(temperature + "°C = " + (temperature * 1.8 + 32) + "°F");
                    }
                    else if (convertionType == 'F')
                    {
                        Console.WriteLine(temperature + "°F = " + ((temperature - 32) / 1.8) + "°C");
                    }
                    
                    break;


                case 3:
                    break;
            }
        }
    }
}
