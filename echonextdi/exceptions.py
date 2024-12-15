class ProviderNotFoundError(Exception):
	"""
	This class describes a provider not found error.
	"""

	pass


class DependencyCycleError(Exception):
	"""
	This class describes a dependency cycle error.
	"""

	pass


class DependencyNotFoundError(Exception):
	"""
	This class describes a dependency not found error.
	"""

	pass


class DependencyOverrideError(Exception):
	"""
	This class describes a dependency override error.
	"""

	pass


class DependencyAlreadyExistsError(Exception):
	"""
	This class describes dependency already exists.
	"""

	pass
