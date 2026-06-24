document.addEventListener("DOMContentLoaded", () => {

    const resultCard = document.querySelector(".result-card");

    if (resultCard) {
        resultCard.style.opacity = "0";

        setTimeout(() => {
            resultCard.style.transition = "1s";
            resultCard.style.opacity = "1";
        }, 300);
    }

});