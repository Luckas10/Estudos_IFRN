function openModal(id) {
    document.getElementById(id).style.display = 'block';
}

function closeModal(id) {
    const modal = document.getElementById(id);
    const content = modal.querySelector('.modal-content');

    modal.classList.add('fade-out');

    // Aguarda a animação terminar
    content.addEventListener('animationend', function handleAnimationEnd() {
        modal.style.display = 'none';
        modal.classList.remove('fade-out');
        content.removeEventListener('animationend', handleAnimationEnd);
    });
}

window.onclick = function (event) {
    const modals = ['registerModal', 'listModal'];
    modals.forEach(id => {
        const modal = document.getElementById(id);
        if (event.target === modal) {
            closeModal(id);
        }
    });
};

