function blurActive() {
    if (document.activeElement instanceof HTMLElement) {
        document.activeElement.blur();
    }
}

function hideModals() {
    const elements = document.getElementsByClassName("modal");
    for (const element of elements) {
        const modal = bootstrap.Modal.getInstance(element);
        if (modal) {
            modal.hide();
        }
    }
}

function showMessage(message) {
    hideModals();
    let modalBody = document.querySelector("#modal-message .modal-body p");
    modalBody.innerHTML = message;
    let modal = new bootstrap.Modal(document.getElementById("modal-message"));
    modal.show();
}

document.addEventListener("hide.bs.modal", blurActive, true);
