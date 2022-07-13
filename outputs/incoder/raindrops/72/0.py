
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Fizz' to the result.
    has 5 as a factor, add 'Plang' to the result.
    has 11 as a factor, add 'Plong' to the result.
    does not have any of 3, 5, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 3 or 5, so the result would be "Plong".
    15 has both 3 and 5 as factors, but not 11, so the result would be "FizzPlang".
    2 is not factored by 3, 5, or 11, so the result would be "2".
    """
    if num < 1:
        return "Invalid input"
    factors = []
    factors.append(3)
    factors.append(5)
    factors.append(11)
    factors.append(num)
    factors.sort()
    factors.reverse()
    factors.insert(0, num)
    factors.insert(1, num)
    factors.insert(2, num)
    factors.insert(3, num)
    factors.insert(4, num)
    factors.insert(5, num)
    factors.insert(6, num)
    factors.insert(7, num)
    factors.insert(8, num)
    factors.insert(9, num)
    factors.insert(10, num)
    factors.insert(11, num)
    factors.insert(12, num)
    factors.insert(13, num)
    factors.insert(14, num)
    factors.insert(15, num)
    factors.insert(16, num)
    factors.insert(17, num)
    factors.insert(18, num)
    factors.insert(19, num)
    factors.insert(20, num)
    factors.insert(21, num)
    factors.insert(22, num)
    factors.insert(23, num)
    factors.insert(24, num)
    factors.insert(25, num)
    factors.insert(26, num)
    factors.insert(27, num)
    factors.insert(28, num)
    factors.insert(29, num)
    factors.insert(30, num)
    factors.insert(31, num)
    factors.insert(32, num)
    factors.insert(33, num)
    factors.insert(34, num)
    factors.insert(35, num)
    factors.insert(36, num)
    factors.insert(37, num)
    factors.insert(38, num)
    factors.insert(39, num)
    factors.insert(40, num)
    factors.insert(41, num)
    factors.insert(42, num)
    factors.insert(43, num)
    factors.insert(44, num)
    factors.insert(45, num)
    factors.insert(46, num)
    factors.insert(47, num)
    factors.insert(48, num)
    factors.insert(49, num)
    factors.insert(50, num)
    factors.insert(51, num)
    factors.insert(52, num)
    factors.insert(53, num)
    factors.insert(54, num)
    factors.insert(55, num)
    factors.insert(56, num)
    factors.insert(57, num)
    factors.insert(58, num)
    factors.insert(59, num)
    factors.insert(60, num)
    factors.insert(61, num)
    factors.insert(62, num)
    factors.insert(63, num)
    factors.insert(64, num)
    factors.insert(65, 