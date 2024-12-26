from typing import Any

from echonextdi.providers.provider import Provider


class ResourceProvider(Provider):
	"""
	This class describes a resource provider.
	"""

	def __init__(self, resource: Any):
		"""
		Constructs a new instance.

		:param		resource:  The resource
		:type		resource:  Any
		"""
		self.resource = resource

	def __call__(self) -> Any:
		"""
		Get instance

		:returns:	resource
		:rtype:		Any
		"""
		return self.resource
