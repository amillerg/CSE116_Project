package MVC.model.networking

import MVC.model.networking.ScalaClasses.Player
import MVC.model.networking.physics.PhysicsVector
import akka.actor.{Actor, ActorRef}

class PlayerActor(gameActor : ActorRef,
                  location : PhysicsVector,
                  velocity : PhysicsVector,
                  username : String) extends Actor{

  import context.dispatcher
  import scala.concurrent.duration._

  //val tower: DodgeBallTower = new DodgeBallTower(x, y)
  val player : Player = new Player(location, velocity, username)
  // start firing as soon as tower is created
  gameActor ! SendGameState

  var gameState: String = ""

  override def receive: Receive = {
    case Fire =>
      if(gameState != "") {
        /*val projectiles = tower.fire(gameState)
        //        val projectiles = tower.aimFire(gameState)

        projectiles.foreach(proj => gameActor ! AddProjectile(proj.location.x, proj.location.y, proj.location.z, proj.velocity.x, proj.velocity.y, proj.velocity.z))
      */
      }

      // fire again in 1 second
      context.system.scheduler.scheduleOnce(1000.milliseconds, gameActor, SendGameState)

    case gs: GameState =>
      gameState = gs.gameState
      self ! Fire
  }

}
