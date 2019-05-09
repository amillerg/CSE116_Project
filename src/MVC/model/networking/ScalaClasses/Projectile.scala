package MVC.model.networking.ScalaClasses

import MVC.model.networking.physics.{PhysicalObject, PhysicsVector}

class Projectile(location: PhysicsVector, velocity: PhysicsVector,  id: String) extends PhysicalObject(location,velocity,id) {
  var radius : Int = 6
  var direction : Int = 1
  val vel = 10 * direction
  val shooter = id
  //var mouselocation

  //var angle_bullet
}
