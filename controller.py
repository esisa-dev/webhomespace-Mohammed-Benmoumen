from flask import(
    Flask,
    request,
    render_template,
    redirect,
    session,
    url_for,
)
from datetime import datetime
import hashlib
app=Flask(__name__)
from dal import dao

def generate_key(login):
    return hashlib.md5(str(login).encode('utf-8')).hexdigest()
app.secret_key='1234'
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login',methods=['POST'])
def login():
    login=request.form['login']
    pwd=request.form['password']
  
    if dao.authenticate(login,pwd):
        app.secret_key=generate_key(login)
        response=app.make_response(render_template('app.html'))
        session['user_id']=login
        response.set_cookie('access_time',str(datetime.now()))
        
        return response
    else:
        return render_template('index.html',error_auth='login or password incorrect')
    
@app.route('/dir/<path:p_path>')
def dir(p_path):
    pass

@app.route('/logout')
def logout():
    session.pop('user_id',None)
    return redirect('/')

if __name__=='__main__':
    dao=dao()
    app.run(host="0.0.0.0",port=9090,debug=True)