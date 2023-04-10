import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            max_tokens = 3000,
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Suggest four names that is a superhero name for a specific animal.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline, TheKittyDestroyer
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot, Kyripto
Animal: {}
Names:""".format(
        animal.capitalize()
    )
