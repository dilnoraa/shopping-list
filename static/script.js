function addShoppingItem() {
    var url = "/shopping_list_api/";
    const request_options = {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": document.getElementsByName("csrfmiddlewaretoken")[0].value
        },
        body: JSON.stringify({
            "product": document.getElementById("id_selected_product").value,
            "location": document.getElementById("id_location").value
        })
    };
    fetch(
        url, request_options
    )
    .then(response => response.json())
    .then(function(data) {
        getShoppingList(data.id);
    });
}

function getShoppingList(id) {
    var get_request_options = {
        method: 'GET',
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": document.getElementsByName("csrfmiddlewaretoken")[0].value
        },
    };
    url = "/shopping_list_api/" + id;
    fetch(
        url, get_request_options
    ).then(response => response.json())
    .then(function(data) {
        var shopping_items = document.getElementById("id_shopping_list");
        var count = shopping_items.childElementCount;
        var div = document.createElement("div");
        div.innerHTML = "<div class='item-row'>" +
            "<span>" + (count + 1) + "</span>" +
            "<div><span></span>" + data.product_name.name + " - " + data.product_name.description + "</div>" +
            "<div style='padding-left: 10px;'><span>Location: </span>" + data.location + "</div>" +
            "</div>";
        shopping_items.appendChild(div);
    });
}

function editProduct(id) {
    window.location.href = "/product/" + id;
}

function deleteProduct(id) {
    if (confirm("Are you sure you want to delete this product?")) {
        const request_options = {
            method: 'DELETE',
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": document.getElementsByName("csrfmiddlewaretoken")[0].value
            }
        }
        var url = '/product/' + id;
        fetch(url, request_options)
        .then(function(data) {
            window.location.href = "/product_list/"
        });
    }
}
