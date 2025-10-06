from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/soma/valor1=<int:n1>/valor2=<int:n2>')
def soma(n1,n2):
    return "resultado da soma é {}".format(n1 + n2)

@app.route('/divisao/valor1=<int:n1>/valor2=<int:n2>')
def div(n1,n2):
    
    if n2 == 0:
        return f'Está invalido'
    else:
        return "resultado da divisão é {}".format(n1 / n2)
    
@app.route('/multiplicar/valor1=<int:n1>/valor2=<int:n2>')
def mult(n1,n2):
    
    return "resultado da multiplicação é {}".format(n1 * n2)

@app.route('/subtrair/valor1=<int:n1>/valor2=<int:n2>')
def sub(n1,n2):
    
    return "resultado da subtração é {}".format(n1 - n2)

if __name__ == "__main__":

    app.run(debug=True)
