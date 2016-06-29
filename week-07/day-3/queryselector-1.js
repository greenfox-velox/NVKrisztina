'use strict'

var king = document.querySelector('#b325');
console.log(king);

var conceited = document.querySelector('.asteroid.b326');
console.log(conceited);
alert(conceited);

var businessLamp = document.querySelectorAll('.big');
var num = 0;
for (num; num < businessLamp.length; num++){
  console.log(businessLamp[num]);
}
businessLamp.forEach(function(item, index){
  console.log(item);
})

var conceitedKing = document.querySelectorAll('#b325, .asteroid.b326');
var num = 0;
for (num; num < conceitedKing.length; num++){
  alert(conceitedKing[num]);
}

var noBusiness = document.querySelectorAll('.container, .b329');
console.log(noBusiness);

var allBizniss = document.querySelector('.asteroid.big');
alert(allBizniss);
