from pydantic import BaseModel


class Ingredient(BaseModel):
    name: str
    quantity: str


class Recipe(BaseModel):
    title: str
    ingredients: list[Ingredient]
    instructions: str
    cuisine: str
