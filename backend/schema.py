import strawberry
from typing import List
from openai_client import suggest_recipes

# Mock database
recipes_db = []


@strawberry.type
class IngredientType:
    name: str
    quantity: str


@strawberry.type
class RecipeType:
    title: str
    ingredients: List[IngredientType]
    instructions: str
    cuisine: str


# Input types for mutations
@strawberry.input
class IngredientInput:
    name: str
    quantity: str


@strawberry.input
class RecipeInput:
    title: str
    ingredients: List[IngredientInput]
    instructions: str
    cuisine: str


@strawberry.type
class Query:
    @strawberry.field
    def recipes(self) -> List[RecipeType]:
        return recipes_db

    @strawberry.field
    def recipe_by_title(self, title: str) -> RecipeType:
        for recipe in recipes_db:
            if recipe.title == title:
                return recipe
        return None

    @strawberry.field
    def suggest_recipe(self, ingredients: List[str] = None, cuisine: str = None) -> str:
        return suggest_recipes(ingredients, cuisine)


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_recipe(self, recipe_data: RecipeInput) -> RecipeType:
        new_recipe = RecipeType(
            title=recipe_data.title,
            ingredients=recipe_data.ingredients,
            instructions=recipe_data.instructions,
            cuisine=recipe_data.cuisine,
        )
        recipes_db.append(new_recipe)
        return new_recipe


schema = strawberry.Schema(query=Query, mutation=Mutation)
