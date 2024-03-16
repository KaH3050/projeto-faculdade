function enviar(){
    let nome = document.getElementById("nome").value;
    let money = document.getElementById('money').value;
    var msg = 'Olá ' + nome + 'Obrigado por ter doado o valor R$:' + money + ' A org Cão sem dono agradeçe';
    alert(msg);
}
