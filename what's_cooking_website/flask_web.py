from flask import Flask, request, render_template
import pickle
import pandas as pd
import os
import nltk

app = Flask(__name__)

class ModelFile():
    model_file = os.listdir("models")[0]

model_manager = ModelFile()

if not os.path.isdir("templates"):
    os.mkdir("templates")
if not os.path.isdir("models"):
    os.mkdir("models")

@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == 'POST' and request.form :
        model_manager.model_file = request.form['model']
    elif (request.method == 'GET' and request.args):
        inputs = [
            str(request.args["search"])
        ]
        #change filename to change model to load up
        with app.open_resource("models/"+model_manager.model_file, "rb") as f:
            model = pickle.load(f)
        has_proba = hasattr(model, 'predict_proba')
        print(has_proba)
        if has_proba:
            probabilities = pd.DataFrame(model.predict_proba(inputs)*100, columns=model.classes_, index=["probs"]).T.sort_values(["probs"], ascending=False).head(4)
            output_probability = probabilities.values.max()
            output = probabilities.index[0]
            print(probabilities)
        else:
            probabilities = pd.DataFrame()
            output_probability = "None"
            output = model.predict(inputs)[0]
        if (output == "southern_us"):
            output = "south american"
        elif (output == "cajun_creole"):
            output = "cajun-creole"
        return render_template("index.html", model=model_manager.model_file, resp=output, resp_proba=output_probability, a="Other possible values are:", x=probabilities.iloc[1:], ser=True, allow_prob=has_proba)
    return render_template("index.html", model=model_manager.model_file, resp="", resp_proba="", a="", x="", ser=False, allow_prob=True)


@app.template_filter('format_perc')
def format_perc(value):
    if value:
        return '{:.2f}%'.format(value)
    return ""

@app.route("/admin")
def admin():
    models = list()
    for m in os.listdir("models"):
        models.append(m)
    return render_template("admin.html", models=models)