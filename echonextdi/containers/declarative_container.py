from typing import Any

from echonextdi.containers.container import Container
from echonextdi.providers.configuration_provider import ConfigurationProvider
from echonextdi.providers.resource_provider import ResourceProvider


class DeclarativeContainer(Container):
	"""
	This class describes a declarative container.
	"""

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
