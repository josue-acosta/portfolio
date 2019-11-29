// function to get list of images from the folder
async function fetchImageList(endpoint) {
    const response = await fetch(endpoint);
    const data = await response.json();
    return data;
}

// call function to get list of images
fetchImageList("/static/images/grace-kelly/grace-kelly-images.json")
    .then(data => imageList = data)
    .then(() => {
        secondImg = /\d+/.exec(imageList[0])
        console.log("secondImg: " + secondImg[0])
    })
    .then(() => {
        firstImg = /\d+/.exec(imageList[1])
        console.log("firstImg: " + firstImg[0])
    })
    .catch(err => console.log('Error, with message:', err.statusText));

// identify image and button elements
let switchButton = document.getElementById("switch__button")
let galleryImage = document.getElementsByClassName("gallery__image")
let currentImgIndex = /\d+/.exec(galleryImage[0].getAttribute("src"));


switchButton.addEventListener("click", () => {
    if (currentImgIndex[0] == firstImg) {
        console.log("currentImgIndex[0]: " + currentImgIndex[0])
        console.log("firstImg[0]: " + firstImg[0])
        galleryImage[0].setAttribute("src", `/static/images/grace-kelly/grace-kelly-${secondImg[0]}.png`)
    }
    else {
        console.log("currentImgIndex[0]: " + currentImgIndex[0])
        console.log("secondImg: " + secondImg)
        galleryImage[0].setAttribute("src", `/static/images/grace-kelly/grace-kelly-${firstImg[0]}.png`)
    }
})