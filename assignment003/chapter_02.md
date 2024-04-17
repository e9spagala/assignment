# 2. Using the Python Interpreter


### Invoking the interpreter:

- On linux OS python interpreter lies in `/usr/local/bin/python3.12`.
- To invoke the python3 interpreter use `python3` command.
- On Windows OS py.exe launcher is installed so we can use `py` command to launch the interpreter
- Typing `ctrl + d` `ctrl + z` in windows will shutdown the interpreter with exit code 0.
- Alternatively we can use quit() method to exit the interpreter terminal.

- Second way of starting interpreter is by using  `python -c command [arg]...`
- In order to run modules use `python -m module [arg] ... `

### Argument Passing:
- The command line arguments are turned in to list of strings and are stored in `argv` variable in the `sys` module. You can access it by importing it by `import sys`
- The length of the list is atleast one.

### Intractive mode:
- We could use `tty` shell to launch python interpreter for intractivity. which looks like this

```bash
charlie@enine020:~$ python3
Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 

```

### Interpreter and Environment:
- Python code is encoaded in UTF-8.
- Your editor must be capable of parsing the UTF-8 file
- In order to declare other encodings you can do it in a comment like shown below:

```python
# -*- coding: encoding -*-
```
- This comment should be in the first line of the code file.

