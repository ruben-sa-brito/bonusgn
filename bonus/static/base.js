function formatarMoeda() {
    var elemento = document.getElementById('vendas');
    var valor = elemento.value;
    
    valor = valor + '';
    valor = valor.replace(/\D/g, "");
    valor = valor.replace(',', '')
    valor = valor.replace(/^0+/, "");
    if (valor.length > 2){
        valor = valor.slice(0, -2)+','+valor.slice(-2)
    }
    if (valor.length == 2){
        valor = '0,'+valor
    }
    if (valor.length == 1){
        valor = '0,0'+valor
    }

    if (valor.length > 6){
        valor = valor.slice(0, -3).replace(/\B(?=(\d{3})+(?!\d))/g, ".") + valor.slice(-3);

    }
    elemento.value ='R$ '+valor;
}