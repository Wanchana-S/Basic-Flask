from flask import Flask, render_template,request,session,flash
from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, SubmitField,BooleanField,SelectField,TextAreaField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'myKey'
Bootstrap(app)

class MyForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired()])
    gender = RadioField('เลือกเพศ', choices=[('M','ชาย'), ('F','หญิง')], default='M')
    skill = SelectField('ความสามารถพิเศษ',choices=[('พูดภาษาอังกฤษ','พูดภาษาอังกฤษ'),('ร้องเพลง','ร้องเพลง'),('เขียนเกมส์','เขียนเกมส์')])
    address = TextAreaField('ที่อยู่ของคุณ')
    isAccept = BooleanField('I accept the terms and conditions')
    submit = SubmitField('Submit')

@app.route('/')
def index():
    data = {
        'name': 'Wanchana',
        'age': 29,
        'salary': '5000'
    }
    return render_template('index.html', data=data)

@app.route('/wtf',methods=['GET', 'POST'])
def indexwtf():
    form = MyForm()
    if form.validate_on_submit():
        flash("บันทึกข้อมูลเรียบร้อย")
        session['name'] = form.name.data
        session['gender'] = form.gender.data
        session['skill'] = form.skill.data
        session['address'] = form.address.data
        session['isAccept'] = form.isAccept.data
        # ลบข้อมูลจากแบบฟอร์ม
        form.name.data = ''
        form.isAccept.data = ''
        form.gender.data = ''
        form.address.data = ''
    return render_template('indexwtf.html', form=form)


@app.route('/about')    
def about():
    products = ('iPhone 14', 'iPad Pro', 'MacBook Pro')
    return render_template('about.html', products=products)

@app.route('/admin')
def admin():
    # ชื่อ,อายุ
    username = "Solo"
    # ส่งข้อมูลไปยัง template   
    return render_template('admin.html', username=username)

@app.route('/sendData')
def signupForm():
    request_data = request.args
    name = request_data.get('name')
    email = request_data.get('email')
    description = request_data.get('description')
    return render_template('thankyou.html', data={"name": name, "email": email, "description": description})


if __name__ == '__main__':
    app.run(debug=True)