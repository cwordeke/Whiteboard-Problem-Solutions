# Carson Wordekemper 12-3-25
# Lab 11 - This script completes fizz buzz in two different methods

def main():
    num = int(input("Enter an int: "))

    fizzBuzzModulusResult = fizzBuzzModulus(num)
    print("Modulus:", fizzBuzzModulusResult)

    fizzBuzzDictResult = fizzBuzzDict(num)
    print("Dictionary:", fizzBuzzDictResult)

# Modulus method
def fizzBuzzModulus(num):
    output = []
    for i in range(1, num+1):
        if (i % 3 == 0) and (i % 5 == 0):
            output.append("FizzBuzz")
        elif (i % 3) == 0:
            output.append("Fizz")
        elif (i % 5) == 0:
            output.append("Buzz")
        elif (i % 7) == 0:
            output.append("Bazz")
        else:
            output.append(str(i))
    return output

# Hashmap method
def fizzBuzzDict(num):
    output = []
    fizz_buzz = {3: "Fizz", 5: "Buzz", 7: "Bazz"}
    for i in range(1, num+1):
        s = ""
        for key in fizz_buzz:
            if i % key == 0:
                s = s + fizz_buzz[key]
        if s == "":
            s = str(i)
        output.append(s)

    return output

if __name__ == "__main__":
    main()