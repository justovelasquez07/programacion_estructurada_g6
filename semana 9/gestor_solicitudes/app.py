
# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
import logica

app = Flask(__name__)
app.secret_key = "clave-local-practica-uam"


@app.get("/")
def inicio():
    return render_template(
        "index.html",
        pendientes=logica.cola_pendientes,
        historial=logica.pila_historial,
        siguiente=logica.consultar_siguiente(),
        estadisticas=logica.obtener_estadisticas()
    )


@app.post("/registrar")
def registrar():
    cliente = request.form.get("cliente", "")
    asunto = request.form.get("asunto", "")

    solicitud = logica.registrar_solicitud(cliente, asunto)

    if solicitud:
        flash("Solicitud registrada correctamente.", "success")
    elif not cliente.strip() or not asunto.strip():
        flash("Debes completar el cliente y el asunto.", "danger")
    else:
        flash("La solicitud ya está pendiente. No se registró un duplicado.", "warning")

    return redirect(url_for("inicio"))


@app.post("/atender")
def atender():
    solicitud = logica.atender_siguiente()

    if solicitud:
        flash(f'Solicitud #{solicitud["id"]} atendida.', "success")
    else:
        flash("No hay solicitudes pendientes.", "warning")

    return redirect(url_for("inicio"))


@app.post("/deshacer")
def deshacer():
    solicitud = logica.deshacer_ultima_atencion()

    if solicitud:
        flash(f'Solicitud #{solicitud["id"]} restaurada a pendientes.', "success")
    else:
        flash("No hay atenciones que deshacer.", "warning")

    return redirect(url_for("inicio"))


@app.get("/buscar")
def buscar():
    valor = request.args.get("id", "").strip()
    resultado = None
    error = None

    if valor:
        try:
            identificador = int(valor)

            if identificador < 1:
                error = "El ID debe ser un número positivo."
            else:
                resultado = logica.buscar_solicitud(identificador)

                if resultado is None:
                    error = "No se encontró una solicitud con ese ID."
        except ValueError:
            error = "El ID debe ser un número entero."

    return render_template(
        "index.html",
        pendientes=logica.cola_pendientes,
        historial=logica.pila_historial,
        siguiente=logica.consultar_siguiente(),
        estadisticas=logica.obtener_estadisticas(),
        busqueda=resultado,
        error_busqueda=error,
        id_busqueda=valor
    )


@app.post("/cancelar/<int:identificador>")
def cancelar(identificador):
    solicitud = logica.cancelar_solicitud(identificador)

    if solicitud:
        flash(f"Solicitud #{identificador} cancelada.", "success")
    else:
        flash("No existe esa solicitud pendiente o ya fue atendida.", "warning")

    return redirect(url_for("inicio"))


@app.post("/deshacer-varias")
def deshacer_varias():
    valor = request.form.get("cantidad", "").strip()

    try:
        cantidad = int(valor)

        if cantidad < 1:
            flash("La cantidad debe ser mayor que cero.", "danger")
        else:
            restauradas = logica.deshacer_varias(cantidad)
            flash(
                f"Se restauraron {len(restauradas)} solicitud(es).",
                "success" if restauradas else "warning"
            )
    except ValueError:
        flash("Introduce una cantidad entera válida.", "danger")

    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(debug=True)
