import os

from .mcp import mcp
from .mcp.mcp.tools.path import run_here

from .exceptions import SubmoduleMissingError

def listdir():
	return os.listdir('.')

with run_here(listdir) as dirlist:
	if 'mcp' not in dirlist:
		raise SubmoduleMissingError('Submodule "mcp" not found')
	
	if 'tam' not in dirlist:
		raise SubmoduleMissingError('Submodule "tam" not found')

from .generate import *
