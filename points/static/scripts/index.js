fetch('/api/team/')
    .then(response => response.json())
    .then(data => {
        team = data;
        initSlider();
    })
    .catch(error => console.error('Error:', error));

let activeCard = 0;
const sliderPlace = document.querySelector('.team-carousel-slide-bar');

let initialOffset;
let cardWidth;
let gap;

function updateSizes() {
    if (window.innerWidth < 600) {
        initialOffset = -260;
        cardWidth = 235;
        gap = 80;
    } else if (window.innerWidth < 1070) {
        initialOffset = -599;
        cardWidth = 598;
        gap = 53;
    } else {
        initialOffset = -242;
        cardWidth = 598;
        gap = 50;
    }
}

updateSizes();

window.addEventListener('resize', updateSizes);

let widthOffset = gap + cardWidth;

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