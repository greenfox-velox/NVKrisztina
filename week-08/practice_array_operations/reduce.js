var input_list = [1, 2, 3, 4, 5];

var students = [
  {name: 'Rezso', age: 9.5, candies: 2},
  {name: 'Rezso', age: 10, candies: 1},
  {name: 'Aurel', age: 7, candies: 3},
  {name: 'Zsombor', age: 12, candies: 5},
  {name: 'Olaf', age: 12, candies: 7},
  {name: 'Teodor', age: 3, candies: 2}
];

//gives back 20 (initial value 5 + sum)
var totalAmount = input_list.reduce(function(pocket, item){
  return pocket + item;
}, 5);

console.log(totalAmount);

//
var totalNumberofCandies = students.reduce(function(pocket, student){
  return pocket + student.candies;
}, 0);

console.log(totalNumberofCandies);
