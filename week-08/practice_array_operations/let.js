//stackoverflow
//The difference is scoping. var is scoped to the nearest function
//block and let is scoped to the nearest enclosing block
//(both are global if outside any block), which can be smaller than
//a function block.
//let is only visible in the for() loop and var is visible to the
//whole function
'use strict';


function allyIlliterate() {
    //tuce is *not* visible out here
    for( let tuce = 0; tuce < 5; tuce++ ) {
        //tuce is only visible in here (and in the for() parentheses)
    };
    //tuce is *not* visible out here
};

function byE40() {
    //nish *is* visible out here
    for( var nish = 0; nish < 5; nish++ ) {
        //nish is visible to the whole function
    };
    //nish *is* visible out here
};
