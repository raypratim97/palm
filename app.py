import google.generativeai as palm
from flask import Flask,request,render_template
app = Flask(__name__)
palm.configure(api_key='AIzaSyDP_HryrkIHj72lh-Q2qE0wDy6Uo7E9XDA')
model = {'model': "models/chat-bison-001"}


@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "POST":
        q = request.form.get("q")
        print(q)
        r = palm.chat(
            **model,
            messages = q
        )
        
        return(render_template('index.html',r=r.last))
    else:
        return(render_template('index.html',r='Waiting for Question..........'))   
    
if __name__ == "__main__":
    app.run(port=4200)
