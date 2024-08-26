
// LISTA INICIAL DE ALUNOS

let alunos = [
    {
        nome: "Ana",
        nota: 8.5
    },
    {
        nome: "Bruno",
        nota: 7.0
    },
    {
        nome: "Carla",
        nota: 9.2
    },
    {
        nome: "Daniel",
        nota: 6.8
    },
    {
        nome: "Elisa",
        nota: 7.5
    }
];


// O PROFESSOR PODE INSERIR OUTRO ALUNO MANUALMENTE SE PRECISAR

const cadastrar = document.querySelector('#inserirAluno')

cadastrar.addEventListener('click', () =>{

    event.preventDefault()

    const novoAluno = {
        nome: document.querySelector('#nome').value,
        nota: parseFloat(document.querySelector('#nota').value)
    };

    // ADICIONANDO O NOVO ALUNO

    alunos.push(novoAluno);

    // EXIBINDO O NOVO ALUNO NA LISTA

    const exibirAlunos = document.getElementById('alunos')
    exibirAlunos.innerHTML += `<tr><td>${novoAluno.nome}</td><td>${novoAluno.nota}</td></tr>` 
    
    nome.value = ""
    nota.value = ""

    
})

// LISTAR OS ALUNOS DA SALA DE AULA

const exibirAlunos = document.getElementById('alunos')

alunos.forEach ((aluno) =>{
    exibirAlunos.innerHTML += `<tr><td>${aluno.nome}</td><td>${aluno.nota}</td></tr>` 
} )

let numeroAlunos = 0
let notas = 0


// CALCULAR A MEDIA DAS NOTAS DOS ALUNOS

const mediaNotas = document.querySelector('#calcularMedia')

mediaNotas.addEventListener('click', ()=>{

    alunos.forEach ((aluno) =>{
        numeroAlunos++
        notas += aluno.nota
    } )

    const resultado = notas / numeroAlunos
    const resultadoMedia = document.getElementById('resultadoMedia')
    resultadoMedia.innerHTML = `A média dos alunos é de: ${resultado}`
    
})