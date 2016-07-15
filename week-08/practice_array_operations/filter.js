'use strict';

//filtered is not a function. It returns an array.

var input_list = [1, 2, 3, 4, 5];

var filtered = input_list.filter(function(item){
    return item % 2 === 0;
});

console.log(filtered);

//********************************************

var students = [
  {name: 'Rezso', age: 9.5, candies: 2},
  {name: 'Rezso', age: 10, candies: 1},
  {name: 'Aurel', age: 7, candies: 3},
  {name: 'Zsombor', age: 12, candies: 5},
  {name: 'Olaf', age: 12, candies: 7},
  {name: 'Teodor', age: 3, candies: 2}
];

console.log(students[0].name);

//2 sort adja vissza

var filtered2 = students.filter(function(item){
  return item.name === 'Rezso';
})

console.log(filtered2);

//csak amire igaz

var filtered3 = students.filter(function(item){
  return item.name === 'Rezso' && item.age === 10;
})

console.log(filtered3);

//

var filtered4 = students.filter(function(item){
  return item.candies > 4;
})

console.log(filtered4);
