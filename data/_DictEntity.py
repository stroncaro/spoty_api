# TODO: Write proper tests using a test framework

from typing import Dict, Type, TypeVar

from ..exceptions import InvalidDictException

T = TypeVar("T", bound="DictEntity")


class DictEntity:
    """
    Base class for creating instances from a dictionary.

    Classes inheriting from DictEntity can define attributes with type annotations,
    and their constructor will automatically accept a dictionary of string values.
    These values will be converted to the specified types and assigned to the attributes.

    Attributes:
        _original_data (Dict[str, str]): The original dictionary used to create the instance.
    """

    _original_data: Dict[str, str]

    def __init__(self, *, data: Dict[str, str]) -> None:
        """
        Initialize instance from given data, validating it first.

        Args:
            data (Dict[str, str]): A dictionary containing the required fields.

        Raises:
            InvalidDictException: If any required fields are missing.
        """

        self.__class__._validate_data(data)

        for field, type in self.__class__.__annotations__.items():
            setattr(self, field, type(data[field]))
        self._original_data = data

    @classmethod
    def _validate_data(cls: Type[T], data: Dict[str, str]) -> None:
        """
        Validate that all required fields, based on the class annotations, are present in the given data.

        Args:
            data (Dict[str, str]): A dictionary to validate.

        Raises:
            InvalidDictException: If any required fields are missing.
        """

        required_fields = cls.__annotations__.keys()
        missing_fields = [
            field for field in required_fields if field not in data.keys()
        ]
        if missing_fields:
            raise InvalidDictException(
                f"Missing required fields: {', '.join(missing_fields)}"
            )


if __name__ == "__main__":

    class Thing(DictEntity):
        """Example subclass with specific attributes."""

        name: str
        purpose: str
        age: int

    # Example usage
    data = {"name": "ball", "purpose": "bounce", "age": "13"}
    thing = Thing(data=data)

    try:
        assert thing.name == "ball"
        assert thing.purpose == "bounce"
        assert thing.age + 3 == 16
    except AssertionError as error:
        print("DictEntity not working correctly")
        print(error)
        exit(1)

    print("DictEntity working as intended.")
