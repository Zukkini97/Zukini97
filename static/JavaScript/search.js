// document.getElementById('search-form').addEventListener('submit', function(e) {
//     e.preventDefault();  // Previi trimiterea tradițională a formularului

//     const query = document.getElementById('search-query').value;

//     // Trimite cererea AJAX
//     fetch('/search/?query=' + query)
//         .then(response => response.json())
//         .then(data => {
//             const resultsContainer = document.getElementById('search-results');
//             resultsContainer.innerHTML = '';  // Curăță rezultatele anterioare

//             if (data.results.length > 0) {
//                 let html = '<ul>';
//                 data.results.forEach(result => {
//                     html += `<li>${result.pet_name} - ${result.pet_species} - ${result.pet_breed}</li>`;
//                 });
//                 html += '</ul>';
//                 resultsContainer.innerHTML = html;
//             } else {
//                 resultsContainer.innerHTML = '<p>Nu au fost găsite rezultate.</p>';
//             }
//         })
//         .catch(error => {
//             console.error('Eroare la căutare:', error);
//         });
// });
