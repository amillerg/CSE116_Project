package MVC.model

import MVC.model.physics.PhysicsVector
import akka.actor.{Actor, ActorRef}
import akka.io.Tcp.{Connected, Register}
/*
class gameActor extends Actor {

  override def receive: Receive = {

    case message: AddPlayer => game.addPlayer(message.username)
    case message: RemovePlayer => game.removePlayer(message.username)
    case message: MovePlayer => game.players(message.username).move(new PhysicsVector(message.x, message.y))
    case message: StopPlayer => game.players(message.username).stop()

    case UpdateGame =>
      game.update()
      if (game.baseHealth <= 0) {
        game.baseHealth = 2
        levelNumber = (levelNumber + 1) % 3
        loadLevel(levelNumber)
      }
    case SendGameState => sender() ! GameState(game.gameState())
    case projectile: AddProjectile =>
      val location = new PhysicsVector(projectile.x, projectile.y, projectile.z)
      val velocity = new PhysicsVector(projectile.xVelocity, projectile.yVelocity, projectile.zVelocity)
      game.addProjectile(new Projectile(location, velocity))

  }

}
*/