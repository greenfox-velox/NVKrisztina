var input_list = [1, 2, 3, 4, 5];

var students = [
  {name: 'Rezso', age: 9.5, candies: 2},
  {name: 'Rezso', age: 10, candies: 1},
  {name: 'Aurel', age: 7, candies: 3},
  {name: 'Zsombor', age: 12, candies: 5},
  {name: 'Olaf', age: 12, candies: 7},
  {name: 'Teodor', age: 3, candies: 2}
];

var output_list = input_list.map(function(item, index){
  return item + 2;
});

console.log(output_list);

//
input_list.map(function(item, index){
  console.log(item + 2);
});
