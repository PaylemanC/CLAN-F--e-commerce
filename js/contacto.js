const formulario = document.getElementById("formulario");
const userName = document.getElementById('userNames');
const userEmail = document.getElementById('userEmail');

const regUserName = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;
const regUserEmail = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;


formulario.addEventListener("submit", (e) => {
    e.preventDefault();

    if (!regUserName.test(userNames.value)) {
        console.log('Formato no valido');
        return;
    }
    if (!regUserEmail.test(userEmail.value)) {
        console.log('Formato no valido');
        return;
    }

    console.log('formulario enviado');
})