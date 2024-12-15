from abc import ABC, abstractmethod
from typing import Any, Callable

from echonextdi.providers.provider import Provider


class AbstractProduct(ABC):
	"""
	This class describes an abstract product.
	"""

	def call(self) -> Any:
		"""
		Call handler

		:returns:	result of handler
		:rtype:		Any
		"""
		raise NotImplementedError


class Product(AbstractProduct):
	"""
	This class describes a product.
	"""

	def __init__(self, handler: Callable):
		"""
		Constructs a new instance.

		:param		handler:  The handler
		:type		handler:  Callable
		"""
		self.handler = handler

	def call(self) -> Any:
		"""
		Call handler

		:returns:	result of handler
		:rtype:		Any
		"""
		return self.handler()


class AbstractFactory(ABC):
	"""
	Front-end to create abstract objects.
	"""

	@abstractmethod
	def get_product(self) -> AbstractProduct:
		"""
		Gets the product.

		:returns:	The product.
		:rtype:		AbstractProduct
		"""
		raise NotImplementedError


class ProductFactory(AbstractFactory):
	"""
	Front-end to create product objects.
	"""

	def __init__(self, handler: Callable):
		"""
		Constructs a new instance.

		:param		handler:  The handler
		:type		handler:  Callable
		"""
		self.product = Product(handler)

	def get_product(self) -> Any:
		"""
		Gets the product.

		:returns:	The product.
		:rtype:		Any
		"""
		return self.product.call()


class FactoryProvider(Provider):
	"""
	This class describes a factory provider.
	"""

	def __init__(self, handler: Callable):
		"""
		Constructs a new instance.

		:param		handler:  The handler
		:type		handler:  Callable
		"""
		self.factory = ProductFactory(handler)

	def get_instance(self) -> Any:
		"""
		Gets the instance.

		:returns:	The instance.
		:rtype:		Any
		"""
		return self.factory.get_product()
