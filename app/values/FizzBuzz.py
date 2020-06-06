from app.getters.InputDataForFizz import getInputData
from app.logger.PrintOutputData import printOutput

'''
The method fizzBuzz will return "FizzBuzz" if the number is divisible by 15  or it will return "Fizz" it is divisible by 3
or it will return "Buzz" if it is divisible by 5 or it will return the same number if it is not divisible by 3 or 5 or 15 
'''

def fizzBuzz(num):
    if (num % 15 == 0):
        return "FizzBuzz"
    elif(num%3 == 0):
        return "Fizz"
    elif (num%5 == 0):
        return "Buzz"
    else:
        return str(num)
'''
fizzBuzzOfNNumbers method retun the list of encoded numbers
'''

def fizzBuzzOfNNumbers(lower_bound,upper_bound):
    encoded_numbers = []
    for number in range(lower_bound,upper_bound+1):
        encoded_numbers.append(fizzBuzz(number))
    return encoded_numbers

'''
main function to get the input data and processing the data and printing the output
'''
def main():
    [lower_bound,upper_bound] = getInputData()
    encoded_numbers = fizzBuzzOfNNumbers(lower_bound,upper_bound)
    printOutput(encoded_numbers)

if __name__ == "__main__":
    main() #calling main method