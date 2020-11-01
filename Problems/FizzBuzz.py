def FizzBuzz(n):

    result = ""

    if n % 3 == 0:
        result += "Fizz"

    if n % 5 == 0:
        result += "Buzz"
    
    if result == "":
        result += str(n)

    return result

def FizzBuzzRange(n):
    for i in range(1, n):
        print(FizzBuzz(i))

FizzBuzzRange(20)