from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from schema import schema

app = FastAPI()

# Create a GraphQL router
graphql_app = GraphQLRouter(schema)

# Add the GraphQL route to FastAPI
app.include_router(graphql_app, prefix="/graphql")


@app.get("/")
def read_root():
    return {"message": "Welcome to AimCooking"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
