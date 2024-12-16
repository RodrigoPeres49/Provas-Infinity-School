from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods= [ 'GET' , 'POST'])
def index():
    
    # OBS: o programa estava ocorrendo um erro quando eu utilizava um laço for.
    # desta maneira eu consegui realizar as operações.
    
    # Variaveis
    
    velocidade = 0
    valor = 0
    
    # Condicionais
    
    if request.method == 'POST':
        velocidade = int(request.form.get('velocidade'))
        if velocidade > 80:
            multiplicador = velocidade - 80
            valor = multiplicador * 20
            info = "Velocidade excedida a {}km/h, valor da multa: {},00R$.".format(velocidade, valor)
        else:
            info = 'Velocidade não excedida.'
    
    else:
        info = 'Informe a velocidade do veículo.'
    
    # Retorno 
    
    return render_template('index.html' , velocidade = velocidade, valor = valor, info = info)

if __name__ == '__main__':
    app.run(debug=True)
    
    