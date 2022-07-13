
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Pling' to the result.
    has 3 as a factor, add 'Buzz' to the result.
    has 7 as a factor, add 'Plang' to the result.
    does not have any of 13, 3, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 13 or 3, so the result would be "Plang".
    39 has both 13 and 3 as factors, but not 7, so the result would be "PlingBuzz".
    2 is not factored by 13, 3, or 7, so the result would be "2".
    """
    factors = []
    factors.append(num)
    factors.append(num / 13)
    factors.append(num / 3)
    factors.append(num / 7)
    factors.append(num % 13)
    factors.append(num % 3)
    factors.append(num % 7)
    factors.sort()
    factors.reverse()
    factors.insert(0,"Plang")
    factors.insert(1,"Pling")
    factors.insert(2,"Buzz")
    factors.insert(3,"Plang")
    factors.insert(4,"Pling")
    factors.insert(5,"Buzz")
    factors.insert(6,"Plang")
    factors.insert(7,"Pling")
    factors.insert(8,"Buzz")
    factors.insert(9,"Plang")
    factors.insert(10,"Pling")
    factors.insert(11,"Buzz")
    factors.insert(12,"Plang")
    factors.insert(13,"Pling")
    factors.insert(14,"Buzz")
    factors.insert(15,"Plang")
    factors.insert(16,"Pling")
    factors.insert(17,"Buzz")
    factors.insert(18,"Plang")
    factors.insert(19,"Pling")
    factors.insert(20,"Buzz")
    factors.insert(21,"Plang")
    factors.insert(22,"Pling")
    factors.insert(23,"Buzz")
    factors.insert(24,"Plang")
    factors.insert(25,"Pling")
    factors.insert(26,"Buzz")
    factors.insert(27,"Plang")
    factors.insert(28,"Pling")
    factors.insert(29,"Buzz")
    factors.insert(30,"Plang")
    factors.insert(31,"Pling")
    factors.insert(32,"Buzz")
    factors.insert(33,"Plang")
    factors.insert(34,"Pling")
    factors.insert(35,"Buzz")
    factors.insert(36,"Plang")
    factors.insert(37,"Pling")
    factors.insert(38,"Buzz")
    factors.insert(39,"Plang")
    factors.insert(40,"Pling")
    factors.insert(41,"Buzz")
    factors.insert(42,"Plang")
    factors.insert(43,"Pling")
    factors.insert(44,"Buzz")
    factors.insert(45,"Plang")
    factors.insert(46