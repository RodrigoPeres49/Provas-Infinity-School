document.addEventListener("DOMContentLoaded", () => {
    console.log('pagina carregada')

    const radios = document.querySelectorAll('input[type="radio"][name="planos"]')
    console.log(radios)

    radios.forEach(radio => {
        radio.addEventListener('change', () => {
            console.log('evento de mudança')

            const divs = document.querySelectorAll('.conteudo-plano')
            
            divs.forEach(div => div.classList.remove('ativo'))
            console.log(divs)
             
            const conteudoSelecionado = document.querySelector(`.conteudo-plano[data-content="${radio.id}"]`)

            console.log('conteudo selecionado:' + conteudoSelecionado)
            if (conteudoSelecionado){
                conteudoSelecionado.classList.add('ativo')
                console.log('conteudo selecionado:', conteudoSelecionado)
            }
        })
    })


})