thumbnailBordrDom.appendChild(thumbnailItemsDom[0]);
let timeRunning = 2000;
let timeAutoNext = 3000;

nextDom.onclick = function() {
    showSlider('next');
}

prevDom.onclick = function() {
    showSlider('prev');
}
let runTimeOut;
let runNextAuto = setTimeout(() => { nextDom.click(); }, timeAutoNext)

function showSlider(type) {
    let SliderItemsDom = SliderDom.querySelectorAll('.carousel .list .item');
    let thumbnailItemsDom = document.querySelectorAll('.carousel .thumbnail .item');

    if (type == 'next') {
        SliderDom.appendChild(SliderItemsDom[0]);
        thumbnailBordrDom.appendChild(thumbnailItemsDom[0]);
        carouselDom.classList.add('next');
    } else {
        SliderDom.prepend(SliderItemsDom[SliderItemsDom.length - 1]);
        thumbnailBordrDom.prepend(thumbnailItemsDom[thumbnailItemsDom.length - 1]);
        carouselDom.classList.add('perv');
    }
    clearTimeout(runTimeOut);
    runTimeOut = setTimeout(() => {
        carouselDom.classList.remove('next');
        carouselDom.classList.remove('perv')
    }, timeRunning)

    clearTimeout(runNextAuto);
    runNextAuto = setTimeout(() => { nextDom.click(); }, timeAutoNext)
}