const URL = "http://127.0.0.1:5000/";

async function obtenerCoristas() {
    try {
        const response = await fetch(`${URL}coristas`);
        if (!response.ok) {
            throw new Error(`Error al obtener los coristas: ${response.statusText}`);
        }
        const data = await response.json();
        actualizarTablaCoristas(data);
    } catch (error) {
        console.error('Error:', error);
        alert('Error al obtener los coristas. Inténtalo de nuevo más tarde.');
    }
}

function actualizarTablaCoristas(data) {
    const coristasTable = document.getElementById('coristas-table');
    if (!coristasTable) {
        console.error('No se encontró el elemento de la tabla de coristas.');
        return;
    }

    const tbody = coristasTable.querySelector('tbody');
    if (!tbody) {
        console.error('No se encontró el cuerpo de la tabla de coristas.');
        return;
    }

    tbody.innerHTML = ''; // Limpiamos la tabla antes de insertar nuevos datos

    data.forEach(corista => {
        const row = tbody.insertRow();
        row.innerHTML = `
            <td>${corista.codigo}</td>
            <td>${corista.apellido}</td>
            <td>${corista.nombre}</td>
            <td align="right">${corista.correo}</td>
            <td><button onclick="eliminarCorista('${corista.codigo}')">Eliminar</button></td>`;
    });
}

async function eliminarCorista(codigo) {
    if (confirm('¿Estás seguro de que quieres eliminar este corista?')) {
        try {
            const response = await fetch(`${URL}coristas/${codigo}`, { method: 'DELETE' });
            if (!response.ok) {
                throw new Error(`Error al eliminar el corista: ${response.statusText}`);
            }
            obtenerCoristas(); // Actualizamos la lista de coristas después de eliminar uno
            alert('Corista eliminado correctamente.');
        } catch (error) {
            console.error('Error:', error);
            alert('Error al eliminar el corista. Inténtalo de nuevo más tarde.');
        }
    }
}

document.addEventListener('DOMContentLoaded', obtenerCoristas);
