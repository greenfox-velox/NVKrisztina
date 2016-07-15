//*********type 1************
function sayHi(){
  console.log('hi!')
}

//sayHi();

//**********type 2************
var sayHello = function(){
  console.log('hello!')
}

//sayHello();

//**********type 3*************
function callAnotherFunction(funToBeCalled){
  funToBeCalled();
}

var sayByeAll = function(){
  console.log('bye all!')
}

//callAnotherFunction(sayByeAll);

//********type 2 (to export more methods)******
var counter = function(arr){
  return 'There are ' + arr.length + ' elements in our array.';
};

//************2 ways of exporting them*********

//module.exports.sayHi = sayHi;
//module.exports.sayHello = sayHello;
//module.exports.counter = counter;

module.exports = {
  sayHi: sayHi,
  sayHello: sayHello,
  counter: counter
}
