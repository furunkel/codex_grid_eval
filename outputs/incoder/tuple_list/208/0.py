
def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest last value.
    """
    lst = sorted(lst)
    return lst[2]

# Test Cases
assert fibonacci([0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946,17711,28657,46368,75025,121393,196418,317811,514229,832040,1346269,2178309,3524578,5702887,9227465,14930352,24157817,39088169,63245986,102334155,165580141,267914296,433494437,701408733,1134903170,1836311903,3082640183,5331629117]) == 55
assert fibonacci([0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946,17711,28657,46368,75025,121393,196418,317811,514229,832040,1346269,2178309,3524578,5702887,9227465,14930352,24157817,39088169,63245986,102334155,165580141,267914296,433494437,701408733,1134903170,1836311903,3082640183,5331629117,765744987,1236937161,1910590506,3178460757,514229663,832042923,1346269673,2178309196,3524578273,5702887406,9227466137,14930352036,24157817105,39088169941,6324598587,10233415449,16558014108,26791429592,43349443689,70140873337,11349031723,18363119063,30826401876,53316291176,7752311721,12369371608,191059050610,31784607584,51422966303,8320429229,13462696733,21783091966,35245782733,57028874066,92274661377,