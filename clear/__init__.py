from os import system
from platform import system as platform

class _clear_impl(type):
	def __repr__(self):
		os = platform()
		if os == "Linux" or os == "Darwin":
			system("clear")
		elif os == "Windows":
			system("cls")
		else:
			raise NotImplementedError()
		return ""

class clear(metaclass=_clear_impl): pass
