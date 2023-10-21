function displayItems(category) {
    if (document.getElementById(category).style.display === "flex") {
        document.getElementById(category).style.display = "none";
    } else {
        document.getElementById(category).style.display = "flex";
    }
}