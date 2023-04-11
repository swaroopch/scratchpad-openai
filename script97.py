import pydantic
from marvin import ai_fn


class Person(pydantic.BaseModel):
    name: str
    age: int


@ai_fn
def random_people(n: int) -> list[Person]:
    """
    """


if __name__ == "__main__":
    print(random_people(3))
