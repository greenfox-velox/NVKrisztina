var fs = require('fs');

function getFlowers(file, fs, cb){
  fs.readFile(file, 'utf8', function(err, data){
    var flowers = JSON.parse(data);
    cb(flowers)
});
}

getFlowers('flowers.txt', fs, addNewFeatures);

function addNewFeatures(data){
  var newList = [];
  newList = data.map(function(item, index){
    var newItem = addNewFeature(item);
    return newItem;
  });
    return newList;
}

function addNewFeature(item){
  item.location = "Budapest";
  return item;
}

module.exports.getFlowers = getFlowers;
module.exports.addNewFeature = addNewFeature;
module.exports.addNewFeatures = addNewFeatures;
