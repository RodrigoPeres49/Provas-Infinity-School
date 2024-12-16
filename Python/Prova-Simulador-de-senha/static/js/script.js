function pressionar_botao(botao) {
    var input_numero = document.getElementById("senha");
    input_numero.value += botao;
}
function pagina_cadastro() {
    window.location.href = "/cadastrar";
}
function exibir_mensagem(){
    sorteioVariavel = document.getElementById('info').src='/cadastrar';
    document.getElementById('info').style.display = 'block';
}