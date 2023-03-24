from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))

import random
import json


camp_no= ("SPRING","WINTER","SUMMER","FALL")
region=("ONTARIO","QUEBEC","NOVA SCOTIA","NB","BRITISH COLOMBIA")
Department=("IT","Finance","HR","Marketing","Manufacturing","Customer Service")
Year=(2018,2019,2020,2021,2022)
loyalty_lev=("High","Intermeddiate","Low")

mar_data= list()
def marketing_data(points=200):
    for i in range(points):
        cno=random.choice(camp_no)
        rg=random.choice(region)
        yr=random.choice(Year)
        lfs=random.random()*4
        cost_year= random.randint(10000,500000)
        cus_value=random.randint(5000,60000)
        tra=random.randint(1000000,10000000)
        lead= random.randint(1000,1000000)
        tot_mention=random.randint(10000,100000000)
        my_mention=random.randint(1000,10000)
        obj={
            "YEAR":yr,
        "REGION":rg,
        "CAMPAIGN":cno,
        "COST/YEAR":cost_year,
        "TRAFFIC":tra,
        "LEADS":lead,
        "TOTAL MENTIONS":tot_mention,
        "RIVEAN MENTIONS":my_mention,
        "CUSTOMER VALUE":cus_value,
        "Lifespan":lfs

        }
        mar_data.append(obj)
    return mar_data

hr_data=list()
import datetime
def hr_data():
    for i in Year:
        for j in Department:
            start_date = datetime.date(year=i, month=1, day=1)
            emp_end=random.randint(200,1000)  
            emp_st= random.randint(200,1000)
            emp_lft=random.randint(0,abs(emp_end-emp_st))
            avg_fill_time=random.randint(7,365)
            tot_re=random.randint(200,1000)
            pos_re=random.randint(200,tot_re)
            cos_train=random.randint(1000,5000)
            obj={
                "YEAR":i,
            "DEPARTMENT":j,
            "EMPLOYEES AT START OF YEAR":emp_st,
            "EMPLOYEES AT END OF YEAR":emp_end,
            "EMPLOYEE FIRED":emp_lft,
            "FILL TIME":avg_fill_time,
            "POSITIVE REVIEW":pos_re,
            "TOTAL REVIEW":tot_re,
            "COST TO TRAIN":cos_train
            }
            hr_data.append(obj)
        return hr_data


cs_data=list()
def cs_data(points=20):
    for i in range(points):
        loyno=random.choice(loyalty_lev)
        rg=random.choice(region)
        call=random.randint(0,1)
        if call:
            aba_call=random.randint(0,1)
        else:
            aba_call=0
        satisfaction_score=random.randint(0,10)
        talk_time=random.randint(0,120)
        hold_time=random.randint(0,60)
        aftercall=random.randint(0,200)
        obj={"LOYALTY":loyno,
             "REGION":rg,
             "NUMBER OF CALLS":call,
             "ABANDONED CALL":aba_call,
             "SATISFACTION":satisfaction_score,
             "TALK TIME":talk_time,
             "HOLD TIME":hold_time,
             "AFTER CALL TIME":aftercall
        }
        cs_data.append(obj)
    return cs_data



man_data=list()
def manufacturing_data(points=20): 
    for i in range(points):
        yr=random.choice(Year)
        lab_cost=random.randint(10,30)
        isdefetive=random.randint(0,1)
        ontime=random.randint(0,1)
        pro_time=random.randint(70,200)
        rg=random.choice(region)
        obj={
            "Year":yr,
            "Region":rg,
            "IS-defective":isdefetive,
            "ON-Time_delivery":ontime,
            "Labour-cost":lab_cost,
            "Product-development-time":pro_time,

        }
        man_data.append(obj)
    return man_data

url_mark="C:/Users/aniru/Desktop/visual/marketing.json"
url_hr="C:/Users/aniru/Desktop/visual/hr.json"
url_cs="C:/Users/aniru/Desktop/visual/cs.json"
url_manufacture="C:/Users/aniru/Desktop/visual/manufacturing.json"

def obj_list_json(mar_data,url="",update=False):
    if(update):
        with open(url, 'r') as f:
            up_data = json.load(f)
            mar_data.append(up_data)
        markjson=json.dumps(mar_data)
        f = open(url, "w")
        f.write(markjson)
        f.close()
        print( markjson)

@app.route("/aa")
def home_view():
        return "<h1>Welcome to My api</h1>"
@app.route("/marketing")
def mar_d():
     jdata= marketing_data(20)
     return jdata
@app.route("/hr")
def hr_d():
     jdata= hr_data()
     return jdata
@app.route("/manufacturing")
def man_d():
     jdata= manufacturing_data(20)
     return jdata
@app.route("/cs")
def cs_d():
     jdata= cs_data(20)
     return jdata
if __name__ == "__main__":
        app.run()