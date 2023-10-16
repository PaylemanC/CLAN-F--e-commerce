// Variables para manipular el DOM entorno al formulario: 
const formulario = document.getElementById("formulario");

const userName = document.getElementById("userName");
const userEmail = document.getElementById("userEmail");
const userNumber = document.getElementById("userNumber");
const mensaje = document.getElementById("mensaje");

const alertSuccess = document.getElementById("alertSuccess");

const alertName = document.getElementById("alertName");
const alertEmail = document.getElementById("alertEmail");
const alertNumber = document.getElementById("alertNumber");
const alertMsj = document.getElementById("alertMsj");

// Patrones regex de validación de campos:

const regUserName = /^[A-Za-zÑñÁáÉéÍíÓóÚúÜü\s]+$/;
const regUserEmail = /^[a-z0-9]+(\.[_a-z0-9]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,15})$/;
const regUserNumber = /^\d+$/gi;

const errores = [];

const pintarMensajeExito = () => {
    alertSuccess.classList.remove("d-none");
    alertSuccess.textContent = "¡Mensaje enviado con éxito!";
};

const pintarMensajeError = (errores) => {
    errores.forEach((item) => {
        item.tipo.classList.remove("d-none");
        item.tipo.textContent = item.msg;
    });
};

//Validación base: verificación de patrones regex y que no haya campos vacíos, maneja el .remove y .add de las clases de CSS.

function validar(campo, mensajeAlerta, elementoAlerta, patron = null) {
    if (campo.value.trim() === "" || patron && (!patron.test(campo.value) || !campo.value.trim())) {
        campo.classList.add("is-invalid");
        elementoAlerta.classList.remove("d-none");
        elementoAlerta.textContent = mensajeAlerta;
        errores.push({
            campo: campo,
            tipo: elementoAlerta,
            msg: mensajeAlerta
        });
    } else {
        campo.classList.remove("is-invalid");
        campo.classList.add("is-valid");
        elementoAlerta.classList.add("d-none");
    }
}

formulario.addEventListener("submit", (e) => {
    e.preventDefault();    

    alertSuccess.classList.add("d-none");
    errores.length = 0; 

    //validar(campo a validar, mensaje personalizado para "campo inválido", elemento <p> donde se ingresará mensaje anterior en caso de campo inválido, patrón regex en caso de que lo precise)
    validar(userName, "Formato no válido para campo nombre, solo letras.", alertName, regUserName);
    validar(userEmail, "Escriba un correo electrónico válido.", alertEmail, regUserEmail);
    validar(userNumber, "Formato no válido para campo teléfono, solo números.", alertNumber, regUserNumber);
    validar(mensaje, "El campo mensaje no puede estar vacío.", alertMsj);

    //Validar TODOS:
    if (errores.length !== 0) {
        pintarMensajeError(errores);
        return;
    }

    console.log("¡Formulario enviado con éxito!");
    pintarMensajeExito();
});