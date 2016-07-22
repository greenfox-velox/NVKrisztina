var dog = function(){

  var sound = 'woof';

  return {

    talk: function () {
      console.log(sound)
    }
  }

};

var sniffles = dog()
sniffles.talk();
