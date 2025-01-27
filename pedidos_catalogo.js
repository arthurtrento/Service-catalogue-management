function GerarCombo() {

    let select = document.querySelector('#fila');
    let optionValue = select.options[select.selectedIndex];
   
    let value = optionValue.value;
   
   //  console.log(value)
          
    var fromSelect = document.getElementById('insert');
    var fromSelect2 = document.getElementById('modify');
    var fromSelect3 = document.getElementById('exclude');
    var toSelect = document.getElementById('escolserv');
    var toSelect2 = document.getElementById('escolserv2');
    var toSelect3 = document.getElementById('escolserv3');
    toSelect.innerHTML = "";
    toSelect2.innerHTML = "";
    toSelect3.innerHTML = "";

    if (value == "") {
       return;
    }

    for (var i = 0; i < fromSelect.options.length; i++) {
      var option = fromSelect.options[i];
       if (option.value.includes(value) ) {
         // console.log(option.value)
         toSelect.innerHTML = toSelect.innerHTML + '<option>' + option.value + '</option>'
                
       }
    };
         
    for (var i = 0; i < fromSelect2.options.length; i++) {
      var option2 = fromSelect2.options[i];
        
       if (option2.value.includes(value) ) {
      //   console.log(option2.value)
        toSelect2.innerHTML = toSelect2.innerHTML + '<option>' + option2.value + '</option>'
                 
        }     
     };

     for (var i = 0; i < fromSelect3.options.length; i++) {
      var option3 = fromSelect3.options[i];
        
       if (option3.value.includes(value) ) {
      //   console.log(option3.value)
        toSelect3.innerHTML = toSelect3.innerHTML + '<option>' + option3.value + '</option>'
                 
        }          
     };
  
}

GerarCombo()

function cadastro_inserir(){

  let campoA = document.getElementsByName("fila")[0].value;
  let campoB = document.getElementsByName("escolserv")[0].value;
  
  if((campoA=="")){
    alert('Preencha todos os campos obrigatórios!'); 
    return
  } else {
      if((campoB=="")){
         alert('Não há pedidos para remoção!'); 
         return
      } else {
         alert('Pedido de inclusão apagado!');
             }
      }  
}

function cadastro_modificar(){

   let campoA = document.getElementsByName("fila")[0].value;
   let campoB = document.getElementsByName("escolserv2")[0].value;
  
  if((campoA=="")){
    alert('Preencha todos os campos obrigatórios!'); 
    return
  } else {
      if((campoB=="")){
         alert('Não há pedidos para remoção!'); 
         return
   }  else {
         alert('Pedido de modificação apagado!');
          }
   }  
}

function cadastro_excluir(){

   let campoA = document.getElementsByName("fila")[0].value;
   let campoB = document.getElementsByName("escolserv3")[0].value;

   
   console.log(campoB);
  
  if((campoA=="")){
    alert('Preencha todos os campos obrigatórios!'); 
    return
  } else {
      if((campoB=="")){
         alert('Não há pedidos para remoção!'); 
         return
   }  else {
         alert('Pedido de exclusão apagado!');
       }
   }  

}