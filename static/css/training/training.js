function checkMethod(attribute) {

    let item_quantity_1;
    let item_quantity_2;
    let item_quantity_3;
    let training_time;
    let training_results;

    if (attribute === "strength") {
        const selectedMethod = document.querySelector("#strength-method");

        item_quantity_1 = document.getElementById("strength-quantity-1")
        item_quantity_2 = document.getElementById("strength-quantity-2")
        item_quantity_3 = document.getElementById("strength-quantity-3")
        training_time = document.getElementById("strength-time")
        training_results = document.getElementById("strength-results")

        if (selectedMethod.value === "method_1") {
            item_quantity_1.innerHTML = "x5"
            item_quantity_2.innerHTML = "x5"
            item_quantity_3.innerHTML = "x1"
            training_time.innerHTML = "15 minutes"
            training_results.innerHTML = "+1 Strength"

        } else if (selectedMethod.value === "method_2") {
            item_quantity_1.innerHTML = "x25"
            item_quantity_2.innerHTML = "x25"
            item_quantity_3.innerHTML = "x5"
            training_time.innerHTML = "1 hour"
            training_results.innerHTML = "+4 Strength"

        } else if (selectedMethod.value === "method_3") {
            item_quantity_1.innerHTML = "x50"
            item_quantity_2.innerHTML = "x50"
            item_quantity_3.innerHTML = "x10"
            training_time.innerHTML = "3 hours"
            training_results.innerHTML = "+12 Strength"

        } else if (selectedMethod.value === "method_4") {
            item_quantity_1.innerHTML = "x500"
            item_quantity_2.innerHTML = "x500"
            item_quantity_3.innerHTML = "x100"
            training_time.innerHTML = "12 hours"
            training_results.innerHTML = "+48 Strength"
        }
    }
}