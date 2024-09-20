class Country():
    def __init__(self, name: str, code: str) -> None:
        self.name = name
        self.code = code

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Country):
            return False
        return self.name == value.name and self.code == value.code