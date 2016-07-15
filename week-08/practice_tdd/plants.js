'use strict';

function Plant(plant_type, water_level, times_soil_changed){
  this.plant_type = plant_type;
  this.water_level = water_level;
  this.times_soil_changed = times_soil_changed;
  this.init_by_type();
}

Plant.prototype.init_by_type = function() {
  if (this.plant_type == 'tulip'){
    this.water_needed = 3;
    this.soil_needed = 1;
  } else if (this.plant_type == 'rose'){
    this.water_needed = 1;
    this.soil_needed = 2;
  }
};

Plant.prototype.water = function() {
  this.water_level += this.water_needed;
};

Plant.prototype.give_new_soil = function() {
  this.times_soil_changed += this.soil_needed;
};

Plant.prototype.get_stats = function() {
  return 'Type: ' + this.plant_type + ', ' + 'Water level: ' + this.water_level + ', ' + 'Times soil changed: ' + this.times_soil_changed
}

function Garden(water_storage, soil_storage){
  this.water_storage = water_storage;
  this.soil_storage = soil_storage;
  this.list_of_plants = [];
}

Garden.prototype.add_plants = function(plant){
  this.list_of_plants.push(plant);
}

Garden.prototype.water_all = function(){
  var _this = this
  this.list_of_plants.forEach(function (item, index){
    item.water();
    _this.water_storage -= item.water_needed;
  })
}

Garden.prototype.give_new_soil_all = function(){
  var _this = this
  this.list_of_plants.forEach(function (item, index){
    item.give_new_soil();
    _this.soil_storage -= item.soil_needed;
  })
}

Garden.prototype.get_stats = function() {
  return 'Number of plants: ' + this.list_of_plants.length + ', ' + 'Water stored: ' + this.water_storage + ', ' + 'Soil stored: ' + this.soil_storage
}











module.exports.Plant = Plant;
module.exports.Garden = Garden;
