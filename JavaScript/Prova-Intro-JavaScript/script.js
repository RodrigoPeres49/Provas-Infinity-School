document.addEventListener('DOMContentLoaded', ()=>{
    
    calcular = document.querySelector('#calcular')
    calcular.addEventListener('click', () =>{
        event.preventDefault()
        
        // PRIMEIRA NOTA

        const nota1 = parseFloat(document.querySelector('#nota1').value)
        const peso1 = parseFloat(document.querySelector('#peso1').value)

        // SEGUNDA NOTA

        const nota2 = parseFloat(document.querySelector('#nota2').value)
        const peso2 = parseFloat(document.querySelector('#peso2').value)

        // TERCEIRA NOTA

        const nota3 = parseFloat(document.querySelector('#nota3').value)
        const peso3 = parseFloat(document.querySelector('#peso3').value)


        resultado = ( (peso1*nota1) + (peso2*nota2) + (peso3*nota3) )/ ( peso1 + peso2 + peso3 )

        // RESULTADO EXIBIDO NO CONSOLE DE ACORDO COM A PROVA

        console.log(`A média ponderada das notas é de: ${resultado}`)

        // RESULTADO EXIBIDO NA PÁGINA

        resultadoHTML = document.getElementById('resultado').innerHTML =`A média ponderada das notas é de: ${resultado}`


    })
})