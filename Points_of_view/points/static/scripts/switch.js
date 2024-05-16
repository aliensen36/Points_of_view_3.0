// // Получаем форму и все радиокнопки
// const form = document.getElementById('language-form');
// const languageRadios = form.querySelectorAll('input[name="language"]');

// // Добавляем обработчик события к каждой радиокнопке
// languageRadios.forEach(radio => {
//     radio.addEventListener('change', function () {
//         // При изменении выбранного языка отправляем форму
//         form.submit();
//     });
// });


// // Получаем форму и все радиокнопки
// const form = document.getElementById('language-form');
// const languageRadios = form.querySelectorAll('input[name="language"]');

// // Добавляем обработчик события к каждой радиокнопке
// languageRadios.forEach(radio => {
//     radio.addEventListener('change', function () {
//         form.submit();
//         // Убираем класс "selected" у всех ярлыков
//         document.querySelectorAll('.language-label').forEach(label => {
//             label.classList.remove('selected');
//         });
//         // Добавляем класс "selected" к родительскому ярлыку выбранной радиокнопки
//         this.parentElement.classList.add('selected');
//         // При изменении выбранного языка отправляем форму
//     });
// });

// Получаем форму и все радиокнопки
const form = document.getElementById('language-form');
const languageRadios = form.querySelectorAll('input[name="language"]');
const languageLabels = form.querySelectorAll('.language-label');

// Функция для сохранения выбранного языка в localStorage
function saveSelectedLanguage() {
    const selectedRadio = form.querySelector('input[name="language"]:checked');
    if (selectedRadio) {
        const selectedLanguage = selectedRadio.value;
        localStorage.setItem('selectedLanguage', selectedLanguage);
    }
}

// Функция для установки класса "selected" на соответствующем ярлыке
function setSelectedLanguage() {
    const selectedLanguage = localStorage.getItem('selectedLanguage');
    if (selectedLanguage) {
        languageLabels.forEach(label => {
            if (label.querySelector('input').value === selectedLanguage) {
                label.classList.add('selected');
            } else {
                label.classList.remove('selected');
            }
        });
    }
}

// Вызываем функцию для установки выбранного языка при загрузке страницы
setSelectedLanguage();

// Добавляем обработчик события к каждой радиокнопке
languageRadios.forEach((radio, index) => {
    radio.addEventListener('change', function () {
        // Устанавливаем выбранный язык в localStorage
        saveSelectedLanguage();
        // Убираем класс "selected" у всех ярлыков
        languageLabels.forEach(label => {
            label.classList.remove('selected');
        });
        // Добавляем класс "selected" к родительскому ярлыку выбранной радиокнопки
        languageLabels[index].classList.add('selected');
        // При изменении выбранного языка отправляем форму
        form.submit();
    });
});




