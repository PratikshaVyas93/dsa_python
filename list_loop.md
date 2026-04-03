1. what is list?
A. A list store multiple values in single variable. we can think of it like array.

2. Access element.
A. Can access an element using index such as 0, 1, 2, etc...

3. what is indexing?
A. Accesing element bu position. that starts from 0.

4. module (%)?
A. This s a modulo operator that checks the reminder after devision (useful for even/odd).

5. equality (=)?
A. This is a equal sign that compares values for equality.

6. Addition assignment (+=)?
A. Adds to a variable(shorthand for sum = sum+i).

7. Range function?
A. range(len(arr)) geretates indices for looping. 

eg. for i in range(len(arr)):
    loops over indices to 0 to 4

8. For loop?
A. Iterates over elements or indices.

- to add new value in the list we can use append, for specific index we want to add value then use insert and for deleting the last element we can use pop()


- logic to find max - use variable and assume that the first element is the biggest one then loop through all and check condition if the element in array is greaterthan max element if yes then max element will be change with the updated new max element.

Start: len(list_arr) - 1 (e.g., 4 for a list of length 5). This begins at the last element's index.
Stop: -1. This tells the loop to stop before reaching -1 (i.e., when i becomes -1, stop). Since indices start at 0, this ensures you go down to index 0.
Step: -1. This makes the loop count downwards (decrement by 1 each time), instead of the default upwards.

☐ Learned list basics  
☐ Used loops on lists  
☐ Solved sum problem  
☐ Found max/min  
☐ Counted even/odd  
☐ Reversed list  

From today, start noticing patterns:

Loop over list → Traversal pattern
Find max/min → Comparison pattern
Count something → Frequency pattern