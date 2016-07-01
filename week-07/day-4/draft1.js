
var leftThumbnailButton = document.querySelector('.leftToThumbnail');
leftThumbnailButton.addEventListener("click", swipeImagesRight);

var thumbnailLength = document.querySelectorAll('.inThumbnail').length;

var number = 1;

function swipeImagesLeft() {
  if (photoList.length > number + thumbnailLength - 1){
  thumbnails.forEach(function(item, num){
      item.setAttribute("src", photoList[num + number]);
  });
  number += 1;
};
};

var rightThumbnailButton = document.querySelector('.rightToThumbnail');
rightThumbnailButton.addEventListener("click", swipeImagesLeft);

function swipeImagesRight() {
  if (number - 1 > 0){
  thumbnails.forEach(function(item, num){
    item.setAttribute("src", photoList[num - number]);
});
  number -= 1;
};
};
