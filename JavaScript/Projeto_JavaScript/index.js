
// Necessário a instalação de algumas dependencias:

// npm install express
// npm install ejs

const express = require("express")
const path = require("path")
const routes = require("./routes/routes")
const app = express()

const port = 3000

app.set("view engine", "ejs")
app.set("views", path.join(__dirname, "public"))

app.use(express.static(path.join(__dirname, "public")))
app.use(routes)



app.listen(port, () =>{
    console.log('Rodando na porta', port)
})