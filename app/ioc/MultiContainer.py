from typing import Optional

from app.ioc import Container, NotFoundException, ReadableContainer

class ContainerAlreadyAddedException(Exception):
    """Exception thrown when the container being attached already exists."""
    pass

class MultiContainer(ReadableContainer):
    """
    Pull from multiple DI containers instead of just a single one, allowing for composing more complex containers from a
    collection of simpler ones
    """

    def __init__(self, containers: Optional[list[Container]] = None):
        super().__init__()
        self._containers: list[Container] = containers if containers else []

    def attach(self, container: Container):
        """Attach container to instance, allowing it to be referenced when resolving services."""
        if container in self._containers:
            raise Exception('Container already attached')

        self._containers.append(container)

    def raw(self, name):
        """
        Search each container for the first matching service.
        """
        last = self._containers[:-1]

        for container in self._containers:
            try:
                return container.get(name)
            except NotFoundException as e:
                if container is last:
                    raise e

        raise NotFoundException(f'Service "{name}" not registered')
