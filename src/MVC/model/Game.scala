package MVC.model

import MVC.model.physics.{PhysicalObject, World}
import play.api.libs.json.{JsValue, Json}


class Game {


  var world : World = new World(10)

  var projectiles: List[PhysicalObject] = List()

  var players: Map[String, Player] = Map()
  val playerSize: Double = 0.3

  var lastUpdateTime: Long = System.nanoTime()



  def addPlayer(id: String): Unit = {
    val player = new Player(startingVector(), new PhysicsVector(0, 0))
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


  def startingVector(): PhysicsVector = {
    new PhysicsVector(level.startingLocation.x + 0.5, level.startingLocation.y + 0.5)
  }



  def update(): Unit = {
    val time: Long = System.nanoTime()
    val dt = (time - this.lastUpdateTime) / 1000000000.0
    Physics.updateWorld(this.world, dt)
    checkForPlayerHits()
    checkForBaseDamage()
    projectiles = projectiles.filter(po => !po.destroyed)
    this.lastUpdateTime = time
  }

  def gameState(): String = {
    val gameState: Map[String, JsValue] = Map(
      "gridSize" -> Json.toJson(Map("x" -> level.gridWidth, "y" -> level.gridHeight)),
      "start" -> Json.toJson(Map("x" -> level.startingLocation.x, "y" -> level.startingLocation.y)),
      "base" -> Json.toJson(Map("x" -> level.base.x, "y" -> level.base.y)),
      "baseHealth" -> Json.toJson(baseHealth),
      "maxBaseHealth" -> Json.toJson(level.maxBaseHealth),
      "walls" -> Json.toJson(this.walls.map({ w => Json.toJson(Map("x" -> w.x, "y" -> w.y)) })),
      "towers" -> Json.toJson(this.towers.map({ t => Json.toJson(Map("x" -> t.x, "y" -> t.y)) })),
      "players" -> Json.toJson(this.players.map({ case (k, v) => Json.toJson(Map(
        "x" -> Json.toJson(v.location.x),
        "y" -> Json.toJson(v.location.y),
        "v_x" -> Json.toJson(v.velocity.x),
        "v_y" -> Json.toJson(v.velocity.y),
        "id" -> Json.toJson(k))) })),
      "projectiles" -> Json.toJson(this.projectiles.map({ po => Json.toJson(Map("x" -> po.location.x, "y" -> po.location.y)) }))
    )

    Json.stringify(Json.toJson(gameState))
  }

  def check(player: Player): Unit = {
    val centerX = level.base.x + .5
    val centerY = level.base.y + .5
    val distanceX = scala.math.abs(player.location.x - centerX)
    val distanceY = scala.math.abs(player.location.y - centerY)
    val distance = scala.math.pow(scala.math.pow(distanceX, 2) + scala.math.pow(distanceY, 2),.5)
    if (distance < this.playerSize){
      player.location = startingVector()
      this.baseHealth -= 1
    }
  }

  def checkForBaseDamage(): Unit = {
    // TODO: Objective 1
    players.values.foreach(player => check(player))

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
