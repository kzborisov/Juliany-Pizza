$(document).ready(function () {
    let btn = document.getElementById('btn-order');
    let orders = document.getElementById("cart-items");
    if (orders.textContent > 0) {
        btn.classList.add('items-added');
    }
});
