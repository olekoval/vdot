from flask import Flask, render_template, request
import datetime
from vdot import find_vdot # импотр функции поиска VDOT
from list_vdot import pace, dist, km_5, km_10
# импорт словарей pace, dist
# импортт списков km_5, km_10

app = Flask(__name__)

@app.route('/')

@app.route('/entry')
def entry_page() -> 'html':
    """        
    отображение формы ввода данных - entry.html с дальнейшей передачей данных по методу
    POST из формы на URL '/searhvdot' для вывода темпов тренировок
    return render_template('entry.html', the_title='Определение темпа')
    """
    return render_template('entry.html', the_title='YES')


@app.route('/searchvdot', methods=['POST'])
def do_search() ->'html':
    title = 'Результаты расчета'
    hr = request.form['hr'] # часы
    mt = request.form['mt'] # минуты
    sc = request.form['sc'] # секунды
    s = request.form['s'] # дистанция
    finish = datetime.timedelta(hours = int(hr), minutes = int(mt), seconds = int(sc)) # время завершения дистанции     
    vdot = str(find_vdot(finish, dist[s]))
    the_e = pace[vdot]['e'] # pace easy
    the_m = pace[vdot]['m'] # pace marathon
    the_t400 = pace[vdot]['t400'] # pace threshold 400m
    the_t1000 = pace[vdot]['t1000'] # pace threshold 1000m
    the_i400 = pace[vdot]['i400'] # pace interval 400m
    the_i1000 = pace[vdot]['i1000'] # pace interval 1000m
    the_i1200 = pace[vdot]['i1200'] # pace interval 12000m
    the_r200 = pace[vdot]['r200'] # pace repetition 200m
    the_r400 = pace[vdot]['r400'] # pace repetition 400m 
    the_r800 = pace[vdot]['r800'] # pace repetition 800m    
    return render_template('pace.html', the_e, the_m, the_t400,
                           the_t1000, the_i400, the_i1000, the_i1200,
                           the_r200, the_r400, the_r800, the_title=title)
app.run()
