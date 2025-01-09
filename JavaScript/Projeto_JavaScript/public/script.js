
document.addEventListener("DOMContentLoaded", ()=>{
    const adicionarBotao = document.getElementById("adicionar-tarefa")

    if (adicionarBotao){

        adicionarBotao.addEventListener("click", () => {
            const descricao = document.getElementById("descricao").value
            const data = document.getElementById("data").value
            const hora = document.getElementById("hora").value
        
            fetch("/adicionar-tarefa", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ descricao, data, hora })
            })
            .then((response) =>{
                if(!response.ok){
                    throw new Error("Erro ao adicionar tarefa")
                }
                return response.text()
            })
            .then(message => {
                alert(message)
                fetchTarefas()
            })
            .catch(error => console.error("Erro ao adicionar tarefa:", error))
            })

    }
   
    const editarBotao = document.getElementById("editar-tarefa")
    
    if(editarBotao){

    document.getElementById("editar-tarefa").addEventListener("click", async () => {
    console.log('clicou')
    const tarefaId = window.location.pathname.split("/").pop()
    const descricao = document.getElementById("descricao").value
    const data = document.getElementById("data").value
    const hora = document.getElementById("hora").value

    try {
        const response = await fetch(`/editar-tarefa/${tarefaId}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ descricao, data, hora }),
        });

        if (!response.ok) {
            throw new Error("Erro ao editar tarefa")
        }

        const message = await response.text()
        alert(message);

        // Redireciona para a página inicial após salvar
        window.location.href = "/"
    } catch (error) {
        console.error("Erro ao editar tarefa:", error);
        alert("Falha ao editar a tarefa. Tente novamente.")
    }
    })
    }
})

async function removerTarefa(id) {
    try {
        const response = await fetch(`/remover-tarefa/${id}`, { method: "DELETE" })
        if (response.ok) {
            alert("Tarefa removida com sucesso!")
            fetchTarefas() // Atualiza a lista de tarefas
        }
    } catch (error) {
        console.error("Erro ao remover tarefa:", error)
    }
}

async function concluirTarefa(id) {
    try {
        const response = await fetch(`/concluir-tarefa/${id}`, { method: "PATCH" })
        if (response.ok) {
            alert("Tarefa concluída com sucesso!")
            fetchTarefas() 
        }
    } catch (error) {
        console.error("Erro ao concluir tarefa:", error)
    }
}

async function fetchTarefas() {   
    try{
        const resposta = await fetch("/listar-tarefas")
        const tarefas = await resposta.json()

        const tabela = document.getElementById("tarefas")
        if (!tabela) {
            console.error("Elemento com ID 'tarefas' não encontrado!")
            return
        }

        tabela.innerHTML = ""

        if (tarefas.length > 0){
            tarefas.forEach((tarefa) => {
                const linha = document.createElement("tr")
                linha.innerHTML = `
                    <td>${tarefa.descricao}</td>
                    <td>${tarefa.data}</td>
                    <td>${tarefa.hora}</td>
                    <td>${tarefa.situacao ? "Concluída" : "Pendente"}</td>
                    <td>
                        <button class="botao" onclick="concluirTarefa(${tarefa.id})">Concluir</button>
                        <button class="botao" onclick="removerTarefa(${tarefa.id})">Remover</button>
                        <a class="botao" href="/editar-tarefa/${tarefa.id}">Editar</a>
                    </td>
                `
                tabela.appendChild(linha)
                
            })
        }
        else {
            tabela.innerHTML = `
                <tr>
                    <td colspan="5">Nenhuma tarefa encontrada</td>
                </tr>
            `
        }
    }catch (error){
        console.error("Erro ao buscar tarefas: ", error)
    }
}

document.addEventListener("DOMContentLoaded", () => {
    fetchTarefas() 
    setInterval(fetchTarefas, 5000)
})