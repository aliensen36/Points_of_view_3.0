// const team = [
//     {
//         photo: '../static/img/team-photo-1.png',
//         name: 'Михаил Смирнов',
//         role: 'Digital artist: создание муз. подложки для арт-дайвинга в галерее сестер Асламазян'
//     },
//     {
//         photo: '../static/img/team-photo-2.png',
//         name: 'Гунина Анна',
//         role: 'Дизайн: айдентика лаборатории, разработка дизайна сайта-визитки'
//     },
//     {
//         photo: '../static/img/team-photo-3.png',
//         name: 'Алексей Степанов',
//         role: ' Sound engineer: звуковые эффекты для картины “Отсутствующие основания”'
//     },
//     {
//         photo: '../static/img/team-photo-4.png',
//         name: 'Артур Манукян',
//         role: ' Музыкант, звуко-режиссер: музыка к арт-дайвингу на выставке “Россия нулевых: случайных кадр”'
//     },
//     {
//         photo: '../static/img/team-photo-5.png',
//         name: 'Роза Сайфулина',
//         role: ' Видеомонтаж “Наивных вопросов художнику”, оцифровка картин галереи Асламазян для арт-дайвинга'
//     },
//     {
//         photo: '../static/img/team-photo-6.png',
//         name: 'Дарья Володина',
//         role: 'Оператор и фотограф “Наивных вопросов художнику”'
//     },
//     {
//         photo: '../static/img/team-photo-7.png',
//         name: 'Henry',
//         role: 'Озвучка на иностранных языках'
//     },
//     {
//         photo: '../static/img/team-photo-8.png',
//         name: 'Lucile',
//         role: 'Озвучка на иностранных языках'
//     },
//     {
//         photo: '../static/img/team-photo-9.png',
//         name: 'Андрей Гунявин',
//         role: 'Куратор лаборатории'
//     }
// ]

fetch('http://127.0.0.1:8000/en/api/team/')
    .then(response => response.json())
    .then(data => {
        // Обработка полученных данных
        console.log(data);
    })
    .catch(error => console.error('Error:', error));


let activeCard = 0;
const sliderPlace = document.querySelector('.team-carousel-slide-bar');
const cardWidth = 598;
const gap = 50;
const initialOffset = -242;
const widthOffset = gap + cardWidth;

const createTeamCard = (member) => {
    const card = document.createElement('div');
    card.classList.add('team-carousel-card');

    const image = document.createElement('img');
    image.src = member.photo;
    image.alt = 'photo of a team member';
    image.classList.add('team-carousel-photo');
    card.appendChild(image);

    const name = document.createElement('h3');
    name.classList.add('team-carousel-name');
    name.textContent = member.name;
    card.appendChild(name);

    const role = document.createElement('p');
    role.classList.add('team-carousel-role');
    role.textContent = member.role;
    card.appendChild(role);

    return card;
};

const initSlider = () => {
    const firstCard = createTeamCard(team[0]);
    sliderPlace.appendChild(firstCard);
    sliderPlace.style.left = initialOffset + 'px';
    nextCardGenerate();
    prevCardGenerate();
};

const nextCardGenerate = () => {
    let nextCard = activeCard + 1;
    if (nextCard >= team.length) {
        nextCard = 0;
    }

    let card = createTeamCard(team[nextCard]);
    sliderPlace.append(card);
}

const prevCardGenerate = (w = false) => {
    let prevCard = activeCard - 1;
    if (prevCard < 0) {
        prevCard = team.length - 1;
    }

    let card = createTeamCard(team[prevCard]);
    sliderPlace.prepend(card);
}

initSlider();

const nextSlide = () => {
    activeCard++;
    if (activeCard >= team.length) {
        activeCard = 0;
    }

    nextCardGenerate();

    document.querySelector('.team-carousel-btn-right').style.zIndex = '-1';
    document.querySelector('.team-carousel-btn-left').style.zIndex = '-1';

    animate({
        duration: 1000,
        draw: function (progress) {
            sliderPlace.style.left = initialOffset - widthOffset * progress + 'px';
        },
        removeElement: document.querySelector('.team-carousel-slide-bar > .team-carousel-card')
    });

}

const prevSlide = () => {
    activeCard--;
    if (activeCard < 0) {
        activeCard = team.length - 1;
    }

    prevCardGenerate(true);

    document.querySelector('.team-carousel-btn-left').style.zIndex = '-1';
    document.querySelector('.team-carousel-btn-right').style.zIndex = '-1';

    animate({
        duration: 1000,
        draw: function (progress) {
            sliderPlace.style.left = initialOffset - widthOffset * (1 - progress) + 'px';
        },
        timing: function (step) {
            return step;
        },
        removeElement: document.querySelector('.team-carousel-slide-bar > .team-carousel-card:last-child')
    });

}

document.querySelector('.team-carousel-btn-right').addEventListener('click', nextSlide);
document.querySelector('.team-carousel-btn-left').addEventListener('click', prevSlide);

function animate({ duration, draw, removeElement }) {

    let start = performance.now();

    requestAnimationFrame(function animate(time) {
        let step = (time - start) / duration;

        if (step > 1) step = 1;

        draw(step);

        if (step < 1) {
            requestAnimationFrame(animate);
        }
        else {
            removeElement.remove();
            sliderPlace.style.left = initialOffset + 'px';
            document.querySelector('.team-carousel-btn-right').style.zIndex = '1';
            document.querySelector('.team-carousel-btn-left').style.zIndex = '1';
        }
    });
}