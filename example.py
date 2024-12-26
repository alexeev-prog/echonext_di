from echonextdi.containers.container import Container
from echonextdi.depends import Depends
from echonextdi.providers.callable_provider import CallableProvider


def sqrt(a: int, b: int = 2):
	return a**b


class SQRT_Dependency:
	def __init__(self, sqrt):
		self.sqrt = sqrt


container = Container()
container.register("sqrt", CallableProvider(sqrt))


def calculate(number: int, depend: Depends = Depends(container, SQRT_Dependency)):
	print(f"{number} ^2 = {depend().sqrt(2)}")


calculate(4)
