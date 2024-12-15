from typing import Any, Optional, Type

from echonextdi.providers.provider import Provider


class SingletonProvider(Provider):
	"""
	This class describes a singleton provider.
	"""

	def __init__(self, cls: Type):
		"""
		Constructs a new instance.

		:param		cls:  The cls
		:type		cls:  Type
		"""
		self.cls = cls
		self._instance: Optional[Any] = None

	def get_instance(self) -> Any:
		"""
		Gets the instance.

		:returns:	The instance.
		:rtype:		Any
		"""
		if self._instance is None:
			self._instance = self.cls()

		return self._instance
