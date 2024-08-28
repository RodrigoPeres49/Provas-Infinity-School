document.addEventListener('DOMContentLoaded', ()=>{

    // FUNÇÃO PARA EXIBIR A INPUT PARA ADICONAR OUTRO NÚMERO DESEJADO

    const numero = document.getElementById('numero')
    const outroNumero = document.getElementById("outroNumero")

    numero.addEventListener('change', ()=>{
        if(numero.value === 'outro'){
            outroNumero.classList.remove('outroNumero')
        }
        else{
            outroNumero.classList.add('outroNumero')
        }
    })

    // FUNÇÃO PARA CALCULAR O FATORIAL

    const calcular = document.querySelector('#calcular')

    calcular.addEventListener('click', ()=>{
        event.preventDefault()

        // VOU CRIAR UMA VARIÁVEL " numeroFatorial " QUE VAI RECEBER O NÚMERO SELECIONADO

        let numeroFatorial = 0

        // SE A OPÇÃO DOS NÚMEROS FOR IGUAL A " outro " A VARIÁVEL RECEBERA O VALOR DA ID DA INPUT " outroNumero "

        if(numero.value === 'outro'){
            numeroFatorial = parseFloat(outroNumero.value)
            console.log(numeroFatorial)
        }

        // SE NÃO ELE RECEBE O VALOR DE UM DOS NÚMEROS SELECIONADOS NA TAG select

        else{
            numeroFatorial = parseFloat(numero.value)
        }

        // AQUI SERÁ CRIADO UM ARRAY COM O TAMANHO DO NÚMERO SELECIONADO E UMA VARIÁVEL QUE EXIBIRÁ O RESULTADO

        let fatorialArray = Array.from({length:numeroFatorial}, (_,i) => numeroFatorial - i)
        let resultado = 0

        // AQUI VAMOS PERCORRER O ARRAY E REALIZAR O CÁLCULO DO FATORIAL

        fatorialArray.forEach((i) =>{
            if(i === numeroFatorial){
                
                // SE O NÚMERO FOR ELE MESMO ELE NÃO REALIZA NENHUMA ATIVIDADE

            }
            else{
                resultado += numeroFatorial * (i-1)
            }
        })

        // AQUI SERÁ EXIBIDO O RESULTADO NA PÁGINA

        const resultadoFatorial = document.getElementById('resultadoFatorial')
        resultadoFatorial.innerHTML = `O fatorial de ${numeroFatorial} é ${resultado}`
    })

})