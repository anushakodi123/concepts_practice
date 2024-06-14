import strawberry

def get_name() -> str:
    return "Hello"


@strawberry.type
class Fruit:
    id: int
    name: str
    weight: float

@strawberry.input
class AddFruitInput:
    id: int
    name: str
    weight: float

@strawberry.type
class FruitMutations:
    @strawberry.mutation
    def add(self, info, input: AddFruitInput) -> Fruit:
        fruit = Fruit(id= input.id, name= input)

    @strawberry.mutation
    def update_weight(self, info, input: UpdateFruitWeightInput) -> Fruit: ...


@strawberry.type
class Mutation:
    @strawberry.field
    def fruit(self) -> FruitMutations:
        return FruitMutations()