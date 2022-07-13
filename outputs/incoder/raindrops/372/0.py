
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 11 as a factor, add 'Fizz' to the result.
    has 3 as a factor, add 'Pling' to the result.
    has 5 as a factor, add 'Plong' to the result.
    does not have any of 11, 3, or 5 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 5 as a factor, but not 11 or 3, so the result would be "Plong".
    33 has both 11 and 3 as factors, but not 5, so the result would be "FizzPling".
    2 is not factored by 11, 3, or 5, so the result would be "2".
    """
    if num < 1:
        return "Invalid input"
    factors = []
    factors.append(num)
    while num != 1:
        factors.append(num % 10)
        num = num // 10
    factors.append(num)
    factors.sort()
    factors.reverse()
    factors.insert(0,"Fizz")
    factors.insert(1,"Pling")
    factors.insert(2,"Plong")
    factors.insert(3,"FizzPling")
    factors.insert(4,"FizzPlong")
    factors.insert(5,"FizzPlong")
    factors.insert(6,"FizzPlong")
    factors.insert(7,"FizzPlong")
    factors.insert(8,"FizzPlong")
    factors.insert(9,"FizzPlong")
    factors.insert(10,"FizzPlong")
    factors.insert(11,"FizzPlong")
    factors.insert(12,"FizzPlong")
    factors.insert(13,"FizzPlong")
    factors.insert(14,"FizzPlong")
    factors.insert(15,"FizzPlong")
    factors.insert(16,"FizzPlong")
    factors.insert(17,"FizzPlong")
    factors.insert(18,"FizzPlong")
    factors.insert(19,"FizzPlong")
    factors.insert(20,"FizzPlong")
    factors.insert(21,"FizzPlong")
    factors.insert(22,"FizzPlong")
    factors.insert(23,"FizzPlong")
    factors.insert(24,"FizzPlong")
    factors.insert(25,"FizzPlong")
    factors.insert(26,"FizzPlong")
    factors.insert(27,"FizzPlong")
    factors.insert(28,"FizzPlong")
    factors.insert(29,"FizzPlong")
    factors.insert(30,"FizzPlong")
    factors.insert(31,"FizzPlong")
    factors.insert(32,"FizzPlong")
    factors.insert(33,"FizzPlong")
    factors.insert(34,"FizzPlong")
    factors.insert(35,"FizzPlong")
    factors.insert(36,"FizzPlong")
    factors.insert(37,"FizzPlong")
    factors.insert(38,"FizzPlong")
    