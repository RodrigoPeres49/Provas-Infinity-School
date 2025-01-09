const path = require("path")
const fs = require("fs")

const tarefasFile = path.join(__dirname, "../tarefas.json")


const readTasks = () => {
    const data = fs.readFileSync(tarefasFile, "utf-8")
    return JSON.parse(data)
}


const saveTasks = (tarefas) => {
    fs.writeFileSync(tarefasFile, JSON.stringify(tarefas, null, 2))
}


const getAll = (req, res) => {
    const tarefas = readTasks() 
    res.render("index", { tarefas })
}


const listarTarefas = (req, res) => {
    try {
        const tarefas = readTasks() 
        res.json(tarefas) 
    } catch (error) {
        res.status(500).send("Erro ao listar tarefas")
    }
}


const adicionarTarefa = (req, res) => {
    const { descricao, data, hora } = req.body 
    const tarefas = readTasks()


    const novaTarefa = {
        id: tarefas.length > 0 ? tarefas[tarefas.length - 1].id + 1 : 1,
        descricao,
        data,
        hora,
        situacao: false, 
    }

    tarefas.push(novaTarefa) 
    saveTasks(tarefas) 
    res.status(201).send("Tarefa adicionada com sucesso!")
}

const removerTarefa = (req, res) => {
    const { id } = req.params
    const tarefas = readTasks()
    const index = tarefas.findIndex((t) => t.id === parseInt(id))

    if (index !== -1) {
        tarefas.splice(index, 1) 
        saveTasks(tarefas) 
        res.status(200).send("Tarefa removida com sucesso!")
    } else {
        res.status(404).send("Tarefa não encontrada!")
    }
}

const paginaEditarTarefa = (req, res) => {
    const { id } = req.params
    const tarefas = readTasks()

    const tarefa = tarefas.find((t) => t.id === parseInt(id))

    if (tarefa) {
        res.render("editar-tarefa", { tarefa })
    } else {
        res.status(404).send("Tarefa não encontrada!")
    }
};

const editarTarefa = (req, res) => {
    const { id } = req.params
    const { descricao, data, hora } = req.body
    const tarefas = readTasks()

    const tarefa = tarefas.find((t) => t.id === parseInt(id))

    if (tarefa) {
        tarefa.descricao = descricao
        tarefa.data = data
        tarefa.hora = hora
        saveTasks(tarefas) 
        res.status(200).send("Tarefa editada com sucesso!")

    } else {
        res.status(404).send("Tarefa não encontrada!")

    }



    res.redirect("/")
}


const concluirTarefa = (req, res) => {
    const { id } = req.params
    const tarefas = readTasks()

    const tarefa = tarefas.find((t) => t.id === parseInt(id))

    if (tarefa) {
        tarefa.situacao = true 
        saveTasks(tarefas) 
        res.status(200).send("Tarefa concluída com sucesso!")
    } else {
        res.status(404).send("Tarefa não encontrada!")
    }
}


module.exports = {
    getAll,
    listarTarefas,
    adicionarTarefa,
    removerTarefa,
    paginaEditarTarefa,
    editarTarefa,
    concluirTarefa,
}
