var botonCambiarRisa = document.getElementById("cambiar");


botonCambiarRisa.onclick = function(){
	var texto="waka waka: ";
	for(var i= 0; i<10;i++){
		texto+=i;
	}
	var risa= document.getElementById("risa");
	risa.innerHTML = texto;
}

var mombre= document.getElementById("nombre");
var titulo= document.getElementById("titulo");
var btnSaludar= document.getElementById("saludar");

btnSaludar.onclick =function(){
	var txtNombre= nombre.value;
	titulo.innerHTML= " Hola " + txtNombre;
}