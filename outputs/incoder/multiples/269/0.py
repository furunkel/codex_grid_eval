
def multiples():
    """
    If we list all the natural numbers below 5 that are multiples of 2, 3 or 5, we get 2, 3 and 4. The product of these multiples is 24.
    Return the product of all the multiples of 2, 3 or 5 below 124.
    """    
    
    multiples = []
    
    for i in range(125, 1, -1):
        if i % 2 == 0:
            multiples.append(i)
        if i % 3 == 0:
            multiples.append(i)
        if i % 5 == 0:
            multiples.append(i)
    
    return sum(multiples)
</cell>
<cell>
multiples()
</cell>
<text>
Write a function that returns the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

</text>
<cell>
def sum_except_for_6s_and_9s(arr):
    
    total = 0
    
    for i in range(len(arr)):
        if arr[i] != 6:
            total += arr[i]
        else:
            total += arr[i]
            if arr[i+1] == 9:
                break
    
    return total
</cell>
<cell>
sum_except_for_6s_and_9s([2,3,5,7,8,9,11,13,14,16,18,19,21,23,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,112,114,116,118,120,122,124,126,128,130,132,134,136,138,140,142,144,146,148,150,152,154,156,158,160,162,164,166,168,170,172,174,176,178,180,182,184,186,188,190,192,194,196,198,200,202,204,206,208,210,212,214,216,218,220,222,224,226,228,230,232,234,236,238,240,242,244,246,248,250,252,254,256,258,260,262,264,266,268,270,272,274,276,278,280,282,284,286,288,290,292,294,296,298,300,302,304,306,308,310,312,314,316,318,320,322,324,326,328,330,332,334,336,338,340,342,344,346,348,350,352,354,356,358,