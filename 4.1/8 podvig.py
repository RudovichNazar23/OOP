class Validator:
    def _is_valid(self, data):
        return True

    def __call__(self, *args, **kwargs):
        pass


class IntegerValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        return True if isinstance(data, int) and self.min_value <= data <= self.max_value else False

    def __call__(self, data, **kwargs):
        if not self._is_valid(data):
            raise ValueError('данные не прошли валидацию')
        else:
            return True


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        return True if isinstance(data, float) and self.min_value <= data <= self.max_value else False

    def __call__(self, data, **kwargs):
        if not self._is_valid(data):
            raise ValueError('данные не прошли валидацию')
        else:
            return True
