const altura = document.getElementById('altura')
altura.addEventListener('input', (event)=>{
    let valor = event.target.value.replace(/\D/g, '')
    valor = (parseFloat(valor) / 100).toFixed(2)

    event.target.value = valor
})

function calculoIMC(){
    const peso = document.getElementById('peso').value
    const altura = document.getElementById('altura').value
    calculo = peso /(altura * altura)
    resultado = document.getElementById('resultado')

    resultado.innerHTML = `<p>IMC: ${calculo} </p>`
}
