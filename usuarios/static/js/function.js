function bloquearLogin() {
    if (sessionStorage.getItem('usuario')) {
      window.location.href = 'index.php';
    }
  }
  
  if (document.querySelector('#login').checked) {
    // Iniciar sesión
  } else {
    // Bloquear login
    bloquearLogin();
  }