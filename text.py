import joblib
from flask import Blueprint, render_template, request

# TODO
# Eingabefelder eintragen [Feldname, Labeltext]
fields = [['field1', 'Labeltext1'], ['field2', 'Labeltext2']]

# TODO
# Name des Modells festlegen
model_file = 'qm_model.dt'

textki = Blueprint('textki', __name__)


@textki.route('/text', methods=['GET'])
def text_get():
    return render_template('text.html', inputfields=fields)


@textki.route('/text', methods=['POST'])
def text_post():
    # TODO
    # Daten aus Form Request laden, evtl. konvertieren
    # Ergebnis ins Array input_values
    input_values = []
    for input_field in fields:
        if input_field[0] in request.form.keys():
            input_values.append(float(request.form.get(input_field[0])))
    # TODO
    # Model mit Daten aufrufen
    model = joblib.load(model_file)
    result = model.predict([input_values])

    # TODO
    # Ergebnis für Ausgabe vorbereiten
    # result = result ...
    if result == 'N':
        result = "Nacharbeit"
    else:
        result = "Ausschuss"

    return render_template('text.html', inputfields=fields, result=result)
