from abc import ABC, abstractmethod
from typing import Any


class Provider(ABC):
	"""
	This abs class describes a provider.
	"""

	@abstractmethod
	def get_instance(self) -> Any:
		"""
		Gets the instance.

		:returns:	The instance.
		:rtype:		Any
		"""
		raise NotImplementedError
