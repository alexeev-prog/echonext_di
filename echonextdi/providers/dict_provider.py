from typing import Any, Dict

from echonextdi.providers.provider import Provider


class DictProvider(Provider):
	"""
	This class describes an dict provider.
	"""

	def __init__(self, dictionary: Dict[Any, Any]):
		"""
		Constructs a new instance.

		:param      dictionary:  The dictionary
		:type       dictionary:  { type_description }
		"""
		self.dictionary = dictionary

	def append_item(self, key: Any, value: Any):
		"""
		Appends an item.

		:param      item:  The item
		:type       item:  Any
		"""
		self.dictionary[key] = value

	def get_instance(self) -> Any:
		"""
		Gets the instance.

		:returns:	The instance.
		:rtype:		Any
		"""
		return self.dictionary
