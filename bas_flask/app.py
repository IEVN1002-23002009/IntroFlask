from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    nombre = ""
    cantidadCompradores = 1
    tarjetaCineco = "No"
    cantidadBoletas = 1
    valorAPagar = 0
    mensajeError = ""
    procesado = False

    if request.method == "POST":
        procesado = True
        nombre = request.form.get("nombre", "").strip()
        
        try:
            cantidadCompradores = int(request.form.get("cantidadCompradores", 1))
            cantidadBoletas = int(request.form.get("cantidadBoletas", 1))
        except ValueError:
            cantidadCompradores, cantidadBoletas = 1, 1

        tarjetaCineco = request.form.get("tarjetaCineco", "No")

        if not nombre:
            mensajeError = "Debes ingresar tu nombre."
        elif cantidadCompradores < 1 or cantidadBoletas < 1:
            mensajeError = "Las cantidades deben ser mayores que cero."
        elif cantidadBoletas > cantidadCompradores * 7:
            mensajeError = f"Máximo 7 boletas por comprador (Límite: {cantidadCompradores * 7})."
        else:
            valorAPagar = cantidadBoletas * 12
            
            if cantidadBoletas > 5:
                valorAPagar *= 0.85
            elif cantidadBoletas >= 3:
                valorAPagar *= 0.90
                
            if tarjetaCineco == "Si":
                valorAPagar *= 0.90

    return render_template(
        "cinepolis.html",
        nombre=nombre,
        cantidadCompradores=cantidadCompradores,
        tarjetaCineco=tarjetaCineco,
        cantidadBoletas=cantidadBoletas,
        valorAPagar=valorAPagar,
        mensajeError=mensajeError,
        procesado=procesado
    )

if __name__ == "__main__":
    app.run(debug=True)