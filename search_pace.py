from flask import Flask, render_template, request
import datetime
from vdot import find_vdot # импотр функции поиска VDOT
from list_vdot import km_5, km_10 # импорт списков времени прохождения дистанции в зависимости от VDOT


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
    hr = requst.form['hr'] # часы
    mt = requst.form['mt'] # минуты
    sc = requst.form['sc'] # секунды
    s = requst.form['s'] # дистанция
    #finish = datetime.timedelta(hours = 0, minutes = 62, seconds = 1) # данные от пользователя
    #s = '10km' # 10km - получить от пользователя
    dist = {'5km':km_5, '10km':km_10}
    #return find_vdot(finish, dist[s]) # list_vdot.km_10 список времен финиширования
    return render_template('results.html', the_hr=hr, the_mt=mt, the_sc=sc, the_s=s, the_title=title)

app.run()
