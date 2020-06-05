from app.getters.InputDataForFizz import getInputData
from app.helper.PrintOutputData import printOutput


def fizzBuzz(num):
    if (num % 15 == 0):
        return "FizzBuzz"
    elif(num%3 == 0):
        return "Fizz"
    elif (num%5 == 0):
        return "Buzz"
    else:
        return str(num)

def fizzBuzzOfNNumbers(lower_bound,upper_bound):
    result = []
    for i in range(lower_bound,upper_bound+1):
        result.append(fizzBuzz(i))
    return result

def main():
    [lower_bound,upper_bound] = getInputData()
    result = fizzBuzzOfNNumbers(lower_bound,upper_bound)
    printOutput(result)

if __name__ == "__main__":
    main() #calling main method