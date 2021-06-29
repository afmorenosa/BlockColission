/**
* Create the system of two boxes.

* @param mass_1 {number} - Mass of the first box [Kg].
* @param mass_2 {number} - Mass of the second box [Kg].
* @param width_1 {number} - Width of the first box [m].
* @param width_2 {number} - Width of the second box [m].
* @param x0_1 {number} - Initial position of the first box [m].
* @param x0_2 {number} - Initial position of the second box [m].
* @param v0_1 {number} - Initial velocity of the first box [m/s].
* @param v0_2 {number} - Initial velocity of the second box [m/s].
* @param h {number} - Time step [s].
*/
var base_system = function (
  mass_1, mass_2,
  width_1, width_2,
  x0_1, x0_2,
  v0_1=0, v0_2=0,
  h=0.1
) {

  this.box_1 = new box(mass_1, width_1, x0_1, v0_1);
  this.box_2 = new box(mass_2, width_2, x0_2, v0_2);
  this.h = h;
  this.coll_counter = 0;

  /**
  * Test if the bloxes had collied.
  */
  this.box_collision = function () {
    border_box_pos_1 = this.box_1.x + this.box_1.width/2;
    border_box_pos_2 = this.box_2.x - this.box_2.width/2;

    if ((border_box_pos_2 - border_box_pos_1) <= 0) {
      return true;
    } else {
      return false;
    }

  };

  /**
  * Test if the boxes had collied.
  */
  this.wall_collision = function () {
    border_box_pos_1 = this.box_1.x - this.box_1.width/2;

    if ((border_box_pos_1) <= 0) {
      return true;
    } else {
      return false;
    }

  };

  /**
  * Make a step in time.
  */
  this.time_step_evolution = function () {
    this.box_1.x += this.h * this.box_1.v;
    this.box_2.x += this.h * this.box_2.v;

    if (this.box_collision()) {

      aux_v_1 = this.box_1.v;
      aux_v_2 = this.box_2.v;
      this.box_1.v = (aux_v_1 * (this.box_1.mass - this.box_2.mass) +
      2*aux_v_2*this.box_2.mass)/(this.box_1.mass + this.box_2.mass);
      this.box_2.v = (aux_v_2 * (this.box_2.mass - this.box_1.mass) +
      2*aux_v_1*this.box_1.mass)/(this.box_2.mass + this.box_1.mass);
      this.coll_counter += 1;

    } else if (this.wall_collision()) {

      this.box_1.v = -this.box_1.v;
      this.coll_counter += 1;

    }
  };

  /**
  * @param element {object} - the canvas object.
  */
  this.draw = function (element) {
    x_1_i = this.box_1.x + this.box_1.width/2;
    x_1_f = this.box_1.x - this.box_1.width/2;

    x_2_i = this.box_2.x + this.box_2.width/2;
    x_2_f = this.box_2.x - this.box_2.width/2;

    element.context.beginPath();
    // element.context.fillRect(
    //   x_1_i + element.width/2,
    //   0 + element.height/4,
    //   x_1_f + element.width/2,
    //   this.box_1.width + element.height/4
    // );
    element.context.arc(
      x_1_i,
      0 + element.height/2,
      this.box_1.width/2, 0, 2 * Math.PI
    );
    element.context.fillStyle = "#0000FF";
    element.context.fill();
    element.context.stroke();

    element.context.beginPath();
    element.context.fillStyle = "#FF0000";
    // element.context.fillRect(
    //   x_2_i,
    //   0 + element.height/4,
    //   x_2_f,
    //   this.box_2.width + element.height/4
    // );
    element.context.arc(
      x_2_i,
      0 + element.height/2,
      this.box_2.width/2, 0, 2 * Math.PI
    );
    element.context.fill();
    element.context.stroke();

  };

};
