// Definimos la URL del servidor donde se encuentran los datos de los coristas
const URL = "http://127.0.0.1:5000/";
// Al subir al servidor, deberá utilizarse la siguiente ruta.
// USUARIO debe ser reemplazado por el nombre de usuario de Pythonanywhere
// const URL = "https://USUARIO.pythonanywhere.com/";

// Realizamos la solicitud GET al servidor para obtener todos los coristas.
fetch(URL + 'coristas')

.then(function (response) {
    if (response.ok) {
        // Si la respuesta es exitosa (response.ok), convertimos el cuerpo de la respuesta de formato JSON a un objeto JavaScript y pasamos estos datos a la siguiente promesa then.
        return response.json();
    } else {
        // Si hubo un error, lanzamos explícitamente una excepción para ser "catcheada" más adelante
        throw new Error('Error al obtener los coristas.');
    }
})

.then(function (data) {
    // Obtenemos la referencia al elemento del DOM donde se mostrarán los coristas
    let tablaCoristas = document.getElementById('tablaCoristas');

    // Iteramos sobre cada corista en los datos obtenidos y creamos filas de tabla para cada uno
    for (let corista of data) {
        let fila = document.createElement('tr'); // Creamos una nueva fila de tabla (<tr>) para cada corista
        // Llenamos la fila con las celdas correspondientes usando la información del corista
        fila.innerHTML = `
            <td>${corista.codigo}</td>
            <td>${corista.apellido}</td>
            <td align="right">${corista.nombre}</td>
            <td align="right">${corista.correo}</td>
            <td align="right">${corista.cuerda}</td>
            <td align="right">${corista.experiencia}</td>
            <td align="right">${corista.lectura_musical}</td>
            <td align="right">${corista.estudios_musicales}</td>
            <td align="right">${corista.activo}</td>
        `;
        // Agregamos la fila a la tabla utilizando el método appendChild del elemento tablaCoristas
        tablaCoristas.appendChild(fila);
    }
})
// Capturamos y manejamos errores, mostrando una alerta en caso de error al obtener los coristas
.catch(function (error) {
    // Código para manejar errores
    alert('Error al obtener los coristas.');
});