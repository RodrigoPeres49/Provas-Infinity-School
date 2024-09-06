// LEITURA DA PÁGINA

let selecionado
let hoje = document.getElementById('hoje')
const meses = ['Janeiro', 'Fevereiro','Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
let data = new Date()
hoje.innerHTML += `${data.getDate()} de ${meses[data.getMonth()]} de ${data.getFullYear()}`

document.addEventListener('DOMContentLoaded', () => {
    const membros = document.getElementById('membros');
    // Função para listar membros da família
    function listarMembros(dados) {
        membros.innerHTML = ''; // Limpa a tabela antes de listar os membros
        dados.forEach(pessoa => {
            membros.innerHTML += `<tr><td>${pessoa.nome}</td><td>${pessoa.parentesco}</td><td><button onclick="selecionar('${pessoa.nome}', '${pessoa.parentesco}')">Selecionar</button></td>`
        })
    }

    // LER ARQUIVO JSON E INICIALIZAR sessionStorage
    fetch('familia.json')
        .then(resposta => resposta.json())
        .then(dadosJson => {
            
            let dadosArmazenados = sessionStorage.getItem('dadosFamilia');
            if (!dadosArmazenados) {
                
                sessionStorage.setItem('dadosFamilia', JSON.stringify(dadosJson));
                dadosArmazenados = dadosJson
            } else {
                
                dadosArmazenados = JSON.parse(dadosArmazenados);
            }
            listarMembros(dadosArmazenados); 
        })
        
})

function selecionar(nome, parentesco){

    
    selecionado = {
        "nome": nome,
        "parentesco": parentesco
    }
    

    const membroSelecionado = document.querySelector('#membroSelecionado')
    membroSelecionado.innerHTML = `<h1>${selecionado.nome}, ${selecionado.parentesco}</h1>`

    const mostrar = document.querySelector('.atividade')
    mostrar.classList.add('selecionado')

}


let atividades = []
const adicionar = document.querySelector('#adicionar')
    adicionar.addEventListener('click', ()=>{
        const descricao = document.querySelector('#descricao').value
        const horario = document.querySelector('#horario').value
        
        atividades.push({
            "descricao": descricao,
            "horario": horario
        })
        
        function converterHorario(horario){
            const [horas, minutos] = horario.split(':').map(Number)
            return horas * 60 + minutos
        }
        
        const atividadeOrdenada = atividades.slice().sort((a,b) => converterHorario(a.horario) - converterHorario(b.horario))
        const listaAtividades = document.querySelector('#listaAtividades')
        listaAtividades.innerHTML = ''
        atividadeOrdenada.forEach(i =>{
            listaAtividades.innerHTML += `<tr><td>${i.descricao}</td><td>${i.horario}</td></tr>`
        })
        

    })

    const imprimir = document.querySelector('#imprimir')

    imprimir.addEventListener('click', ()=>{
        const impressao = document.querySelector('#listaImpressao').innerHTML
        const membro = document.querySelector('#membroSelecionado').innerHTML
        const telaImpressao = window.open()
        telaImpressao.document.write(`<link rel="stylesheet" href="style.css"><div class='principal'><div class='atividades'><h1>${membro} Data: ${hoje.innerHTML}</h1><table>${impressao}</table></div></div>`)
        telaImpressao.window.print()

    
    })







