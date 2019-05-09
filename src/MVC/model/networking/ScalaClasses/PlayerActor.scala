package MVC.model.networking.ScalaClasses

import MVC.model.networking.physics.{PhysicalObject, PhysicsVector}
import akka.actor.Actor

case class shoot(projectile : PhysicalObject)

class PlayerActor(location:PhysicsVector,
                  velocity:PhysicsVector,
                  id:String) extends Actor {

  var player = new Player(location,velocity,id)

  def receive : Receive = {
    case message:shoot => player.bullets = message.projectile :: player.bullets
  }
}
