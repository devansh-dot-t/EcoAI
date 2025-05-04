from flask import Flask, render_template, request
from utils.carbon_predictor import predict_carbon

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    tips = []
    transport = energy = meat = 0
    transport_pct = energy_pct = meat_pct = 0

    if request.method == "POST":
        try:
            transport = float(request.form['transport'])
            energy = float(request.form['energy'])
            meat = float(request.form['meat'])
            data = [transport, energy, meat]

            prediction = predict_carbon(data)

            total = transport + energy + meat
            if total > 0:
                transport_pct = round((transport / total) * 100)
                energy_pct = round((energy / total) * 100)
                meat_pct = round((meat / total) * 100)

        except ValueError:
            prediction = "Invalid input!"

    return render_template(
        "dashboard.html",
        prediction=prediction,
        tips=tips,
        transport=transport,
        energy=energy,
        meat=meat,
        transport_pct=transport_pct,
        energy_pct=energy_pct,
        meat_pct=meat_pct
    )

if __name__ == "__main__":
    app.run(debug=True)