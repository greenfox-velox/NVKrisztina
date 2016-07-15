var tape = require('tape');
var fs = require('fs');

var garden = require('./add_flower_properties');

var getFlowers = garden.getFlowers

tape('filereader_works', function (t){
  getFlowers('flowers.txt', fs, function(result){
    t.deepEqual(result, [ { type: 'tulip', color: 'pink'},
      { type: 'rose', color: 'white'},
      { type: 'tulip', color: 'yellow'} ]);
  });
  t.end();
});

tape('iteration_works', function (t){
  garden.addNewFeatures([{
      "type": "tulip",
      "color": "pink"
  }]);
  t.deepEqual(garden.addNewFeatures([{
      "type": "tulip",
      "color": "pink"
  }]), [{
      "type": "tulip",
      "color": "pink",
      "location": "Budapest"
  }])
  t.end();
});
