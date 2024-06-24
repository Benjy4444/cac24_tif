const URL = "http://127.0.0.1:5000/"
// Obtiene el contenido del inventario
function obtenerProductos() {
fetch(URL + 'productos') // Realiza una solicitud GET al servidor y obtener la lista de productos.
.then(response => {
    // Si es exitosa (response.ok), convierte los datos de la respuesta de formato JSON a un objeto JavaScript.
    if (response.ok) { return response.json(); }
})
// Asigna los datos de los productos obtenidos a la propiedad productos del estado.
.then(data => {
    const coristasTable =
    document.getElementById('coristastable').getElementsByTagName('tbody')[0];
    coristasTable.innerHTML = ''; // Limpia la tabla antes de insertar nuevos datos
    data.forEach(corista => {
    const row = coristasTable.insertRow();
    row.innerHTML = `
    <td>${corista.codigo}</td>
    <td>${corista.apellido}</td>
    <td>${corista.nombre}</td>
    <td align="right">${corista.correo}</td>
    <td><button onclick="eliminarCorista('${corista.codigo}')">Eliminar</button></td>`;
    });
})
// Captura y maneja errores, mostrando una alerta en caso de error al obtener los productos.
.catch(error => {
    console.log('Error:', error);
    alert('Error al obtener los coristas.');
});
}
// Se utiliza para eliminar un producto.
function eliminarCorista(codigo) {
// Se muestra un diálogo de confirmación. Si el usuario confirma, se realiza una solicitud DELETE al servidor a través de
fetch(URL + 'coristas/${codigo}', {method: 'DELETE' });
if (confirm('¿Estás seguro de que quieres eliminar este corista?')) {
    fetch(URL + 'coristas/${codigo}', { method: 'DELETE' })
    .then(response => {
        if (response.ok) {
            // Si es exitosa (response.ok), elimina el producto y da mensaje de ok.
            obtenerCoristas(); // Vuelve a obtener la lista de productos para actualizar la tabla.
            alert('Corista eliminado correctamente.');
        }
    })
    // En caso de error, mostramos una alerta con un mensaje de error.
    .catch(error => {
        alert(error.message);
        });
    }
}

// Cuando la página se carga, llama a obtenerProductos para cargar la lista de productos.
document.addEventListener('DOMContentLoaded', obtenerCoristas);