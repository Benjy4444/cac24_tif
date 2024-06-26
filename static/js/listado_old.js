//<script>
const URL = "http://127.0.0.1:5000/"
// Al subir al servidor, deberá utilizarse la siguiente ruta. 
//USUARIO debe ser reemplazado por el nombre de usuario de Pythonanywhere
//const URL = "https://USUARIO.pythonanywhere.com/"
// Realizamos la solicitud GET al servidor para obtener todos los productos.
fetch(URL + 'coristas')
.then(function (response) {
if (response.ok) {
    //Si la respuesta es exitosa (response.ok), convierte el cuerpo de la respuesta de formato JSON a un objeto JavaScript y pasa estos datos a la siguiente promesa then.
    return response.json();
} else {
    // Si hubo un error, lanzar explícitamente una excepción para ser "catcheada" más adelante
    throw new Error('Error al obtener los coristas.');
}
})
//Esta función maneja los datos convertidos del JSON.
.then(function (data) {
    let tablaCoristas =
    document.getElementById('tablaCoristas'); //Selecciona el elemento del DOM donde se mostrarán los productos.
    // Iteramos sobre cada producto y agregamos filas a la tabla
    for (let corista of data) {
    let fila = document.createElement('tr'); //Crea una nueva fila de tabla (<tr>) para cada producto.
    fila.innerHTML = '<td>' + corista.codigo + '</td>' +
    '<td>' + corista.apellido + '</td>' +
    '<td align="right">' + corista.nombre +
    '</td>' +
    '<td align="right">' + corista.correo + '</td>'
    + '<td align="right">' + corista.cuerda +
    '</td>' +
    '<td align="right">' + corista.experiencia +
    '</td>' +
    '<td align="right">' + corista.lectura_musical +
    '</td>' +
    '<td align="right">' + corista.estudios_musicales +
    '</td>' +
    '<td align="right">' + corista.activo +
    '</td>';
    // Mostrar miniatura de la imagen
    //'<td><img src=./static/imagenes/' + producto.imagen_url +' alt="Imagen del producto" style="width: 100px;"></td>' + '<td align="right">' + producto.proveedor + '</td>';
    //Al subir al servidor, deberá utilizarse la siguiente ruta. USUARIO debe ser reemplazado por el nombre de usuario de Pythonanywhere
    //'<td><img src=https://www.pythonanywhere.com/user/USUARIO/files/home/USUARIO/mysite/static/imagenes/' + producto.imagen_url +' alt="Imagen del producto" style="width: 100px;"></td>' + '<td align="right">' + producto.proveedor + '</td>';
    //Una vez que se crea la fila con el contenido del producto, se agrega a la tabla utilizando el método appendChild del elemento tablaProductos.
    tablaCoristas.appendChild(fila);
    }
})
//Captura y maneja errores, mostrando una alerta en caso de error al obtener los productos.
.catch(function (error) {
    // Código para manejar errores
    alert('Error al obtener los coristas.');
});

