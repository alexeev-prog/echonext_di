from typing import Any, Type, TypeVar

from echonextdi.containers.container import Container

T = TypeVar("T")


class Depends:
	"""
	This class describes depends.
	"""

	def __init__(self, container: Container, dependency: Type[T]):
		"""
		Constructs a new instance.

		:param		container:	 The container
		:type		container:	 Container
		:param		dependency:	 The dependency
		:type		dependency:	 Type[T]
		"""
		self.container = container
		self.dependency = dependency

	def __call__(self) -> Any:
		"""
		Resolve dependency

		:returns:	resolved provider
		:rtype:		Any
		"""
		return self.container.resolve(self.dependency)
