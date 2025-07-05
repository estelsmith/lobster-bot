from typing import Any, Callable

from app.ioc import ReadableContainer

class NotExtendableException(Exception):
    """
    Exception generated when a service is not extendable for any reason.
    """
    pass

class Container(ReadableContainer):
    """
    Dependency Injection container allowing to register() and get() services, as well as some helper methods to determine
    how services and values should be registered.
    """

    def register(self, name, value):
        """
        Register a service by name.
        """
        self._values[name] = value
        pass

    def share(self, value):
        """
        Wrap a service definition in a lambda to ensure the same copy of the service is generated every time.
        """
        instance = None

        def inner(*args, **kwargs):
            nonlocal instance
            instance = instance if instance is not None else value(*args, **kwargs)
            return instance

        return inner

    def protect(self, value):
        """
        Ensure a callable does not get interpreted as a service definition. Useful when raw callables need to be passed
        as service parameters.
        """
        def inner():
            return value

        return inner

    def extend(self, name, value: Callable[[Any], Any]):
        """
        Extends a service definition by being able to modify it after its initial creation.
        """
        old_service = self.raw(name)

        if not callable(old_service):
            raise NotExtendableException(f'Service {name} is not callable')

        self._values[name] = lambda: value(old_service())
