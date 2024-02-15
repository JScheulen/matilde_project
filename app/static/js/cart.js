var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productID', productId, 'action', action)

        console.log('USER: ', user)
        if(user === 'AnonymousUser'){
            console.log('Not Logged in')
        }else {
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action){
    console.log(productId)

    var url = '/update_item/'

    const respuesta = fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({"productId": productId, 'action': action})
    })



    console.log(respuesta)
}

