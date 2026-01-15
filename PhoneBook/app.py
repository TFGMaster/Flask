from flask import Flask, render_template, request
import json
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')#here we link our HTML file using 'render_template'. but remember one thing the 'templaet' folder name should be without any spelling mistake.

@app.route('/submit', methods=['GET','POST'])# *Note: the name'submit',ha same asla pahije jo aapun HTML form madhi deu.
def add_contact():#function name should be any thing. for now its 'submit' we can also give 'XYZ'
    if request.method == 'POST':
        name = request.form['Name']#when we 'get' the 'Name' jo HTML form madhun yetoy to same letters madhi pahije with case sencetivity. nahi ter error ny det pan 'None' show karto.
        phone = request.form['ContactNum']#Hy variable la kay pan naav deu shakto(eg.'Contacts').
        
        try:#this is for handeling error's in code but there is one more very big reason to use this 'try-catch' block. is acording to our functionality we need to store data in sequance for that we need this. so our app read the file and gess the next sequance(eg.contact1,contact2...)
            with open('contacts.txt', 'r') as f:
                Contacts = json.load(f)
        except:#if we found '.txt' file empty then we can go with empty file.
            Contacts={}

        new_key = f"contact{len(Contacts)+1}"#format of storing data in .txt file.
        Contacts[new_key]={
            "name":name,
            "phone":phone
        }
        with open('contacts.txt', 'w') as f:
            json.dump(Contacts,f,indent=2)#dum meansp(push in .txt file)
        
        return render_template('add.html', user=name, num=phone)#hite je variable's use kelet(user,num) he tikadche nave aahet ji 'add.html' file madhi diliet(all this for testing).
    
    return render_template("home.html")
         