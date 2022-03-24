$(document).ready(function () {
    let btn = document.getElementById('btn-order');
    let orders = document.getElementById("cart-items")
    console.log(orders.textContent)
    if (orders.textContent > 0) {
        btn.classList.add('items-added');
    }
});