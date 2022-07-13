
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Pling' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    has 11 as a factor, add 'Plang' to the result.
    does not have any of 13, 5, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 13 or 5, so the result would be "Plang".
    65 has both 13 and 5 as factors, but not 11, so the result would be "PlingBuzz".
    2 is not factored by 13, 5, or 11, so the result would be "2".
    """
    factors = []
    factors.append(str(num))
    factors.append(str(num//13))
    factors.append(str(num//5))
    factors.append(str(num//11))
    factors.append(str(num%13))
    factors.append(str(num%5))
    factors.append(str(num%11))
    
    factors.sort()
    
    final = ""
    for factor in factors:
        if factor == "13":
            final += "Pling"
        elif factor == "5":
            final += "Buzz"
        elif factor == "11":
            final += "Plang"
        else:
            final += factor
    return final

print(raindrops(22))
print(raindrops(65))
print(raindrops(2))
</cell>
<text>
Problem 4
Write a function that takes a string and returns the number of words in the string.

The string can contain punctuation marks and spaces.

Examples:

"Hello, world!" returns 5.
"Hello, world. How are you?" returns 7.
"Hello, world." returns 0.
"Hello, world. How are you?" returns 0.
"Hello, world." returns 0.
"Hello, world. How are you?" returns 0.
"Hello, world. How are you?" returns 0.
"Hello, world. How are you?" returns 0.
"Hello, world. How are you?" returns 0.
"Hello, world. How are you?" returns 0.
"Hello, world. How are you?" returns 0.
"Hello, world. How are you?" returns 0.
"Hello, world. How are you?" returns 0.
"Hello, world. How are you?" returns 0.
"Hello, world. How are you?" returns 0.
"Hello, world. How are you?" returns 0.
"Hello, world. How are you?" returns 0.
"Hello, world. How are you?" returns 0.
"Hello, world. How are you?" returns 0.
"Hello, world. How are you?" returns 0.
"Hello, world. How are you?" returns 0.
"Hello, world. How are you?" returns 0.
"Hello, world. How are you?" returns 0.
"Hello, world. How are you?" returns 0.
"Hello, world. How are you?" returns 0.
"Hello, world. How are you?" returns 0.
"Hello, world. How are you?" returns 0.
"Hello, world. How are you?" returns 0.
"Hello, world. How are 