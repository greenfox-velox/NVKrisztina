'use strict';

var tape = require('tape');

var garden = require('./plants');

var Plant = garden.Plant;
var Garden = garden.Garden;

tape('Plant properties', function (t) {
  var plant = new Plant('tulip', 2, 2);
  t.equal(plant.plant_type, 'tulip');
  t.equal(plant.water_level, 2);
  t.equal(plant.times_soil_changed, 2);
  t.end();
});

tape('init_by_type method', function (t){
  var plant = new Plant('tulip', 2, 2);
  plant.init_by_type();
  t.equal(plant.water_needed, 3)
  t.end();
});

tape('water increases', function (t){
  var plant = new Plant('tulip', 2, 2);
  plant.water();
  t.equal(plant.water_level, 5);
  t.end();
});

tape ('new soil increases', function (t){
  var plant = new Plant('tulip', 2, 2);
  plant.give_new_soil();
  t.equal(plant.times_soil_changed, 3);
  t.end();
})

tape ('stats are printed', function (t){
  var plant = new Plant('tulip', 2, 2);
  t.equal(plant.get_stats(), 'Type: tulip, Water level: 2, Times soil changed: 2');
  t.end();
})

tape('Garden properties', function (t) {
  var garden = new Garden(100, 200);
  t.equal(garden.water_storage, 100);
  t.equal(garden.soil_storage, 200);
  t.end();
});

tape('adding item inreases list length', function (t) {
  var garden = new Garden(100, 200);
  var plant = new Plant('tulip', 2, 2);
  garden.add_plants(plant);
  t.equal(garden.list_of_plants.length, 1);
  t.end();
});

tape ('water_all decreases water_storage', function (t) {
  var garden = new Garden(100, 200);
  var plant = new Plant('tulip', 2, 2);
  garden.add_plants(plant);
  garden.water_all();
  t.equal(garden.water_storage, 97);
  t.end();
})

tape ('give_new_soil_all_increases_soil', function (t) {
  var garden = new Garden(100, 200);
  var plant = new Plant('tulip', 2, 2);
  garden.add_plants(plant);
  garden.give_new_soil_all();
  t.equal(garden.soil_storage, 199);
  t.end();
})

tape ('garden stats are printed', function (t){
  var garden = new Garden(100, 200);
  var plant = new Plant('tulip', 2, 2);
  garden.add_plants(plant);
  t.equal(garden.get_stats(), 'Number of plants: 1, Water stored: 100, Soil stored: 200');
  t.end();
})
