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

var leftThumbnailButton = document.querySelector('.leftToThumbnail');
leftThumbnailButton.addEventListener("click", swipeImagesLeft);

function swipeImagesLeft() {
  thumbnails.forEach(function(item, index){
    if (index <= photoList.length){
      item.setAttribute("src", photoList[index + 1]);
    };
  });
};

var rightThumbnailButton = document.querySelector('.rightToThumbnail');
rightThumbnailButton.addEventListener("click", swipeImagesRight);

function swipeImagesRight() {
  thumbnails.forEach(function(item, index){
    if (index >= 0){
    item.setAttribute("src", photoList[index - 1]);
  };
});
};
