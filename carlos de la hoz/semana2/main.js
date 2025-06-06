function validarLogin() {
    const usuario = document.getElementById('user').value;
    const contrasena = document.getElementById('password').value;
    const mensajeError = document.getElementById('mensaje-error');

    const usuarioValido = "admin";
    const contrasenaValida = "1234";


    if (usuario === usuarioValido && contrasena === contrasenaValida) {
        mensajeError.textContent="¡Login exitoso!";
        mensajeError.style.color="green";
        setTimeout(()=>{
        window.location.href="about_me.html";
        },1000);
        return false;
    } else {
        mensajeError.textContent = "Usuario o contraseña incorrectos";
        mensajeError.style.color="red";
        return false;
    }
}


