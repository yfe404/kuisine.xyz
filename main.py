import json

from jinja2 import Environment, FileSystemLoader, select_autoescape
env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

data = json.load(open("dataset/full_format_recipes.json", "r"))
for idx, recipe in enumerate(data):
    recipe["href"] = f"./recipes/{idx+1}.html"

template = env.get_template('index.html')


with open("index.html", "w") as f:
    f.write(template.render(recipes=data))


template = env.get_template('recipe.html')

for idx, recipe in enumerate(data):
    with open(f"recipes/{idx+1}.html", "w") as f:
        f.write(template.render(recipe=recipe))
