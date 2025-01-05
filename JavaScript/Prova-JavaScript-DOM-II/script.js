const adicionarNota = document.querySelector('#adicionar')
const gerador = document.querySelector('#gerador')
let contador = 0


adicionarNota.addEventListener('click', () =>{
    
    // CONTADOR DE NOTAS

    contador ++

    let divisor = document.createElement('div')
    divisor.className = 'notas'
    divisor.innerHTML= `Nota ${contador} <p style="font-size: 10px;">(Ajuste o tamanho no lado inferior direito do campo)</p>`
    divisor.style.alignItems = 'center'
    gerador.appendChild(divisor)


    // BLOCO DE NOTAS 
    
    let nota = document.createElement('textarea')
    nota.id = 'nota'
    nota.style.height ='150px'
    nota.style.width = '300px'
    divisor.appendChild(nota)

    // BOTAO DE EXCLUIR 

    let excluir = document.createElement('button')
    excluir.textContent = 'excluir'
    excluir.addEventListener('click',() =>{

        // REMOVER TODOS OS ELEMENTOS ESCOLHIDOS

        nota.remove()
        excluir.remove()
        divisor.remove()
    })

    divisor.appendChild(excluir)



})