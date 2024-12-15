from typing import Callable

from echonextdi.containers.container import Container
from echonextdi.providers.callable_provider import CallableProvider
from echonextdi.providers.dict_provider import DictProvider
from echonextdi.providers.list_provider import ListProvider


class DynamicContainer(Container):
	"""
	This class describes a dynamic container.
	"""

	def register_callable(self, key: str, handler: Callable):
		"""
		Register callable handler

		:param		key:	  The key
		:type		key:	  str
		:param		handler:  The handler
		:type		handler:  Callable
		"""
		self.register(key, CallableProvider(handler))

	def register_dict(self, key: str, **kwargs):
		"""
		Register dictionary

		:param		key:	 The key
		:type		key:	 str
		:param		kwargs:	 The keywords arguments
		:type		kwargs:	 dictionary
		"""
		self.register(key, DictProvider(**kwargs))

	def register_list(self, key: str, *args):
		"""
		Register list

		:param		key:   The key
		:type		key:   str
		:param		args:  The arguments
		:type		args:  list
		"""
		self.register(key, ListProvider(*args))
