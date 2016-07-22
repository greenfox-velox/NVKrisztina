var dog = (function(){

  var sound = 'woof';

  function talk() {
    console.log(sound);
  }

  return {
    printTalk: talk
  };

})();

dog.printTalk();
