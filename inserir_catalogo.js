function cadastro(){

  let campoA = document.getElementsByName("fila")[0].value;
  let campoB = document.getElementsByName("tipo")[0].value;
  let campoC = document.getElementsByName("area")[0].value;
  let campoD = document.getElementsByName("categoria_n0")[0].value;
  let campoE = document.getElementsByName("categoria_n1")[0].value;
  let campoF = document.getElementsByName("categoria_n2")[0].value;
  let campoG = document.getElementsByName("SLA")[0].value;
  let campoH = document.getElementsByName("resolvedores")[0].value;
  let campoI = document.getElementsByName("gestores")[0].value;
  
  if((campoA=="") || (campoB=="") || (campoC=="") || (campoD=="") || (campoE=="") || (campoF=="") || (campoG=="") || (campoH=="") || (campoI=="")){
    alert('Preencha todos os campos obrigatórios!'); 
    return
  } else {
    alert('Solicitação de inclusão realizada com sucesso!');
  }
  
}