
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Plang' to the result.
    has 3 as a factor, add 'Buzz' to the result.
    has 7 as a factor, add 'Plong' to the result.
    does not have any of 13, 3, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 13 or 3, so the result would be "Plong".
    39 has both 13 and 3 as factors, but not 7, so the result would be "PlangBuzz".
    2 is not factored by 13, 3, or 7, so the result would be "2".
    """
    factors = []
    factors.append(13)
    factors.append(3)
    factors.append(7)
    factors.append(1)
    factors.append(2)
    factors.append(4)
    factors.append(8)
    factors.append(16)
    factors.append(32)
    factors.append(64)
    factors.append(128)
    factors.append(256)
    factors.append(512)
    factors.append(1024)
    factors.append(2048)
    factors.append(4096)
    factors.append(8192)
    factors.append(16384)
    factors.append(32768)
    factors.append(65536)
    factors.append(131072)
    factors.append(262144)
    factors.append(524288)
    factors.append(1048576)
    factors.append(2097152)
    factors.append(4194304)
    factors.append(8388608)
    factors.append(16777216)
    factors.append(33554432)
    factors.append(67108864)
    factors.append(134217728)
    factors.append(268435456)
    factors.append(536870912)
    factors.append(1073741824)
    factors.append(2147483648)
    factors.append(4294967296)
    factors.append(8589934592)
    factors.append(17179869184)
    factors.append(34359738368)
    factors.append(68719476736)
    factors.append(137438953472)
    factors.append(274877906944)
    factors.append(549755813888)
    factors.append(1099511627776)
    factors.append(2199023255552)
    factors.append(4398046511104)
    factors.append(8796093022208)
    factors.append(17592186044416)
    factors.append(35184372088832)
    factors.append(70368744177664)
    factors.append(13743895347208)
    factors.append(27487790694416)
    factors.append(54975581388832)
    factors.append(109951162777632)
    factors.append(219902325555208)
    factors.append(439804651110408)
    factors.append(879609302220808)
    factors.append(175921860444168)
    factors.append(351843720888128)
    factors.append(703687441776648)
    factors.append(1374389534720808)
    