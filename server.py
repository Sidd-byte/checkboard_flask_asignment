from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html",col=8,row=8,color_one='green',color_two="black")
    # return render_template("index.html", col=8, row=8, color_one='red',color_two='black')




if __name__=="__main__":
    app.run(debug=True)