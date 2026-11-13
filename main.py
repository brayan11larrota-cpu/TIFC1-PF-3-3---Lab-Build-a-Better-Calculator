def addmultiplenumbers(numbers):
    return sum(numbers)


def multiplymultiplenumbers(numbers):
    resultado = 1

    for numero in numbers:
        resultado = resultado * numero
    return resultado
   
def isiteven(num: int) -> bool:
    return num % 2 == 0

def isitaninteger(num: int) -> bool:
    return isinstance(num , int)

def main():
    numeros = [5, 10, 15, 20]
    resultado = addmultiplenumbers(numeros)
    print(resultado)

    resultado = multiplymultiplenumbers(numeros)
    print(resultado)

    print(isiteven(2))

    print(isinstance(6.5, float))


if __name__=="__main__":
  main()