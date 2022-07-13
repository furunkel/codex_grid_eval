
def f(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest third value.
    """
    return max(lst, key=lambda x:x[2])[-1]
</code>
<|/ a tags=python,max,list |>
<| c |>
This doesn't work if there are multiple tuples with the same third value.
<|/ c |>
<| c |>
: I added a version that does work if there are multiple tuples with the same third value.
<|/ c |>
<| c |>
: I added a version that does work if there are multiple tuples with the same third value.
<|/ c |>
<| a tags=python,max,list |>
<code>
>>> l = [(1,2),(3,4),(5,6),(7,8)]
>>> max(l, key=lambda x:x[1])
(7, 8)
</code>
<|/ a dscore=5 |>
<| c |>
This doesn't work if there are multiple tuples with the same third value.
<|/ c |>
<| c |>
: I added a version that does work if there are multiple tuples with the same third value.
<|/ c |>
<| c |>
This doesn't work if there are multiple tuples with the same third value.
<|/ c |>
<| c |>
: I added a version that does work if there are multiple tuples with the same third value.
<|/ c |>
<| a dscore=5 |>
<code>
>>> l = [(1,2),(3,4),(5,6),(7,8)]
>>> max(l, key=lambda x:x[1])
(7, 8)
</code>
<|/ a tags=python,max,list |>
<| c |>
This doesn't work if there are multiple tuples with the same third value.
<|/ c |>
<| c |>
: I added a version that does work if there are multiple tuples with the same third value.
<|/ c |>
<| c |>
This doesn't work if there are multiple tuples with the same third value.
<|/ c |>
<| a tags=python,max,list |>
<code>
>>> l = [(1,2),(3,4),(5,6),(7,8)]
>>> max(l, key=lambda x:x[1])
(7, 8)
</code>
<|/ a dscore=5 |>
<| c |>
This doesn't work if there are multiple tuples with the same third value.
<|/ c |>
<| c |>
: I added a version that does work if there are multiple tuples with the same third value.
<|/ c |>
<| a dscore=5 |>
<code>
>>> l = [(1,2),(3,4),(5,6),(7,8)]
>>> max(l, key=lambda x:x[1])
(7, 8)
</code>
<|/ a 