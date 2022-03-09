from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class MaxFileSizeInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.__mb_to_bytes(self.max_size):
            raise ValidationError(f'File size must be less than {self.max_size}!')

    @staticmethod
    def __mb_to_bytes(value):
        return value * 1024 * 1024
