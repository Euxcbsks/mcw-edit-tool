import os

from .exceptions import SubmoduleMissingError

if 'mcp' not in os.listdir('.'):
	raise SubmoduleMissingError('Submodule "mcp" not found')

if 'tam' not in listdir:
	raise SubmoduleMissingError('Submodule "tam" not found')

from .generate import *