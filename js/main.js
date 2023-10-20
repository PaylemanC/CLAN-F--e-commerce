// ----------------------- DOM:
const toggleMenuElement = document.getElementById('toggle-menu');
const mainMenuElement = document.getElementById('main-menu');
const reviewCardContainer = document.getElementById('review-card-container');


// ----------------------------------------------------------------------


// ----------------------- MENÚ TOGGLE RESPONSIVE:
toggleMenuElement.addEventListener('click', () => {
    mainMenuElement.classList.toggle('main-menu--show');
})


// ----------------------- API:
let apiUsers = "https://randomuser.me/api/"; 
let apiReviews = "https://jsonplaceholder.typicode.com/posts";

let reviewData = { name: '', photo: '', review: '' };

function reviewCard() {
    const { name, photo, review } = reviewData;
    reviewCardContainer.innerHTML = `
        <img src="${photo}" width="100px" class="">
        <p>Nombre: ${name}</p>
        <p>Reseña: ${review}</p>`;
}

fetch(apiUsers) 
    .then(user => user.json())
    .then(user => {
        const name = `${user.results[0].name.first} ${user.results[0].name.last}`;
        const photo = user.results[0].picture.medium;
        reviewData.name = name;
        reviewData.photo = photo;
        reviewCard();
    })
    .catch(error => console.log("Ocurrió un error en la solicitud de usuarios: ", error));

fetch(apiReviews) 
    .then(review => review.json()) 
    .then(review => {
        randomReview = Math.floor(Math.random() * review.length);
        reviewData.review = review[randomReview].body;
        reviewCard();
    }) 
    .catch(error => console.log("Ocurrió un error en la solicitud de reseñas: ", error));