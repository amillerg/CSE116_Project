package MVC.model.networking

import MVC.model.physics.{PhysicalObject, Physics, PhysicsVector, World}
import MVC.model.ScalaClasses.Player
import play.api.libs.json.{JsValue, Json}


class Game {

  val startingVector = new PhysicsVector(112,222)

  var world : World = new World(10)

  var projectiles: List[PhysicalObject] = List()

  var players: Map[String, Player] = Map()
  val playerSize: Double = 0.3

  var lastUpdateTime: Long = System.nanoTime()



  def addPlayer(id: String): Unit = {
    val player = new Player(startingVector, new PhysicsVector(0, 0),"test_username")
      players += (id -> player)
    world.objects = player :: world.objects
  }


  def removePlayer(id: String): Unit = {
    players(id).destroy()
    players -= id
  }





  def addProjectile(projectile: PhysicalObject): Unit = {
    projectiles = projectile :: projectiles
    world.objects = projectile :: world.objects
  }



  def update(): Unit = {
    val time: Long = System.nanoTime()
    val dt = (time - this.lastUpdateTime) / 1000000000.0
    Physics.updateWorld(this.world, dt)
    checkForPlayerHits()
    projectiles = projectiles.filter(po => !po.destroyed)
    this.lastUpdateTime = time
  }

  def gameState(): String = {
    val gameState: Map[String, JsValue] = Map(
       "players" -> Json.toJson(this.players.map({ case (k, v) => Json.toJson(Map(
        "x" -> Json.toJson(v.location.x),
        "y" -> Json.toJson(v.location.y),
        "v_x" -> Json.toJson(v.velocity.x),
        "v_y" -> Json.toJson(v.velocity.y),
         "width"-> Json.toJson(64),
         "height" -> Json.toJson(64),
         "username"-> Json.toJson(v.user_name),
         "kills" -> Json.toJson(v.kills),
         "health"->Json.toJson(v.health),
         "coins"->Json.toJson(v.coins),
         "id" -> Json.toJson(k))) })),
      "projectiles" -> Json.toJson(this.projectiles.map({ po => Json.toJson(Map("x" -> po.location.x, "y" -> po.location.y)) }))
    )

    Json.stringify(Json.toJson(gameState))
  }



  def hit(player: Player): Unit ={
    for (proj<- projectiles) {
      // val centerX = proj.location.x
      // val centerY = proj.location.y
      val distance = player.location.distance2d(proj.location)
      // val distanceX = scala.math.abs(player.location.x - centerX)
      // val distanceY = scala.math.abs(player.location.y - centerY)
      // val distance = scala.math.pow(scala.math.pow(distanceX, 2) + scala.math.pow(distanceY, 2), .5)
      if (distance < this.playerSize) {
        proj.destroy()
        player.location = startingVector()
      }
    }
  }
  def checkForPlayerHits(): Unit = {
    // TODO: Objective 3
    players.values.foreach(player=>hit(player))
  }


}
