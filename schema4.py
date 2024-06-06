import typing as ty
import strawberry
import asyncio

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "world"
    
@strawberry.type
class Subscription:
    @strawberry.subscription
    async def count(self, target: int = 100) -> ty.AsyncGenerator[int, None]:
        for i in range(target):
            yield i
            await asyncio.sleep(0.5)

schema = strawberry.Schema(query=Query, subscription =Subscription)