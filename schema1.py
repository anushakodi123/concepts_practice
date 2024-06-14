import strawberry
from typing import Union

# def get_name() -> str:
#     return "strawberry"


# @strawberry.type
# class Query:
#     name: str = strawberry.field(resolver=get_name)


# @strawberry.type
# class Query:
#     @strawberry.field
#     def name(self) -> str:
#         return "strawberry"


# schema = strawberry.Schema(query=Query)




FRUITS = [
    "Strawberry",
    "Apple",
    "Orange",
]

@strawberry.type
class Query:
    @strawberry.field
    def fruit(self, startswith: str ) -> Union[str, None]:
        for fruit in FRUITS:
            if fruit.startswith(startswith):
                return fruit
        return None

schema = strawberry.Schema(query=Query)



