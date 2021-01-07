import pandas as pd
import json


def lambda_handler(event, context):
    df = pd.read_json("https://swapi.dev/api/planets")
    planets = pd.DataFrame(df["results"].to_list())

    # cleaning
    planets = planets.set_index("name")
    planets["population"] = pd.to_numeric(planets["population"], errors="coerce")

    # max pop
    print(planets[planets.population == planets.population.max()]["population"])

    return {"statusCode": 200, "body": "job completed"}
