# Pandas and AWS Lambda

Appending your `lambda_function.py` to the deployment zip bundle

```sh
zip -g ./function.zip lambda_function.py
```

__Sample__

```python
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
```

__Resources__

Star Wars API: https://swapi.dev