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
		self._resolved: set = set()

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

		return provider

	def resolve(self, cls: Type[T], *args, **kwargs) -> T:
		"""
		Resolve dependency

		:param		cls:	 The cls
		:type		cls:	 Type[T]
		:param		args:	 The arguments
		:type		args:	 list
		:param		kwargs:	 The keywords arguments
		:type		kwargs:	 dictionary

		:returns:	class instance
		:rtype:		T
		"""
		constructor = inspect.signature(cls.__init__)

		dependencies = {}

		for name, param in constructor.parameters.items():
			if name in self._providers:
				dependencies[name] = self.get(name)

		return cls(**dependencies)
