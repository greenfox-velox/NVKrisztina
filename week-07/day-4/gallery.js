'use strict'

var photoList = ['cat9.jpg', 'cat1.jpg', 'cat2.jpg', 'cat3.jpg', 'cat4.jpg', 'cat5.jpg', 'cat6.jpg', 'cat7.jpg', 'cat8.jpg'];

var a = document.querySelector('.clickOn');
a.addEventListener('click', movePicturesLeft);

var b = document.querySelector('.inTheMiddle');
var c = b.getAttribute("src");

var d = 0;

function movePicturesLeft() {
  d -= 1;
  if (0 <= d && d <= photoList.length - 1){
    b.setAttribute("src", photoList[d]);
  };
};

var e = document.querySelectorAll('.clickOn')[1];
e.addEventListener('click', movePicturesRight);

function movePicturesRight() {
  d += 1;
  if (0 <= d && d <= photoList.length - 1){
    b.setAttribute("src", photoList[d]);
  }
};

var thumbnails = document.querySelectorAll('.inThumbnail');
thumbnails.forEach(function(item, index){
  item.setAttribute("src", photoList[index]);
});

var number = 0;

function setNumberBetweenPhotoListlength() {
  if (number > photoList.length - thumbnailLength){
    number = photoList.length - thumbnailLength;
  } else if (number < 0){
    number = 0;
  }
}

var leftThumbnailButton = document.querySelector('.leftToThumbnail');
leftThumbnailButton.addEventListener("click", swipeImagesRight);

var thumbnailLength = document.querySelectorAll('.inThumbnail').length;

function swipeImagesLeft() {
  setNumberBetweenPhotoListlength();
  number += 1;
  if (photoList.length > number + thumbnailLength - 1){
  thumbnails.forEach(function(item, num){
      item.setAttribute("src", photoList[num + number]);
  });
};
};

var rightThumbnailButton = document.querySelector('.rightToThumbnail');
rightThumbnailButton.addEventListener("click", swipeImagesLeft);

function swipeImagesRight() {
  setNumberBetweenPhotoListlength();
  number -= 1;
  if (number >= 0){
  thumbnails.forEach(function(item, num){
    item.setAttribute("src", photoList[num + number]);
});
};
};
