
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest third value.
    """
    
    smallest_third = lst[0][2]
    
    for tup in lst:
        if tup[2] < smallest_third:
            smallest_third = tup[2]
    
    return smallest_third
</cell>
<cell>
min_max([(1,2,3), (4,5,6), (7,8,9)])
</cell>
<cell>
min_max([(1,2,3), (4,5,6), (7,8,9), (10,11,12)])
</cell>
<cell>
min_max([(1,2,3), (4,5,6), (7,8,9), (10,11,12), (13,14,15)])
</cell>
<cell>
min_max([(1,2,3), (4,5,6), (7,8,9), (10,11,12), (13,14,15), (16,17,18)])
</cell>
<cell>
min_max([(1,2,3), (4,5,6), (7,8,9), (10,11,12), (13,14,15), (16,17,18), (19,20,21)])
</cell>
<cell>
min_max([(1,2,3), (4,5,6), (7,8,9), (10,11,12), (13,14,15), (16,17,18), (19,20,21), (22,23,24)])
</cell>
<cell>
min_max([(1,2,3), (4,5,6), (7,8,9), (10,11,12), (13,14,15), (16,17,18), (19,20,21), (22,23,24), (25,26,27)])
</cell>
<cell>
min_max([(1,2,3), (4,5,6), (7,8,9), (10,11,12), (13,14,15), (16,17,18), (19,20,21), (22,23,24), (25,26,27), (28,29,30)])
</cell>
<cell>
min_max([(1,2,3), (4,5,6), (7,8,9), (10,11,12), (13,14,15), (16,17,18), (19,20,21), (22,23,24), (25,26,27), (28,29,30), (31,32,33)])
</cell>
<cell>
min_max([(1,2,3), (4,5,6), (7,8,9), (10,11,12), (13,14,15), (16,17,18), (19,20,21), (22,23,24), (25,26,27), (28,29,30), (31,32,33), (34,35,36)])
</cell>
<cell>
min_max([(1,2,3), (4,5,6), (7,8,9), (10,11,12), (13,14,15), (16,17,18), (19,20,21), (22,23,24), (25,26,27), (28,29,30), (31,32,33), (34,35,36), (37,38,39)])