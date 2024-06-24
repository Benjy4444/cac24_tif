const URL = "http://127.0.0.1:5000/"
//Al subir al servidor, deberá utilizarse la siguiente ruta.
//USUARIO debe ser reemplazado por el nombre de usuario de Pythonanywhere
//const URL = "https://USUARIO.pythonanywhere.com/"
// Variables de estado para controlar la visibilidad y los datos del formulario
let codigo = '';
let apellido = '';
let nombre = '';
let correo = '';
let cuerda = '';
let experiencia = '';
let lectura_musical = '';
let estudios_musicales = '';
let activo = '';
//let imagenSeleccionada = null;
//let imagenUrlTemp = null;
let mostrarDatosCorista = false;
document.getElementById('form-obtenercorista').addEventListener('submit', obtenerCorista);
document.getElementById('form-guardarcambios').addEventListener('submit', guardarCambios);
//document.getElementById('nuevaImagen').addEventListener('change',seleccionarImagen);
// Se ejecuta cuando se envía el formulario de consulta. Realiza una solicitud GET a la API y obtiene los datos del producto correspondiente al código ingresado.
function obtenerProducto(event) {
    event.preventDefault();
    codigo = document.getElementById('codigo').value;
    fetch(URL + 'coristas/' + codigo)
.then(response => {
    if (response.ok) {
        return response.json()
    } else {
        throw new Error('Error al obtener los datos del corista.')
    }
})
.then(data => {apellido = data.apellido; nombre = data.nombre; correo = data.correo;
cuerda = data.cuerda; experiencia = data.experiencia; lectura_musical = data.lectura_musical; 
estudios_musicales = data.estudios_musicales; activo = data.activo; mostrarDatosCorista = true; //Activa la vista del segundo formulario
mostrarFormulario();
})
.catch(error => {
    alert('Código no encontrado.');
});
}
// Muestra el formulario con los datos del producto
function mostrarFormulario() {
if (mostrarDatosCorista) {
    document.getElementById('apellidoModificar').value = apellido;
    document.getElementById('nombreModificar').value = nombre;
    document.getElementById('correoModificar').value = correo;
    document.getElementById('cuerdaModificar').value = cuerda;
    document.getElementById('experienciaModificar').value = experiencia;
    document.getElementById('lectura_musicalModificar').value = lectura_musical;
    document.getElementById('estudios_musicalesModificar').value = estudios_musicales;
    document.getElementById('activoModificar').value = activo;

    //const imagenActual = document.getElementById('imagenactual');
    //if (imagen_url && !imagenSeleccionada) { // Verifica si imagen_url no está vacía y no se ha seleccionado una imagen
        //imagenActual.src = './static/imagenes/' +
        //imagen_url;
        //;
        //Al subir al servidor, deberá utilizarse la siguiente ruta. USUARIO debe ser reemplazado por el nombre de usuario de Pythonanywhere
        //imagenActual.src = 'https://www.pythonanywhere.com/user/USUARIO/files/home/USUARIO/mysite/static/imagenes/' + imagen_url;
        //imagenActual.style.display = 'block'; // Muestra la imagen actual
    //} else {
        //imagenActual.style.display = 'none'; // Oculta la imagen si no hay URL
    //}
        document.getElementById('datos-corista').style.display = 'block';
    } else {
        document.getElementById('datos-corista').style.display = 'none';
    }
}
// Se activa cuando el usuario selecciona una imagen para cargar.
//function seleccionarImagen(event) {
    //const file = event.target.files[0];
    //imagenSeleccionada = file;
    //imagenUrlTemp = URL.createObjectURL(file); // Crea una URL temporal para la vista previa
    //const imagenVistaPrevia = document.getElementById('imagenvista-previa');
    //imagenVistaPrevia.src = imagenUrlTemp;
    //imagenVistaPrevia.style.display = 'block';
//}
// Se usa para enviar los datos modificados del producto al servidor.
function guardarCambios(event) {
    event.preventDefault();
    const formData = new FormData();
    formData.append('codigo', codigo);
    formData.append('apellido', document.getElementById('apellidoModificar').value);
    formData.append('nombre', document.getElementById('nombreModificar').value);
    formData.append('correo', document.getElementById('correoModificar').value);
    formData.append('cuerda', document.getElementById('cuerdaModificar').value);
    formData.append('experiencia', document.getElementById('experienciaModificar').value);
    formData.append('lectura_musical', document.getElementById('lectura_musicalModificar').value);
    formData.append('estudios_musicales', document.getElementById('estudios_musicalesModificar').value);
    formData.append('activo', document.getElementById('activoModificar').value);

    
    // Si se ha seleccionado una imagen nueva, la añade al formData.
    //if (imagenSeleccionada) {
       //formData.append('imagen', imagenSeleccionada, imagenSeleccionada.name);
    //}
    fetch(URL + 'coristas/' + codigo, {
        method: 'PUT',
        body: formData,
    })
    .then(response => {
        if (response.ok) {
            return response.json()
        } else {
            throw new Error('Error al guardar los cambios del corista.')
        }
    })
    .then(data => {
        alert('Corista actualizado correctamente.');
        limpiarFormulario();
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error al actualizar el corista.');
    });
    }
    // Restablece todas las variables relacionadas con el formulario a sus valores iniciales, lo que efectivamente "limpia" el formulario.
    function limpiarFormulario() {
        document.getElementById('codigo').value = '';
        document.getElementById('apellidoModificar').value = '';
        document.getElementById('nombreModificar').value = '';
        document.getElementById('correoModificar').value = '';
        document.getElementById('cuerdaModificar').value = '';
        document.getElementById('experienciaModificar').value = '';
        document.getElementById('lectura_musicalModificar').value = '';
        document.getElementById('estudios_musicalesModificar').value = '';
        document.getElementById('activoModificar').value = '';
        //document.getElementById('nuevaImagen').value = '';
        //const imagenActual = document.getElementById('imagenactual');
        //imagenActual.style.display = 'none';
        //const imagenVistaPrevia = document.getElementById('imagenvista-previa');
        //imagenVistaPrevia.style.display = 'none';
        codigo = '';
        apellido = '';
        nombre = '';
        correo = '';
        cuerda = '';
        experiencia = '';
        lectura_musical = '';
        estudios_musicales = '';
        activo = '';
        //imagen_url = '';
        //imagenSeleccionada = null;
        //imagenUrlTemp = null;
        mostrarDatosCorista = false;
        document.getElementById('datos-corista').style.display = 'none';
}