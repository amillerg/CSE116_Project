import MVC.model.ScalaClasses.Projectile
import MVC.model.physics.PhysicsVector

package MVC.model.ScalaClasses {

  import MVC.model.physics.PhysicalObject

  class Player(location: PhysicsVector,
               velocity: PhysicsVector,
               username: String) extends
            PhysicalObject(location,velocity){

    var playerWidth = 64
    var playerHeight = 64

    var coins: Int = 1000

    var kills: Int = 0
    var user_name = this.username
    var deaths: Int = 0

    var health: Int = 3

    var bullets: List[Projectile] = null

    val speed: Double = 4.0

    def move(direction: PhysicsVector){
      val normalDirection = direction.normal2d()
      this.velocity = new PhysicsVector(normalDirection.x * speed, normalDirection.y * speed)
    }

    def stop(): Unit ={
      this.velocity = new PhysicsVector(0, 0)
    }

  }

}
