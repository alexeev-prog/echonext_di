from abc import ABC, abstractmethod
from typing import Any, Dict

import json
import toml
import yaml

from echonextdi.providers.provider import Provider


class AbstractConfig(ABC):
	"""
	This class describes an abstract configuration.
	"""

	@abstractmethod
	def get_loaded_config(self) -> Dict[Any, Any]:
		"""
		Gets the loaded configuration.

		:returns:   The loaded configuration.
		:rtype:     { return_type_description }
		"""
		raise NotImplementedError


class AbstractConfigFactory(ABC):
	"""
	Front-end to create abstract configuration objects.
	"""

	def create_config(self) -> AbstractConfig:
		"""
		Creates a configuration.

		:returns:   The abstract configuration.
		:rtype:     AbstractConfig
		"""
		raise NotImplementedError


class ConfigFactory(AbstractConfigFactory):
	"""
	Front-end to create configuration objects.
	"""

	def __init__(self, config_path: str):
		"""
		Constructs a new instance.

		:param      config_path:  The configuration path
		:type       config_path:  str
		"""
		self.ext = config_path.split(".")[-1]
		self.config_path = config_path

	def create_config(self) -> Dict[Any, Any]:
		"""
		Creates a configuration.

		:returns:   config dict
		:rtype:     Dict[Any, Any]
		"""
		if self.ext.lower() == "json":
			return JSONConfig(self.config_path)
		elif self.ext.lower() == "toml":
			return TOMLConfig(self.config_path)
		elif self.ext.lower() == "yaml":
			return YAMLConfig(self.config_path)


class JSONConfig(AbstractConfig):
	"""
	This class describes a json configuration.
	"""
	
	def __init__(self, config_path: str):
		"""
		Constructs a new instance.

		:param      config_path:  The configuration path
		:type       config_path:  str
		"""
		self.config_path = config_path
		self.config: Dict[Any, Any] = {}

	def get_loaded_config(self) -> Dict[Any, Any]:
		"""
		Gets the loaded configuration.

		:returns:   The loaded configuration.
		:rtype:     Dict[Any, Any]
		"""
		with open(self.config_path) as f:
			self.config = json.load(f)

		return self.config


class TOMLConfig(AbstractConfig):
	"""
	This class describes a toml configuration.
	"""

	def __init__(self, config_path: str):
		"""
		Constructs a new instance.

		:param      config_path:  The configuration path
		:type       config_path:  str
		"""
		self.config_path = config_path
		self.config: Dict[Any, Any] = {}

	def get_loaded_config(self) -> Dict[Any, Any]:
		"""
		Gets the loaded configuration.

		:returns:   The loaded configuration.
		:rtype:     Dict[Any, Any]
		"""
		with open(self.config_path) as f:
			self.config = toml.load(f)

		return self.config


class YAMLConfig(AbstractConfig):
	"""
	This class describes an yaml configuration.
	"""

	def __init__(self, config_path: str):
		"""
		Constructs a new instance.

		:param      config_path:  The configuration path
		:type       config_path:  str
		"""
		self.config_path = config_path
		self.config: Dict[Any, Any] = {}

	def get_loaded_config(self) -> Dict[Any, Any]:
		"""
		Gets the loaded configuration.

		:returns:   The loaded configuration.
		:rtype:     Dict[Any, Any]
		"""
		with open(self.config_path) as f:
			self.config = yaml.load(f, Loader=yaml.FullLoader)

		return self.config


class ConfigurationProvider(Provider):
	"""
	This class describes a configuration provider.
	"""

	def __init__(self, config_path: str):
		"""
		Constructs a new instance.

		:param      config_path:  The configuration path
		:type       config_path:  str
		"""
		self.factory = ConfigFactory(config_path)
		self.config = self.factory.create_config()

	def get_instance(self) -> AbstractConfig:
		"""
		Gets the instance.

		:returns:   The instance.
		:rtype:     AbstractConfig
		"""
		
		return self.config
