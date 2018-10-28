
class ServiceException(Exception):
    def __init__(self, description=None):
        self.description = description

    def __str__(self):
        return f'<Service exception: {self.description}>'


class RecordExistsException(ServiceException):
    def __init__(self, description=None):
        super().__init__(description=description)

    def __str__(self):
        return f'<RecordExistsException exception: {self.description}>'
