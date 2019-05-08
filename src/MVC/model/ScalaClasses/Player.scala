import MVC.model.ScalaClasses.Projectile

package MVC.model.ScalaClasses {

  class Player(x: Double, y: Double, playerWidth: Double = 64, playerHeight: Double = 64, username: String) {
    val vel = 14

    var coins: Int = 1000

    var kills: Int = 0

    var deaths: Int = 0

    var health: Int = 3

    var bullets: List[Projectile] = null

  }

}
