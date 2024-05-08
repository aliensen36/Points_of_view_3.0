const team = [
    {
        photo: '../img/team-photo-1.png',
        name: 'Михаил Смирнов',
        role: 'Digital artist: создание муз. подложки для арт-дайвинга в галерее сестер Асламазян'
    },
    {
        photo: '../img/team-photo-2.png',
        name: 'Гунина Анна',
        role: 'Дизайн: айдентика лаборатории, разработка дизайна сайта-визитки'
    },
    {
        photo: '../img/team-photo-3.png',
        name: 'Алексей Степанов',
        role: ' Sound engineer: звуковые эффекты для картины “Отсутствующие основания”'
    },
    {
        photo: '../img/team-photo-4.png',
        name: 'Артур Манукян',
        role: ' Музыкант, звуко-режиссер: музыка к арт-дайвингу на выставке “Россия нулевых: случайных кадр”'
    },
    {
        photo: '../img/team-photo-5.png',
        name: 'Роза Сайфулина',
        role: ' Видеомонтаж “Наивных вопросов художнику”, оцифровка картин галереи Асламазян для арт-дайвинга'
    },
    {
        photo: '../img/team-photo-6.png',
        name: 'Дарья Володина',
        role: 'Оператор и фотограф “Наивных вопросов художнику”'
    },
    {
        photo: '../img/team-photo-7.png',
        name: 'Henry',
        role: 'Озвучка на иностранных языках'
    },
    {
        photo: '../img/team-photo-8.png',
        name: 'Lucile',
        role: 'Озвучка на иностранных языках'
    },
    {
        photo: '../img/team-photo-9.png',
        name: 'Андрей Гунявин',
        role: 'Куратор лаборатории'
    }
]

const slideBar = document.querySelector('.team-carousel-slide-bar');
const btnLeft = document.querySelector('.team-carousel-btn-left');
const btnRight = document.querySelector('.team-carousel-btn-right');
const cardWidth = 598;
const gap = 50;

const cardsHTML = team.map(member => `
        <div class="team-carousel-card">
            <img src="${member.photo}" alt="photo of a team member" class="team-carousel-photo">
            <h3 class="team-carousel-name">
                ${member.name}
            </h3>
            <p class="team-carousel-role">
                ${member.role}
            </p>
        </div>
    `);

const initSlider = () => {
    slideBar.innerHTML = cardsHTML.slice(0, 3).join('');
    slideBar.style.transform = 'translateX(-242px)';
};

initSlider();

const removeFirstSlide = () => {
    // Находим первый элемент-ребёнок slideBar
    const firstSlide = slideBar.firstElementChild;

    // Проверяем, есть ли какой-либо элемент для удаления
    if (firstSlide) {
        // Удаляем первый элемент-ребёнок
        slideBar.removeChild(firstSlide);
    }
};

