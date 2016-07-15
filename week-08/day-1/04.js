'use strict';

function Car(type, color, balance){
  this.type = type;
  this.color = color;
  this.balance = balance;
  this.id = 0;
  this.enter = function(enterDate){
    this.enterDate = enterDate;
  }
  this.getEnterDate = function(){
    return enterDate;
  }
  this.leave = function(price){
    this.balance -= price;
  }
  this.getStats = function(){
    return 'Type: '+'this.type'+' Color: '+'this.color'+' Balance: '+'this.balance'
  }
}

var fee = 40;

function CarPark(income, startTime){
  this.income = income;
  this.startTime = startTime;
  this.carList = [];
}

CarPark.prototype.careEnter = function(car){
  this.carlist.push(car, car.this.startTime);
}

CarPark.prototype.carLeave = function(id){
  this.carlist.push(car);
}

CarPark.prototype.elapseTime = function(hours){
  this.startTime += hours;
}
