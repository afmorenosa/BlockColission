/**
* Create a squared box.

* @param mass {number} - The mass of the box [Kg].
* @param width {number} - The width of the box [m].
* @param x0 {number} - The initial position [m].
* @param v0 {number} - The initial velocity [m/s].
*/
var box = function (mass, width, x0, v0=0) {
  this.mass = mass;
  this.width = width;
  this.v = v0;
  this.x = x0;

  return this;
};
