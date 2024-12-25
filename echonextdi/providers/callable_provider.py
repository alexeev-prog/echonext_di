from typing import Any, Callable

from echonextdi.providers.provider import Provider


class CallableProvider(Provider):
	"""
	This class describes a callable provider.
	"""

	def __init__(self, handler: Callable):
		"""
		Constructs a new instance.

		:param		handler:  The handler
		:type		handler:  Callable
		"""
		self.handler = handler

	def get_instance(self, *args, **kwargs) -> Any:
		"""
		Gets the instance.

		:returns:	The instance.
		:rtype:		Any
		"""
		return self.handler(*args, **kwargs)
