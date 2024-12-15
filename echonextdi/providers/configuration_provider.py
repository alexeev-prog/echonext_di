from abc import ABC, abstractmethod
from typing import Any, Dict

import orjson as json
import toml
import yaml

from echonextdi.providers.provider import Provider


class AbstractConfig(ABC):
	@abstractmethod
	def get_loaded_config(self) -> Dict[Any, Any]:
		raise NotImplementedError


class AbstractConfigFactory(ABC):
	def create_config(self) -> AbstractConfig:
		raise NotImplementedError


class ConfigFactory(AbstractConfigFactory):
	def __init__(self, config_path: str):
		self.ext = config_path.split(".")[-1]
		self.config_path = config_path

	def create_config(self):
		if self.ext.lower() == "json":
			return JSONConfig(self.config_path)
		elif self.ext.lower() == "toml":
			return TOMLConfig(self.config_path)
		elif self.ext.lower() == "yaml":
			return YAMLConfig(self.config_path)


class JSONConfig(AbstractConfig):
	def __init__(self, config_path: str):
		self.config_path = config_path
		self.config: Dict[Any, Any] = {}

	def get_loaded_config(self) -> Dict[Any, Any]:
		with open(self.config_path) as f:
			self.config = json.load(f)

		return self.config


class TOMLConfig(AbstractConfig):
	def __init__(self, config_path: str):
		self.config_path = config_path
		self.config: Dict[Any, Any] = {}

	def get_loaded_config(self) -> Dict[Any, Any]:
		with open(self.config_path) as f:
			self.config = toml.load(f)

		return self.config


class YAMLConfig(AbstractConfig):
	def __init__(self, config_path: str):
		self.config_path = config_path
		self.config: Dict[Any, Any] = {}

	def get_loaded_config(self) -> Dict[Any, Any]:
		with open(self.config_path) as f:
			self.config = yaml.load(f, Loader=yaml.FullLoader)

		return self.config


class ConfigurationProvider(Provider):
	def __init__(self, config_path: str):
		self.factory = ConfigFactory(config_path)
		self.config = self.factory.create_config()

	def get_instance(self) -> Dict[Any, Any]:
		return self.config.get_loaded_config()
