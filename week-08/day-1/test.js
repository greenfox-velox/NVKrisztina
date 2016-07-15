'use strict'

var countLetters = require('./01');
var tape = require('tape');

tape(function(t){
  t.deepEqual(countLetters.countLetters('apple'),{a: 1, p: 2, l: 1, e: 1});
  t.end();
})

var countLetters2 = require('./01_without_if');
var tape = require('tape');

tape(function(k){
  k.deepEqual(countLetters.countLetters('apple'),{a: 1, p: 2, l: 1, e: 1});
  k.end();
})

var countBooksFunction = require('./02');
var tape = require('tape');

tape(function(k){
  k.deepEqual(countBooksFunction.countBooksFunction(),4);
  k.end();
})

var Rectangle = require('./03');
var tape = require('tape');

tape(function(l){
  l.deepEqual(Rectangle.Rectangle.getArea(10, 5),50);
  l.end();
})
