from flask import Flask,render_template,request


app=Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about')
def about_us():
    title='About Sathwik Reddy'
    names=['sathwik','bob','mr792','ms461']
    return render_template('about.html',names=names,title=title)


@app.route('/subscribe')
def subscribe():
    title='Subscribe To My News Letter'
    return render_template('subscribe.html',title=title)

@app.route('/form',methods=['POST'])
def form():
    first_name=request.form.get('first_name')
    last_name=request.form.get('last_name')
    email=request.form.get('email')

    title='Thank You'
    return render_template('form.html',title=title,first_name=first_name,last_name=last_name,email=email)


if __name__ == '__main__':
    app.run()