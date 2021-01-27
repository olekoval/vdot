from flask import Flask, render_template, request
import datetime
from vdot import find_vdot # импотр функции поиска VDOT
from list_vdot import dist, km_5, km_10 # импорт списков времени прохождения дистанции
                                        # в зависимости от VDOT

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


@app.route('/searchdot', methods=['POST'])
def do_search() ->'html':
    title = 'Результаты расчета'
    hr = request.form['hr'] # часы
    mt = request.form['mt'] # минуты
    sc = request.form['sc'] # секунды
    s = request.form['s'] # дистанция
    finish = datetime.timedelta(hours = int(hr), minutes = int(mt), seconds = int(sc)) # время завершения дистанции     
    vdot = find_vdot(finish, dist[s])
    
    
    #return render_template('results.html', the_hr=hr, the_mt=mt, the_sc=sc, the_s=s, the_title=title)

app.run()
