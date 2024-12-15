import inspect
from typing import Any, Dict, Optional, Type, TypeVar

from echonextdi.exceptions import DependencyAlreadyExistsError, DependencyNotFoundError
from echonextdi.providers.provider import Provider

T = TypeVar("T")


class Container:
	"""
	This class describes a container.
	"""

	def __init__(self):
		"""
		Constructs a new instance.
		"""
		self._providers: Dict[str, Provider] = {}

	def register(self, key: str, provider: Provider):
		"""
		Register dependency in container

		:param		key:						   The key
		:type		key:						   str
		:param		provider:					   The provider
		:type		provider:					   Provider

		:raises		DependencyAlreadyExistsError:  dependency is already registred
		"""
		if key not in self._providers:
			self._providers[key] = provider
		else:
			raise DependencyAlreadyExistsError(
				f'Dependency "{key}" is already registred. Use `container.override`'
			)

	def override(self, key: str, provider: Provider):
		"""
		Override dependency

		:param		key:					  The key
		:type		key:					  str
		:param		provider:				  The provider
		:type		provider:				  Provider

		:raises		DependencyNotFoundError:  Depedency not found for overriding
		"""
		if key not in self._providers:
			raise DependencyNotFoundError(
				f'Dependency "{key}" not found for overriding. Use `container.register`'
			)

		self._providers[key] = provider

	def get(self, key: str, raise_error: Optional[bool] = True) -> Any:
		"""
		Get dependency instance by key

		:param		key:					  The key
		:type		key:					  str
		:param		raise_error:			  The raise error
		:type		raise_error:			  bool

		:returns:	provider instance or None
		:rtype:		Any

		:raises		DependencyNotFoundError:  dependency by key not found
		"""
		provider = self._providers.get(key)

		if provider is None:
			if raise_error:
				raise DependencyNotFoundError(f'Dependency "{key}" not found')

			return None

		return provider.get_instance()

	def resolve(self, cls: Type[T]) -> T:
		"""
		Automatic resolve dependencies for class

		:param		cls:  The cls
		:type		cls:  Type[T]

		:returns:	class object
		:rtype:		T
		"""
		constructor = inspect.signature(cls.__init__)
		dependencies = {
			name: self.get(param.annotation.__name__)
			for name, param in constructor.parameters.items()
			if param.annotation in self._providers
		}

		return cls(**dependencies)
