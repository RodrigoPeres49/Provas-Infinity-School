
// EXECUTAR O SEGUINTE COMANDO NO TERMINAL NA PASTA DO PROJETO:
// npm init -y
// npm install express body-parser
// npm install cors

// APÓS INSTALAR AS DEPENDÊNCIAS EXECUTAR O COMANDO " node server.js "

const express = require('express')
const fs = require('fs')
const cors = require('cors')
const bodyParser = require('body-parser')

const app = express()
const port = 3000

app.use(cors())
app.use(express.static('public'))
app.use(bodyParser.json())

app.post('/salvar-avaliacao', (req,res) =>{
    const avaliacao = req.body

    fs.readFile('avaliacoes.json', 'utf-8', (err, data) =>{
        let avaliacoes = []

        if(!err){
            avaliacoes = JSON.parse(data)
        }

        avaliacoes.push(avaliacao)

        fs.writeFile('avaliacoes.json', JSON.stringify(avaliacoes, null, 2), (err) =>{
            if(err){
                res.status(500).send('Erro ao salvar avaliação')
            }
            else{
                res.status(200).send('Avaliação enviada com sucesso!')
            }
        })
    })
})

app.listen(port, () =>{
    console.log(`Servidor rodando na porta ${port}`)
})