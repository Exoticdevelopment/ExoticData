from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['datafile']
    if not file:
        return "No file"

    # Lee el archivo en un DataFrame de pandas
    df = pd.read_csv(file)

    # Realiza algún análisis, por ejemplo, calcula estadísticas descriptivas
    description = df.describe().to_html()

    # Prepara los datos para el gráfico (usando una columna de ejemplo)
    column_name = df.columns[0]  # Usa la primera columna del DataFrame como ejemplo
    data = df[column_name].value_counts().to_dict()  # Cuenta los valores únicos
    labels = list(data.keys())
    values = list(data.values())

    return render_template('index.html', tables=[description], labels=labels, values=values)

if __name__ == '__main__':
    app.run(debug=True)
