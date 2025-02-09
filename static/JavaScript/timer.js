document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        const messages = document.querySelectorAll('.messages .alert');
        messages.forEach(function(message) {
            message.style.display = 'none';
            console.log("Mesajul a fost ascuns.");
        });
        }, 5000); // 5000 milisecunde = 5 secunde
    });