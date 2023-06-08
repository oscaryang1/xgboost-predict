
from flask import Flask,request,render_template,redirect

from os import environ

from predict import predict

name_all=" "
path=r"D:\xgboost_gui\FlaskWebProject1\\"
app = Flask(__name__,template_folder=path+'templates',static_folder=path+'static',static_url_path="")
@app.route('/')
def index():
    return render_template('sub.html',data1=23.03,data2=1,data7=257.5,data3=2,data4=2,data5=2,data6=3,
                             data8=53.7,data9=8,data10=1.63,data11=26.135)
 
global p,data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11

@app.route('/resuslt2', methods=['post'])

def resuslt2():
    global p,data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11
    data1 = float(request.form.get('data1'))
    data2 = int(request.form.get('data2'))
    data3 = int(request.form.get('data3'))
    data4 = int(request.form.get('data4'))
    data5 = int(request.form.get('data5'))
    data6= int(request.form.get('data6'))
    data7= float(request.form.get('data7'))
    data8 = float(request.form.get('data8'))
    data9 = float(request.form.get('data9'))
    data10 =float( request.form.get('data10'))
    data11 = float(request.form.get('data11'))
    p=predict([[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11]])
   # print(p,"fasfas")
    return   render_template('sub.html',data1=data1,data2=data2,data7=data7,data3=data3,data4=data4,data5=data5,data6=data6,
                             data8=data8,data9=data9,data10=data10,data11=data11,flag=1)
   

@app.route('/resuslt', methods=['post'])

def resuslt():
  
    return render_template('sub.html',predict=p[0],data1=data1,data2=data2,data7=data7,data3=data3,data4=data4,data5=data5,data6=data6,
                             data8=data8,data9=data9,data10=data10,data11=data11,)
  


 
if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
