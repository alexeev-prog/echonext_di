from typing import Any, List

from echonextdi.providers.provider import Provider


class ListProvider(Provider):
	"""
	This class describes an list provider.
	"""

	def __init__(self, datalist: List[Any]):
		"""
		Constructs a new instance.

		:param      datalist:  The datalist
		:type       datalist:  List[Any]
		"""
		self.datalist = datalist

	def append_item(self, item: Any):
		"""
		Appends an item.

		:param      item:  The item
		:type       item:  Any
		"""
		self.datalist.append(item)

	def get_instance(self) -> Any:
		"""
		Gets the instance.

		:returns:	The instance.
		:rtype:		Any
		"""
		return self.datalist
