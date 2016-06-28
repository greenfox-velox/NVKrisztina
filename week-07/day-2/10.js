'use strict';

// create a student object
// that has a method `addgrade`, that takes a grade from 1 to 5
// an other method `getAverage`, that returns the average of the grades

var Student = {
  grades: [],
  addgrade: function (grade){
    this.grades += grade;
  },
  getAverage: function (){
    var aver = 0;
    return this.grades;
  },
}

//var student1 = new Student();
console.log(student1.addgrade(4));
