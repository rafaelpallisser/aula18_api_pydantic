from pydantic import BaseModel

class PokemonSchema(BaseModel): # contrato de dados, schema de dados, a view da minha API
    name: str
    type: str

    class Config:
        from_attributes = True