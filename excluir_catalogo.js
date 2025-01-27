function cadastro(){
   
   let campoA = document.getElementsByName("fila")[0].value;
  
  if((campoA=="")){
    alert('Preencha todos os campos obrigatórios!'); 
    return
  } else {
    alert('Solicitação de exclusão realizada com sucesso!');
  }  
}

function GerarCombo() {

    let select = document.querySelector('#fila');
    let optionValue = select.options[select.selectedIndex];
   
    let value = optionValue.value;
   
   //  console.log(value)
   
    var fromSelect = document.getElementById('serviço');
    var toSelect = document.getElementById('escolserv');
    toSelect.innerHTML = "";
   
   
    for (var i = 0; i < fromSelect.options.length; i++) {
       var option = fromSelect.options[i];
       
       if (option.text.includes(value) ) {

      //   console.log(option.text)
        toSelect.innerHTML = toSelect.innerHTML + '<option>' + option.value + '</option>' 
        // toSelect.appendChild(option);    
   
       }
       
    };
   
   }
   
   GerarCombo()

