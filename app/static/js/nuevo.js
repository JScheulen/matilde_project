

function getNumber(userName) {
    // Obtener el botón que ha sido clicado
    var button = event.target;
    // Obtener el nombre del producto desde el atributo data-product del botón
    var productName = button.dataset.product;
    var action = button.dataset.action;
    // Mostrar el nombre del producto en la consola
    console.log('Nombre del producto:', productName, 'accion', action);

    console.log(userName)

    if (userName ==="AnonymousUser") {
        console.log('User not Logged')
    } else {
        updateOrder(productName, action)
    }
}

function updateOrder(productName, action) {
      fetch('/update_item/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({'productName': productName, 'action': action})
      })
    .then(response => {
        // Verificar si la solicitud fue exitosa (código 200)
        if (!response.ok) {
            throw new Error('Hubo un problema al realizar la solicitud: ' + response.status);
        }
        // Si la solicitud fue exitosa, convertir la respuesta a JSON
        return response.json();
    })
    .then(data => {
        // Manipular los datos recibidos
        console.log(data);
        location.reload()
    })
    .catch(error => {
        // Capturar cualquier error que haya ocurrido durante la solicitud
        console.error('Error:', error);
    });
}

