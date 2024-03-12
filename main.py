from veny.database import Database
from helper.WriteAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()


def getPokemonByName(name: str):
    return db.collection.find({"name": name})

pikachu = getPokemonByName("Pikachu")
writeAJson(pikachu, "pikachu")

pokemons = db.collection.find({"$or": [{"type":"Fire"},{"weaknesses": "Fire"}]})

tipos = ["Grass", "Poison"]
pokemons = db.collection.find({ "type": {"$in": tipos}, "next_evolution": {"$exists": True} })
writeAJson(pokemons, "tipos")

fraquezas = ["Psychic", "Ice"]
pokemons = db.collection.find({"weaknesses": {"$all": fraquezas}})
writeAJson(pokemons, "fraquezas")

pokemons = db.collection.find({"spawn_chance": {"$gt": 0.3, "$lt": 0.6}})
writeAJson(pokemons, "spawn_chance")

pokemons = db.collection.find({"multipliers": None})
writeAJson(pokemons, "multipliers")