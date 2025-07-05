class NotFoundException(Exception):
    """Exception thrown when a given service definition does not exist"""
    pass

class ReadableContainer:
    """
    Container that can be read from but not modified.
    """
    def __init__(self):
        self._values = {}

    def raw(self, name):
        """
        Retrieve a raw service definition if it exists.
        """
        if name not in self._values:
            raise NotFoundException(f'Service "{name}" not registered')
        return self._values.get(name)

    def get(self, name):
        """
        Resolve a service definition and return it.
        """
        service = self.raw(name)
        return service if not callable(service) else service()
