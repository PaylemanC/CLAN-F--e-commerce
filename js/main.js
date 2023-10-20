// ----------------------- DOM:
const toggleMenuElement = document.getElementById('toggle-menu');
const mainMenuElement = document.getElementById('main-menu');
const reviewsCardContainer = document.getElementById('reviews');


// ----------------------------------------------------------------------


// ----------------------- MENÚ TOGGLE RESPONSIVE:
toggleMenuElement.addEventListener('click', () => {
    mainMenuElement.classList.toggle('main-menu--show');
})


// ----------------------- API para reseñas:
let apiUsers = "https://randomuser.me/api/"; 
let apiReviews = "https://jsonplaceholder.typicode.com/posts";

let reviewData = { name: '', photo: '', review: '' };

function reviewCard() {
    const { name, photo, review } = reviewData;
    const reviewCard = document.createElement('div');
    reviewCard.classList.add('review-card');
    const cardContent = `<img src="${photo}" alt="Foto de ${name}" class="review-card__img">
        <p class="review-card__description">"${review}."</p>
        <p class="review-card__name">${name}</p>`

    reviewCard.innerHTML = cardContent;
    reviewsCardContainer.appendChild(reviewCard);
}

fetch(apiReviews) 
    .then(review => review.json()) 
    .then(review => {
        randomReview = Math.floor(Math.random() * review.length);
        reviewData.review = review[randomReview].body;
    }) 
    .catch(error => console.log("Ocurrió un error en la solicitud de reseñas: ", error));

fetch(apiUsers) 
    .then(user => user.json())
    .then(user => {
        const name = `${user.results[0].name.first} ${user.results[0].name.last}`;
        const photo = user.results[0].picture.large;
        reviewData.name = name;
        reviewData.photo = photo;
        reviewCard();
    })
    .catch(error => console.log("Ocurrió un error en la solicitud de usuarios: ", error));