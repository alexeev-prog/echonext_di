from typing import Any, List, Tuple, Type

from echonextdi.containers.container import Container
from echonextdi.providers.configuration_provider import ConfigurationProvider
from echonextdi.providers.provider import Provider
from echonextdi.providers.resource_provider import ResourceProvider


class DeclarativeContainer(Container):
	"""
	This class describes a declarative container.
	"""

	def __init__(self):
		"""
		Constructs a new instance.
		"""
		super().__init__()
		self._declarations: List[Tuple[Type, Provider]] = []

	def declare(self, dependency_type: Type, provider: Provider):
		"""
		Declare dependency

		:param		dependency_type:  The dependency type
		:type		dependency_type:  Type
		:param		provider:		  The provider
		:type		provider:		  Provider
		"""
		self._declarations.append((dependency_type, provider))

	def declarative_build(self):
		"""
		Declarative register
		"""
		for dep_type, provider in self._declarations:
			self.register(dep_type, provider)

	def register_resource(self, key: str, resource: Any):
		"""
		Register resource

		:param		key:	   The key
		:type		key:	   str
		:param		resource:  The resource
		:type		resource:  Any
		"""
		self.register(key, ResourceProvider(resource))

	def register_configuration(self, key: str, config_path: str):
		"""
		Register configuration

		:param		key:		  The key
		:type		key:		  str
		:param		config_path:  The configuration path
		:type		config_path:  str
		"""
		self.register(key, ConfigurationProvider(config_path))
