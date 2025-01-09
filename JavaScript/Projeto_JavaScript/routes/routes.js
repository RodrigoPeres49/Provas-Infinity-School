const routes = require("express").Router()
const TaskController = require("../controller/TaskController")

const express = require("express")
routes.use(express.json())

routes.get("/", TaskController.getAll)

routes.post("/adicionar-tarefa", TaskController.adicionarTarefa)

routes.get("/editar-tarefa/:id", TaskController.paginaEditarTarefa)

routes.put("/editar-tarefa/:id", TaskController.editarTarefa)

routes.delete("/remover-tarefa/:id", TaskController.removerTarefa)

routes.patch("/concluir-tarefa/:id", TaskController.concluirTarefa)

routes.get("/listar-tarefas", TaskController.listarTarefas)

module.exports = routes