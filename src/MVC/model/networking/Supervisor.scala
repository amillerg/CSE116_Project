package MVC.model.networking
import MVC.model.networking.ScalaClasses.Projectile
import MVC.model.networking._
import MVC.model.networking.physics.{PhysicalObject, PhysicsVector}
import akka.actor.{Actor, ActorRef, ActorSystem, Props}


//the game actor
class Supervisor(actorSystem : ActorSystem) extends Actor {

  // this will be my game :)
  var game = new Game()
  var playerActors: Map[String,ActorRef] = Map()


  for ((id,player)<-game.players) {
    playerActors = playerActors +
      (id -> actorSystem.actorOf(Props(classOf[PlayerActor],
        player.location,player.velocity,player.playerid)))
    }

  var total: Int = playerActors.values.size
  var done: Int = 0
  var notDone: Int = 0
  def receive: Receive = {
    case message: AddPlayer => game.addPlayer(message.username)
    case message: RemovePlayer => game.removePlayer(message.username)
    case message: MovePlayer => game.players(message.username).move(new PhysicsVector(message.x, message.y))
    case message: StopPlayer => game.players(message.username).stop()

    case UpdateGame =>
      game.update()

    case SendGameState => sender() ! GameState(game.gamestate())

    case projectile: AddProjectile =>
      val location = new PhysicsVector(projectile.x, projectile.y, projectile.z)
      val velocity = new PhysicsVector(projectile.xVelocity, projectile.yVelocity, projectile.zVelocity)
      //game.projectiles += new Projectile(location, velocity,projectile.username)
      val proj: PhysicalObject = new Projectile(location, velocity, projectile.username)
      game.projectiles = proj :: game.projectiles

  }
}


