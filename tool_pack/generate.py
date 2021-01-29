from .mcp.mcp.source import Unit
from .mcp.mcp.exceptions import raise_TpE

__all__ = [
	'gen_template'
]

def gen_template(unit):
	if type(unit) != Unit:
		raise_TpE('unit', Unit)
	
	