const form = document.getElementById('language-form');
const languageRadios = form.querySelectorAll('input[name="language"]');
const languageLabels = form.querySelectorAll('.language-label');

function saveSelectedLanguage() {
    const selectedRadio = form.querySelector('input[name="language"]:checked');
    if (selectedRadio) {
        const selectedLanguage = selectedRadio.value;
        localStorage.setItem('selectedLanguage', selectedLanguage);
    }
}

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

setSelectedLanguage();

languageRadios.forEach((radio, index) => {
    radio.addEventListener('change', function () {
        
        saveSelectedLanguage();
        
        languageLabels.forEach(label => {
            label.classList.remove('selected');
        });
        
        languageLabels[index].classList.add('selected');
        
        form.submit();
    });
});




