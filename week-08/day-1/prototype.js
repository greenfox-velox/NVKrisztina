'use strict';

var student = {
  age: 8,
  average: 4.5,
  name: 'Kovats Tibborka'
};

function MasterStudent=(erdos, bacon) {
  this.erdos = erdos;
  this.bacon = bacon;
}
/**/
MasterStudent.prototype = student;

var master = new MasterStudent(4, 3);
var master2 = new MasterStudent(5, 2);
student.age = 14;
/*megváltoztatom menet közben a prototype-ot*/
master2.name = 'Kikotos Natalia';
console.log(master.age);
console.log(master2.name);
console.log(master.name);
/*nem fogja felülírni a prototípust*/
