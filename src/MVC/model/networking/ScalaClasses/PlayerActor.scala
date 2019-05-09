package MVC.model.networking.ScalaClasses

import MVC.model.networking.physics.{PhysicalObject, PhysicsVector}
import akka.actor.Actor

case class shoot(projectile : PhysicalObject)

class PlayerActor(player: Player) extends Actor {

  def receive : Receive = {
    case message:shoot => player.bullets = message.projectile :: player.bullets
  }
}
