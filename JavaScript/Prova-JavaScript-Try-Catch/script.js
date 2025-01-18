
// CONTA FICTICIA

let conta = {
    saldo: 1000,
    historico : [
        {
            dia: "01/01/2025 , 16:46:25",
            natureza: "Deposito",
            valor: 1000,
            valorAtual: 1000,
            valorAnterior: 0
        }
    ]
}

// EXIBIR SALDO

    const saldo = document.getElementById("saldo")
    saldo.innerHTML = conta.saldo


//EXIBIR FORMULARIO DE DEPOSITO

const exibirDeposito = document.getElementById("exibirDeposito")

function conteudoDeposito(){
    let deposito = document.getElementById("deposito")
    let saque = document.getElementById("saque")
    saque.classList.remove("mostrar")
    saque.classList.add("esconder")
    deposito.classList.remove("esconder")
    deposito.classList.add("mostrar")
}

exibirDeposito.addEventListener("click", conteudoDeposito)

// EXIBIR FORMULARIO DE SAQUE

const exibirSaque = document.getElementById("exibirSaque")

function conteudoSaque(){
    let deposito = document.getElementById("deposito")
    let saque = document.getElementById("saque")
    deposito.classList.remove("mostrar")
    deposito.classList.add("esconder")
    saque.classList.remove("esconder")
    saque.classList.add("mostrar")
}

exibirSaque.addEventListener("click", conteudoSaque)

// DEPOSITAR DINHEIRO

const deposito = document.getElementById("depositar")
const depositar = () => {
    let depositoInput = document.getElementById("valorDeposito")
    let valorDeposito = document.getElementById("valorDeposito").value
    try{
        if(valorDeposito>0){
            let valorAntigo = parseFloat(conta.saldo)
            conta.saldo += parseFloat(valorDeposito)
            let dia = new Date()
            const hoje = `${dia.getDate()}/${dia.getMonth() > 9 ? '' : '0'}${dia.getMonth() + 1}/${dia.getFullYear()} , ` +
                         `${dia.getHours()}:${dia.getMinutes()}:${dia.getSeconds()}`
    
            let extrato = {
                dia: hoje,
                natureza: "Deposito",
                valor: valorDeposito,
                valorAtual: conta.saldo,
                valorAnterior: valorAntigo
            }
            conta.historico.push(extrato)
            
            saldo.innerHTML = conta.saldo
    
            alert("depositado!", conta.saldo)
            depositoInput.value = ""
        }
        else{
            alert("Não foi possível depositar, insira um valor maior que 0")
        }
    } catch(erro){
    console.log("Não foi possível depositar", erro)
    }
    

}

deposito.addEventListener("click", depositar)

// SACAR DINHEIRO

const saque = document.getElementById("sacar")
const sacar = () => {
    let saqueInput = document.getElementById("valorSaque")
    let valorSaque = document.getElementById("valorSaque").value
    try{
        if(valorSaque>0){
            if (valorSaque<=conta.saldo){
                let valorAntigo = parseFloat(conta.saldo)
                conta.saldo -= parseFloat(valorSaque)
                let dia = new Date()
                const hoje = `${dia.getDate()}/${dia.getMonth() > 9 ? '' : '0'}${dia.getMonth() + 1}/${dia.getFullYear()} , ` +
                             `${dia.getHours()}:${dia.getMinutes()}:${dia.getSeconds()}`
        
                let extrato = {
                    dia: hoje,
                    natureza: "Saque",
                    valor: valorSaque,
                    valorAtual: conta.saldo,
                    valorAnterior: valorAntigo
                }
                conta.historico.push(extrato)
                
                saldo.innerHTML = conta.saldo
        
                alert("Saque realizado com sucesso!", conta.saldo)
                saqueInput.value = ""
            }
            else{
                alert("Saldo insuficiente para sacar")
            }
        }
        else{
            alert("O valor do saque deve ser maior que 0")
        }

    } catch(erro){
    console.log("Não foi possível sacar", erro)
    }
}

saque.addEventListener("click", sacar)

// EXTRATO

const exibirExtrato = () => {
    const extrato = document.getElementById("extrato")
    extrato.innerHTML = ""
    conta.historico.slice().reverse().forEach(transacao => {
        extrato.innerHTML += `<li>
                                <ul>
                                    <li><h2>${transacao.natureza} dia: ${transacao.dia}</h2></li>
                                    <li>Valor: ${transacao.valor}</li>
                                    <li>Saldo atual: ${transacao.valorAtual}</li>
                                    <li>Saldo anterior: ${transacao.valorAnterior}</li>
                                </ul>
                            </li>`  
        })
}

const mostrarExtrato = document.getElementById("exibirExtrato")
mostrarExtrato.addEventListener("click", exibirExtrato)
    
