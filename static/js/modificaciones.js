const URL = "http://127.0.0.1:5000/";

// Variables de estado
let mostrarDatosCorista = false;

document.getElementById('form-obtener-corista').addEventListener('submit', obtenerCorista);
document.getElementById('form-guardar-cambios').addEventListener('submit', guardarCambios);

function obtenerCorista(event) {
    event.preventDefault();
    const codigo = document.getElementById('codigo').value;

    fetch(`${URL}coristas/${codigo}`)
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Error al obtener los datos del corista.');
            }
        })
        .then(data => {
            mostrarDatosCorista = true;
            mostrarFormulario(data);
        })
        .catch(error => {
            alert('Código no encontrado.');
        });
}

function mostrarFormulario(data) {
    if (mostrarDatosCorista) {
        document.getElementById('apellidoModificar').value = data.apellido;
        document.getElementById('nombreModificar').value = data.nombre;
        document.getElementById('correoModificar').value = data.correo;
        document.getElementById('cuerdaModificar').value = data.cuerda;
        document.getElementById('experienciaModificar').value = data.experiencia;
        document.getElementById('lectura_musicalModificar').value = data.lectura_musical;
        document.getElementById('estudios_musicalesModificar').value = data.estudios_musicales;
        document.getElementById('activoModificar').value = data.activo;
        document.getElementById('datos-corista').style.display = 'block';
    } else {
        document.getElementById('datos-corista').style.display = 'none';
    }
}

function guardarCambios(event) {
    event.preventDefault();
    const codigo = document.getElementById('codigo').value;
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

    fetch(`${URL}coristas/${codigo}`, {
        method: 'PUT',
        body: formData,
    })
        .then(response => {
            if (response.ok) {
                alert('Corista actualizado correctamente.');
                limpiarFormulario();
            } else {
                throw new Error('Error al guardar los cambios del corista.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error al actualizar el corista.');
        });
}

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
    mostrarDatosCorista = false;
    document.getElementById('datos-corista').style.display = 'none';
}