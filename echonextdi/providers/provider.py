from abc import ABC, abstractmethod
from typing import Any


class Provider(ABC):
	"""
	This abs class describes a provider.
	"""

	@abstractmethod
	def __call__(self) -> Any:
		"""
		Gets the instance.

		:returns:	The instance.
		:rtype:		Any
		"""
		raise NotImplementedError
