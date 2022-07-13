
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest eleventh value.
    """
    
    # Your code here
    
    return max(lst, key=lambda x:x[-1])[-11]

# Test your code
print(some_func([(1,2,3), (4,5,6), (7,8,9)]))
</cell>
<text>
Great Job!

</text>
<text>


</text>
<text>




</text>
<text>
NumPy Exercises
Now that we've learned about NumPy let's test your knowledge. We've already imported NumPy as np and have a play around with it in the IPython Shell but let's test some things with it.

Print the numpy version and run the following to see what it returns:


</text>
<cell>
print(np.__version__)
</cell>
<text>
Create a 3 x 4 matrix with row values ranging from 0 to 8 and column values ranging from 0 to 7. Cells in row i column j contain the value i j.


</text>
<cell>
# Write your answer here
</cell>
<text>
Create a 3 x 4 matrix with row values ranging from 0 to 8 and column values ranging from 0 to 23. Cells in row i column j contain the value i j+1.


</text>
<cell>
# Write your answer here
</cell>
<text>
Create a 3 x 4 matrix with row values ranging from 0 to 1 and column values ranging from 0 to 5. Then use Matplotlib to plot it.


</text>
<cell>
# Write your answer here
</cell>
<text>
Now do the following:

Display the matrix. 
Change the values in the matrix to be arange from 0 to 8
Finally use Matplotlib to plot it.

Note: Don't forget to import Matplotlib.


</text>
<cell>
# Write your answer here
</cell>
<text>
Now do the following:

Display the matrix. 
Change the values in the matrix to be arange from 0 to 1
Finally use Matplotlib to plot it.

Note: Don't forget to import Matplotlib.


</text>
<cell>
# Write your answer here
</cell>
<text>
Now do the following:

Display the matrix. 
Change the values in the matrix to be arange from 0 to 2
Finally use Matplotlib to plot it.

Note: Don't forget to import Matplotlib.


</text>
<cell>
# Write your answer here
</cell>
<text>
Now do the following:

Display the matrix. 
Change the values in the matrix to be arange from 0 to 3
Finally use Matplotlib to plot it.

Note: Don't forget to import Matplotlib.


</text>
<cell>
# Write your answer here
