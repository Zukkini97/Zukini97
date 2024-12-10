document.getElementById('logout-btn').addEventListener('click', function (e) {
    e.preventDefault();
    fetch(logoutUrl, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken') // Adăugăm CSRF token-ul pentru securitate
        }
    }).then(response => {
        if (response.ok) {
            window.location.href = homeUrl; // Redirect la pagina de home
        } else {
            alert("Eroare la deconectare!");
        }
    });
});

// Funcție pentru a obține CSRF token din cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
