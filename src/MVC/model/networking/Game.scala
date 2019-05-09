package MVC.model.networking


import MVC.model.networking.ScalaClasses.Player
import MVC.model.networking.physics.{PhysicalObject, Physics, PhysicsVector, World}
import play.api.libs.json.{JsValue, Json}

import scala.collection.immutable.ListMap

class Game {

  var players: Map[String, Player] = Map()
  var playerSize = 4

  var world = new World(10)
  val startingVector = new PhysicsVector(300,600)
  var projectiles: List[PhysicalObject] = List[PhysicalObject]()

  var lastUpdateTime: Long = System.nanoTime()

  def update(): Unit = {
    val time: Long = System.nanoTime()
    val dt = (time - this.lastUpdateTime) / 1000000000.0
    Physics.updateWorld(this.world, dt)
    checkForPlayerHits()
    projectiles = projectiles.filter(po => !po.destroyed)
    this.lastUpdateTime = time
  }


  def addPlayer(id: String): Unit = {
    println(id+"player added into game")
    val player = new Player(startingVector, new PhysicsVector(0, 0), id)
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

  def gamestate(): String = {
    val gameState: Map[String, JsValue] = Map(
      "players" -> Json.toJson(this.players.map({ case (k, v) => Json.toJson(Map(
        "x" -> Json.toJson(v.location.x),
        "y" -> Json.toJson(v.location.y),
        "v_x" -> Json.toJson(v.velocity.x),
        "v_y" -> Json.toJson(v.velocity.y),
        "width" -> Json.toJson(64),
        "height" -> Json.toJson(64),
        "username" -> Json.toJson(v.playerid),
        "kills" -> Json.toJson(v.kills),
        "health" -> Json.toJson(v.health),
        "coins" -> Json.toJson(v.coins),
        "id" -> Json.toJson(k)))
      })),
      "projectiles" -> Json.toJson(this.projectiles.map({ po => Json.toJson(Map("x" -> po.location.x, "y" -> po.location.y)) }))
    )

    Json.stringify(Json.toJson(gameState))
  }

  def buy_life(mouse: PhysicsVector): Boolean = {
    var x: Double = mouse.x
    var y: Double = mouse.y
    if (x < 1150 & x > 100 & y > 350 & y < 420) {
      true
    } else {
      false
    }
  }

  def buy_a_life(ship: Player): Unit = {
    ship.health = ship.health + 1
    ship.coins -= 200
  }

  def topPlayers(playerList: List[Player]): List[String] = { //takes list of all players, returns list of usernames from first to last place
    var top: List[String] = List()
    var kds: Map[String, Double] = Map()
    var kd: scala.collection.immutable.Map[String, Double] = kds
    var ratio: Double = 0.0
    for (p <- playerList) {
      ratio = p.kills / p.deaths
      kds += (p.playerid -> ratio)
    }
    var x = ListMap(kd.toSeq.sortWith(_._2 > _._2): _*)
    for (i <- x.keys) {
      top :+= i
    }
    top
  }

  def checkForPlayerHits(): Unit = {
    val vec: PhysicsVector = startingVector
    for (i <- projectiles) {
      var proj: PhysicsVector = new PhysicsVector(i.location.x, i.location.y, 0)
      for (p <- players.values) {
        var dist: Double = p.location.distance2d(proj)
        if (dist < playerSize) {
          p.location.x = vec.x
          p.location.y = vec.y
          i.destroy()
        }
      }
    }

    def checkHit(): Unit = {
      for (b <- projectiles) {
        var proj: PhysicsVector = new PhysicsVector(b.location.x, b.location.y)
        for (p <- players.values) {
          var dist: Double = p.location.distance2d(proj)
          if (dist < playerSize) {
            p.health -= 1
            if (p.health == 0) { //if the player is killed
              p.deaths += 1
              p.coins = 0
              p.health = 3
              p.location = startingVector
              //var shooter: Player = players(b.id )
              players(b.id).coins += 100
              players(b.id).kills += 1
            }
          }
        }
      }
    }

  }

}
