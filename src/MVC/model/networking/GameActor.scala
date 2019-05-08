package MVC.model.networking


import akka.actor.{Actor, ActorRef, PoisonPill, Props}
import MVC.model.ScalaClasses.Projectile
import MVC.model.physics.PhysicsVector


class GameActor extends Actor {
  var players: Map[String, ActorRef] = Map()
  var towers: List[ActorRef] = List()

  val game: Game = new Game()


  override def receive: Receive = {
    case message: AddPlayer => game.addPlayer(message.username)
    case message: RemovePlayer => game.removePlayer(message.username)
    case message: MovePlayer => game.players(message.username).move(new PhysicsVector(message.x, message.y))
    case message: StopPlayer => game.players(message.username).stop()

    case UpdateGame =>
      game.update()

    case SendGameState => sender() ! GameState(game.gameState())
    case projectile: AddProjectile =>
      val location = new PhysicsVector(projectile.x, projectile.y, projectile.z)
      val velocity = new PhysicsVector(projectile.xVelocity, projectile.yVelocity, projectile.zVelocity)
      game.addProjectile(new Projectile(location, velocity)
  }
}
