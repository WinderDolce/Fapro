from flask import Flask, request, jsonify
from requests_html import HTMLSession
from datetime import datetime

app = Flask(__name__)

def get_uf_url(date):
    """Genera la URL de la UF para una fecha dada."""
    year = date.year
    return f"https://www.sii.cl/valores_y_fechas/uf/uf{year}.htm"

@app.route('/api/uf/<int:day>-<int:month>-<int:year>', methods=['GET'])
def get_uf(day, month, year):
    """Obtiene el valor de la UF para una fecha dada."""
    try:
        # Validar fecha mínima
        min_date = datetime(2013, 1, 1)
        query_date = datetime(year, month, day)
        if query_date < min_date:
            raise ValueError("La fecha mínima de consulta es: 01-01-2013.")

        # Validar fecha máxima
        now = datetime.now()
        if query_date > now:
            raise ValueError("La fecha no puede ser futura.")

        # Obtener URL de la UF
        url = get_uf_url(query_date)

        # Consultar valor de la UF
        s = HTMLSession()
        r = s.get(url)
        r.raise_for_status() # Raise an exception if an HTTP error occurs

        # Extraer valor de la UF de la tabla
        table = r.html.find('table')[12]
        tabledata = [[c.text for c in row.find('td, th')[:-1]] for row in table.find('tr')][1:]
        tabledataHeader = [[c.text for c in row.find('th')[:-1]] for row in table.find('tr')][0]
        months = {'Ene': '01', 'Feb': '02', 'Mar': '03', 'Abr': '04', 'May': '05', 'Jun': '06',
                  'Jul': '07', 'Ago': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dic': '12'}
        data = {}
        for t in tabledata:
            if t[0] == str(day):
                for i in range(len(tabledataHeader)):
                    if tabledataHeader[i] == 'Día':
                        data[tabledataHeader[i]] = t[i]
                    else:
                        month_name = tabledataHeader[i].split('-')[-1]
                        month_num = months[month_name]
                        if month_num == str(month):
                            data[month_num] = t[i]
                            return jsonify(data)

        # No se encontraron datos para la fecha consultada
        return jsonify({'error': 'No se encontraron datos para la fecha solicitada.'}), 404

    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8080)
