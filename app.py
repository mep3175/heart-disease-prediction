from flask import Flask, request, render_template
from prediction_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            data = CustomData(
                age=request.form["age"],
                sex=request.form["sex"],
                cp=request.form["cp"],
                trestbps=request.form["trestbps"],
                chol=request.form["chol"],
                fbs=request.form["fbs"],
                restecg=request.form["restecg"],
                thalach=request.form["thalach"],
                exang=request.form["exang"],
                oldpeak=request.form["oldpeak"],
                slope=request.form["slope"],
                ca=request.form["ca"],
                thal=request.form["thal"]
            )
            df = data.get_data_as_dataframe()
            prediction = PredictPipeline().predict(df)
            result = "Likely Heart Disease" if prediction[0] == 1 else "No Significant Risk"
            return render_template("result.html", final_result=result)
        except Exception as e:
            return render_template("error.html", error_message=str(e))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
