from flask import Blueprint, render_template, request, flash
from pandas_datareader import data
from bokeh.plotting import output_file, figure, show
import datetime
views = Blueprint('views',__name__)

@views.route('/')
def home():
    
    

    return render_template('base.html')


@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #start=datetime.datetime.strptime(request.form.get('start'), '%m/%d/%Y').strftime('%Y-%m-%d')
        #end=datetime.datetime.strptime(request.form.get('end'), '%m/%d/%Y').strftime('%Y-%m-%d')
        my_string = request.form['start']
        my_string2 = request.form['end']
        cname = request.form['cname']
        start = datetime.datetime.strptime(my_string, '%Y-%m-%d')
        end = datetime.datetime.strptime(my_string2, '%Y-%m-%d')
        if 0<1:
            
            f = data.DataReader(name = cname, data_source = 'yahoo', start = start, end = end)
            p = figure(width = 1250, height = 500, x_axis_type= "datetime") 
            p.line(f.index[1<f.Open], f["Close"], color = "Orange", alpha = 0.5)
            output_file("website/templates/working.html")
            show(p)
        
    """
    my_string = str(input('Enter Starting date date(yyyy-mm-dd): '))
    my_string2 = str(input('Enter Ending date date(yyyy-mm-dd): '))
    start = datetime.strptime(my_string, "%Y-%m-%d")
    end = datetime.strptime(my_string2, "%Y-%m-%d")
    #start = datetime.datetime(2018,1,1)
    #end = datetime.datetime(2018,2,2)
    f = data.DataReader(name = "GOOG", data_source = "yahoo", start = start, end = end)
    p = figure(width = 1250, height = 500, x_axis_type= "datetime") 
    p.line(f.index[1<f.Open], f["Close"], color = "Orange", alpha = 0.5)
    output_file("working.html")
    show(p)
    """
    return render_template('login.html')

