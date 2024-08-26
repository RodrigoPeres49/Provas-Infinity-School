const altura = document.getElementById('altura')
altura.addEventListener('input', (event)=>{
    let valor = event.target.value.replace(/\D/g, '')
    valor = (parseFloat(valor) / 100).toFixed(2)

    event.target.value = valor
})

const calcularIMC = document.querySelector('#calcularIMC')

calcularIMC.addEventListener('click', ()=>{
    event.preventDefault()

        const nome = document.querySelector('#nome').value
        const idade = document.querySelector('#idade').value

        const altura = parseFloat(document.querySelector('#altura').value)
        const peso = parseFloat(document.querySelector('#peso').value)
        const imc= peso / (altura * altura)
        let grauIMC = ''

        if(imc < 16){
            grauIMC = 'Abaixo do peso, situação muito grave.'
        }
        else if (imc >=16 && imc <= 16.99){
            grauIMC = 'Abaixo do peso, situação grave.'
        }
        else if (imc >=17 && imc <= 18.49){
            grauIMC = 'Abaixo do peso.'
        }
        else if (imc >=18.50 && imc <= 24.99){
            grauIMC = 'Peso normal.'
        }
        else if (imc >=25 && imc <= 29.99){
            grauIMC = 'Sobrepeso , situação grave.'
        }
        else if (imc >=30 && imc <= 34.99){
            grauIMC = 'Obesidade grau I, situação grave.'
        }
        else if (imc >=35 && imc <= 39.99){
            grauIMC = 'Obesidade grau II, situação muito grave.'
        }
        else if(imc > 40){
            grauIMC = 'Obesidade grau III, situação muito grave.'
        }
        else{
            grauIMC = 'IMC Inválido.'
        }

        const resultadoIMC = document.getElementById('resultadoIMC')
        resultadoIMC.innerHTML = `<ul>
                                      <li>Pessoa: ${nome}</li>
                                      <li>Idade: ${idade}</li>
                                  </ul>
                                  <p>IMC: ${imc}, ${grauIMC} </p>`
})