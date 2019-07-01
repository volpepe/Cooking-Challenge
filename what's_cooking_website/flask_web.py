from flask import Flask, request, render_template
import pickle
import pandas as pd
import os

#idea to have multiple models: make an object that is modified by one of these functions in the admin page

app = Flask(__name__)

if not os.path.isdir("templates"):
    os.mkdir("templates")

@app.route("/", methods=["GET"])
def predict():
    if (request.method == 'GET' and request.args):
        inputs = [
            str(request.args["search"])
        ]
        #change filename to change model to load up
        with app.open_resource("model_SVM.bin", "rb") as f:
            model = pickle.load(f)
        #output = model.predict(inputs)[0]
        probabilities = pd.DataFrame(model.predict_proba(inputs)*100, columns=model.classes_, index=["probs"]).T.sort_values(["probs"], ascending=False).head(4)
        output_probability = probabilities.values.max()
        output = probabilities.index[0]
        print(output)
        print(probabilities)
        if (output == "southern_us"):
            output = "south american"
        elif (output == "cajun_creole"):
            output = "cajun-creole"
        return render_template("index.html", resp=output, resp_proba=output_probability, a="Other possible values are:", x=probabilities.iloc[1:], ser=True)
    return render_template("index.html", resp="", resp_proba="", a="", x="", ser=False)


@app.template_filter('format_perc')
def format_perc(value):
    if value:
        return '{:.2f}%'.format(value)
    return ""