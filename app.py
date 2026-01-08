#Simple login app(I'll use Vertual Envirement in this its not mendatory)
from flask import Flask, request, Response, url_for, redirect, session

app = Flask(__name__)
app.secret_key = "supersecret"#For using 'session' we have to give the secret key

@app.route('/', methods=['GET','POST'])#home page with 'get''post' methods. so we can 'send''received' data.
def login():
    if request.method == 'POST':#jar user ni data fill karun submit kela ter
        username = request.form.get('Username')#username store kara 
        password = request.form.get('Password')#pass store kara.

#note:sadhyla demo user create karun thevlay. testing sathi mainly varcha data DB store karun mag login karycha.
        if username == 'pratik' and password == '6352':#jar user 'pratik' aahe ani 'pass' barobar aahe ter
            session['user'] = username#store the info in session for that we allready created 'secretKey'
            return redirect(url_for('welcome'))#user la welcome page ver pathvla. *Note: the 'url_for' "name" should be same jo aapun ty functionla denar aahot.
        
        else: #jar 'ID''PASS' wrong asel ter
            return Response('Wrong user id or password', mimetype='text/plain')
  
  #I'll create demo HTML form here but we should create saperate HTML file.
    return '''
    <h2>Login Page</h2>
    <form method="POST">
        Username: <input type="text" name="Username"><br>
        Password: <input type="password" name="Password"><br>
        <input type="submit" value="Login">
    </form>
    '''

@app.route('/welcomePage')#this is the name appear in URL. 
def welcome():#this should same as 'url_for' "name". jy badel varti sangitlay wo hi.
    if 'user' in session:#jar usercha session create zaly.

#Same demo HTML for welcome page.      
        return f''' 
          <h2>Welcome {session['user']}</h2>
          <a href={url_for('logout')}>Logout</a>
        '''

    return redirect(url_for('login'))#jar user 'logout' karto ter. parat login page ver takayla


@app.route('/logoutPage')
def logout():
  session.pop('user', None)#user cha session close karyla 'POP' vaprto and to 'None' error presizely handel karyla thats'it.
  return redirect(url_for('login'))
