from fastapi import FastAPI
from graphene import ObjectType, String, Schema
from strawberry.asgi import GraphQL

app = FastAPI()

class Query(ObjectType):
    hello = String(name=String(default_value="world"))

    def resolve_hello(self, info, name):
        return f'Hello {name}!'

schema = Schema(query=Query)

app.add_route("/graphql", GraphQL(schema=schema))

@app.get("/")
def read_root():
    return {"message": "Welcome to AimCooking"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
