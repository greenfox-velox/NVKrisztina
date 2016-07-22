function Dog(sound){
  this.sound = sound
  //this.sound = 'woof' nem kell a new Dog paramétereként megadni a woof-ot
}

Dog.prototype.talk = function (){
  console.log(this.sound);
};

var lucky = new Dog('woof')
lucky.talk();
