document.addEventListener('DOMContentLoaded', function () {
    var inputElement = document.getElementById('repo-name');
    var displayElement = document.getElementById('display-src');

    inputElement.addEventListener('input', function () {
        var text = inputElement.value;
        var displayText = `http://3.19.41.18:8000/tecweb/Projeto1A/svg/insper-tecnologias-web/${text}`;
        displayElement.textContent = displayText;
    });
});