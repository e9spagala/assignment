# 3. An Informal Introduction to Python

### Using python as a calculator

- We can use pythn interpreter asa a calculator.
```bash
>>> 2 + 2
4

>>> 50 - 5*6
20

>>> (50 - 5*6) / 4
5.0

>>> 8 / 5  # division always returns a floating point number
1.6
>>> 8 // 5  # floor division discards the fractional part
1
>>> 17 % 3
2
>>> 2 ** 4 # Power operator

```

Note: there are 2 operators `/` division operator gives float as the answer and `//` (floor division operator) which will give the int as the answer.

- `=` sign is used to assign the variable.
```bash
>>> greet = "hello world"
>>> one = 1
```

- If the variable is not declared

```bash
>>> n  # try to access an undefined variable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
```

- integers that intract with floating point variables will be converted into floating points.

- In interactive mode, the last printed expression is assigned to the variable `_`. This must be considered as a read only variable

```bash
>>> tax = 12.5 / 100

>>> price = 100.50

>>> price * tax
12.5625

>>> price + _
113.0625

>>> round(_, 2)
113.06
```

- Python also supports `Decimal` and `Fraction` and `complex numbers`, and uses the j or J suffix to indicate the imaginary part `(e.g. 3+5j)`.

### Text

- Text is considered as a string in python.
- It can be enclosed between single or double quotes.
- To escape a quote we can use back slash `\`.
String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''. End of lines are automatically included in the string, but it’s possible to prevent this by adding a \ at the end of the line. The following example:

- We can use `+` operator to apend 2 strings.
- Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
- strings are just array of characters in python which means we can access individual characters but we cannot change the values as the python strings are immutable.
- there is negative indexing in python where we can iterate the list from behind like -1 represents the last element and -2 represents the second last element etc.
- strings can be split using `:` operator like shown below
> word[0:2] 
- Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.


### Lists

- Lists are sequential data structures.
- It can contain items of different data type.
- List can also be indexed and sliced.
- list supports `+` which appends 2 lists 
- Lists are mutable

## Shallow Copy
>Simple assignment in Python never copies data. When you assign a list to a variable, the variable refers to the existing list. Any changes you make to the list through one variable will be seen through all other variables that refer to it.:
