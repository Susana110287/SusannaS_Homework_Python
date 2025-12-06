n = int(input("Введите число:"))

def fizz_buzz(n):
     for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} - FizzBuzz") #Делится на 3 и на 5
        elif i % 3 == 0:
            print(f"{i} - Fizz") #Делится на 3
        elif i % 5 == 0:
            print(f"{i} - Buzz") #Делится на 5
        else:
            print(i)

fizz_buzz(n)
