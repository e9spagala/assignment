# 5. Data Structures

### More on Lists:

Lists have the fllowing methods


`append(x)` -> appends new element at end of the list
`extend(x)` -> appends new sequence at end of the list
`insert(i, x)` -> inserts new element at given position
`remove(x)` -> removes first matched x in the list
`pop(x)` -> pops from the list if the index is not given. If index is given it will pop out the value from it.
`clear()` -> clears the list

`index(val)` -> returns the first index of the matched val.

`sort()` -> sorts the list. Uses Timsort which has O(nlogn)

`copy()` -> returns shallow copy

- We can manupulate this list to use it as both `stack` and `queue`.
- `del` statement deletes the item at a given index it can also be used to delete slice of lists aswell as the whole list.

### List Comprehensions:

Syntax: [to do | loop | condition]

ex: [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
- We could also make nested list comprehensions


### Tuples and Sequences:
- Tuples are sequential data which is immutable.

- tuple can be initilized also like this.
```python
t = 12345, 54321, 'hello!'
```

- there is a special problem while declaring tuple with only one value.

```python
# Will not work and would be converted into an integer
t = (1) 
# This will work
t = 1 ,
a = (1 , )
```

### Sets

- Sets are declared using `set()` function, usually represented using curly braces `{}`.
- User must use `set()` function inorder to create an empty set.

### Dictionaries:

- Dictionaries are key vaule paris. It is represented by `{}` or `dict()` function.
- Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. You can’t use lists as keys, since lists can be modified in place using index assignments, slice assignments, or methods like append() and extend().

- So by the above statement any mutable data structure cannot act as a key.

### Looping Techniques:

`dict.items()` -> give a list of tuples of (key, value) pairs
`enumerate()` -> give a list of tuples of (key, value) pairs
`zip(0)` -> to iterate over 2 or more lists at a time

`sorted(arr)` -> returns a new array of sorted elements of arr

### More conditions

- The conditions used in `while` and `if` statements can contain any operators, not just comparisons.

- comparision operators -> `in`, `not in`, `is`, `is not`
- boolean operators -> `or`, `and`
- negation -> `not`

###  Comparing Sequences and Other Types

we can compare 2 sequences. The comparision will happen through lexographical ordering.