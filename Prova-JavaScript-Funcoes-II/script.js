
document.getElementById('enviarAvaliacao').addEventListener('click', ()=>{
    const avaliacoes = {
        nome: document.querySelector('#nome').value,
        comida: document.querySelector('input[name="comida"]:checked').value,
        servico: document.querySelector('input[name="servico"]:checked').value,
        atendimento: document.querySelector('input[name="atendimento"]:checked').value
    }
    
    fetch('http://localhost:3000/salvar-avaliacao', {
        method:'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(avaliacoes)
    })
    .then(response => response.text())
    .then(data => {
        alert(data)
    })
    .catch(error =>{
        console.error('Erro:', error)
    })
})