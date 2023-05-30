from flask import Flask,render_template,request
from flask_wtf import Form
from wtforms import StringField,SubmitField,IntegerField
from wtforms.validators import DataRequired


fai=Flask(__name__)


class WebForm(Form):
    name=StringField(validators=[DataRequired()])
    age=IntegerField()
    submit=SubmitField()

@fai.route('/WebForms',methods=['GET','POST'])
def WebForms():
    WFO=WebForm()
    if request.method=='POST':
        WFD=WebForm(request.form)
        if WFD.validate():
            return WFD.data

    return render_template('WebForms.html',WFO=WFO)


if __name__=='__main__':
    fai.run(debug=True)
