from .exceptions import InvalidInputError

class ValidateInputMixin:
    def validate_input(self, input_options):
        while True:
            try:
                user_input = input(input_options)
                if not user_input.isdigit():
                    raise InvalidInputError("Error: Wrond data entered. Try again.")
                option = int(user_input)
                if option < 1 or option > 3:
                    raise InvalidInputError("Error: Wrond number entered. Try again.")
                return option
            except InvalidInputError as e:
                print(e)


class Round_Counter:
    def __init__(self):
        self._value = 1

    def increase_round_number(self):
        self._value += 1
        return self._value
