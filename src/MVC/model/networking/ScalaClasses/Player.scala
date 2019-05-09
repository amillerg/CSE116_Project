

package MVC.model.networking.ScalaClasses

import MVC.model.networking.physics.{PhysicalObject, PhysicsVector}

class Player(inputlocation: PhysicsVector,
             inputvelocity: PhysicsVector,
             inputid: String) extends
          PhysicalObject(inputlocation,inputvelocity,inputid){
var playerloc = location
  var playervel = velocity
  var playerid = id
  var playerWidth = 64
  var playerHeight = 64
  var coins: Int = 1000

  var kills: Int = 0
  var deaths: Int = 0

  var health: Int = 3

  var bullets: List[PhysicalObject] = null

  val speed: Double = 4.0

  def move(direction: PhysicsVector){
    val normalDirection = direction.normal2d()
    this.velocity = new PhysicsVector(normalDirection.x * speed, normalDirection.y * speed)

  }

  def stop(): Unit ={
    this.velocity = new PhysicsVector(0, 0)
  }

}
