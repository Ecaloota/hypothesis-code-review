from pydantic import ValidationError
from hypothesis import given, example, settings

from strategies import *
from main import MyPydanticModel
import pytest


@given(valid_model())
@settings(max_examples=100)
def test_create_with_valid_input(data):

    MyPydanticModel(**data)


@given(invalid_model())
@example({})
def test_cannot_create_with_invalid_input(data):

    # try:
    #     MyPydanticModel(**data)
    # except ValidationError:
    #     pass

    with pytest.raises(ValidationError):
        MyPydanticModel(**data)
