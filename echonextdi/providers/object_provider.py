from typing import Any

from echonextdi.providers.provider import Provider


class ObjectProvider(Provider):
	"""
	This class describes an object provider.
	"""

	def __init__(self, obj: Any):
		"""
		Constructs a new instance.

		:param		obj:  The object
		:type		obj:  Any
		"""
		self.obj = obj

	def get_instance(self) -> Any:
		"""
		Gets the instance.

		:returns:	The instance.
		:rtype:		Any
		"""
		return self.obj
