package MVC.model

import MVC.model.physics.{PhysicalObject, World}
import play.api.libs.json.{JsValue, Json}
import scala.collection.immutable.ListMap
import ScalaClasses._
import physics._

class Game {


  var world : World = new World(10)

  var projectiles: List[Projectile] = List()

  var players: Map[String, Player] = Map()
  val playerSize: Double = 32

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
    val vec: PhysicsVector = startingVector()
    for(i<-projectiles){
      var proj: PhysicsVector = new PhysicsVector(i.location.x, i.location.y, 0)
      for(p<-players.values){
        var dist: Double = p.location.distance2d(proj)
        if(dist < playerSize){
          p.location.x = vec.x
          p.location.y = vec.y
          i.destroy()
        }
      }
    }
    // TODO: Objective 3
    //players.values.foreach(player=>hit(player))
  }

  def checkHit(): Unit={
      for(b<-projectiles) {
        var proj: PhysicsVector = new PhysicsVector(b.location.x, b.location.y)
        for (p <- players.values){
          var dist: Double = p.location.dist(proj)
          if(dist<playerSize){
            p.health -= 1
            if(p.health == 0){ //if the player is killed
              p.deaths += 1
              p.coins = 0
              p.health = 3
              p.location.x = 600 //resets location to starting point
              p.location.y = 300
              var shooter: Player = players(b.user)
              shooter.coins += 100
              shooter.kills += 1
            }
          }
        }
      }
  }



  def buy_life(mouse: PhysicsVector): Boolean={
    var x: Double = mouse.x
    var y: Double = mouse.y
    if(x<1150 & x>100 & y>350 & y<420){
      true
    }else{
      false
    }
  }

  def buy_a_life(ship: Player): Unit={
    ship.health= ship.health + 1
    ship.coins -= 200
  }

  def topPlayers(playerList: Map[String, Player]): List[String] ={ //takes list of all players, returns list of usernames from first to last place
    var top: List[String] = List()
    var kds: Map[String, Double] = Map()
    var kd: scala.collection.immutable.Map[String,Double] = kds
    var ratio: Double = 0.0
    for(p<-playerList.values){
      ratio = p.kills/p.deaths
      kds += (p.user -> ratio)
    }
    var x = ListMap(kd.toSeq.sortWith(_._2 > _._2):_*)
    for(i<-x.keys){
      top :+= i
    }
    top
  }


}
