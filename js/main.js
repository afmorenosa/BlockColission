/**
* Get the canvas element
*/
var boxes = {
  element: document.getElementById("Draw"),
  width: 1000,
  height: 1000,

  init: function () {
    this.element.width = this.width;
    this.element.height = this.height;
    this.context = this.element.getContext("2d");
  },
};

boxes.init();

var my_system = new base_system(1, 10000, 50, 50, 830, 900, 0, -10);

function setFrictionReset () {

  boxes.context.clearRect(0, 0, boxes.width, boxes.height);
  my_system.draw(boxes);
  my_system.time_step_evolution();

  document.getElementById("Collisions").innerText = "Collisions " + my_system.coll_counter;

};
