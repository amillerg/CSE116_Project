package MVC.model.ScalaClasses {

  import MVC.model.physics.{PhysicalObject, PhysicsVector}

  class Projectile(location : PhysicsVector, velocity: PhysicsVector, radius : Double, direction: Int, user: String) extends PhysicalObject(location,velocity) {

    val vel = 10 * direction

    //var mouselocation

    //var angle_bullet
  }

}
