# Interactive additions
Series of python modules that I wish were included in interactive python shell.

Can be used as: `python -i -m interactive_additions`
Or: `python -i -c "from interactive_additions import *"`
Or just drop into a python repl and do: `from interactive_additions import *`

## clear
Typing `clear` into python repl causes the screen to clear, I really missed the clear command in the repl.

## add_fns
Allows adding functions together!
```python
>>> from interactive_additions import *
>>> hexord = ord + hex
>>> hexord("A")
'0x41' 
```