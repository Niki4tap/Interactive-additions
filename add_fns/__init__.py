from forbiddenfruit import curse, reverse
from typing import Type

builtin_fn = Type[hex]

def add_builtin_fns(self: builtin_fn, other: builtin_fn):
	def s(*args, **kwargs):
		return other(self(*args, **kwargs))
	return s

fn = Type[add_builtin_fns]

def add_fns(self: fn, other: fn):
	def s(*args, **kwargs):
		return other(self(*args, **kwargs))
	return s

def allow_fn_sum():
	curse(type(hex), "__add__", add_builtin_fns)
	curse(type(add_builtin_fns), "__add__", add_fns)

def disallow_fn_sum():
	reverse(type(hex), "__add__")
	reverse(type(add_builtin_fns), "__add__")

allow_fn_sum()
