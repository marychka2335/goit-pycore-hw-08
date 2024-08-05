def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return f"Ошибка ключа: {str(e)}"
        except ValueError as e:
            return f"Ошибка значения: {str(e)}"
        except IndexError:
            return "Недостаточно аргументов."
    return inner