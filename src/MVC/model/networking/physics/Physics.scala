package MVC.model.networking.physics

object Physics {
  def computePotentialLocation(physicsObj : PhysicalObject,dt : Double) : PhysicsVector = {
    var x = physicsObj.location.x + (physicsObj.velocity.x * dt)
    var y = physicsObj.location.y + (physicsObj.velocity.y * dt)
    var z = physicsObj.location.z + (physicsObj.velocity.z * dt)
    if (z < 0 ) {
      z = 0
    }
    var hello = new PhysicsVector(x,y,z)
    hello
  }

  def updateVelocity(physicsObj : PhysicalObject, world : World, dt : Double) : Unit = {
    val gravity = world.gravity


    if (physicsObj.location.z == 0 && (physicsObj.velocity.z < 0 )){
      physicsObj.velocity.z = 0.0
    } else {

      val z = physicsObj.velocity.z - (gravity * dt)

      if (z < 0 && physicsObj.location.z == 0){
        physicsObj.velocity.z = 0
      }
      else {physicsObj.velocity.z = z}
    }
  }

  def detectCollision(physicalObj : PhysicalObject,
                      physicalVec : PhysicsVector,
                      boundary : Boundary) : Boolean = {
    var answer = false
    // current location is (x1, y1)
    var x1 = physicalObj.location.x
    var y1 = physicalObj.location.y

    // potential location is (x2, y2)
    var x2 = physicalVec.x
    var y2 = physicalVec.y

    // start boundary
    var startX = boundary.start.x
    var startY = boundary.start.y

    // end boundary
    var endX = boundary.end.x
    var endY = boundary.end.y

    // mutual interval where they could potentially intersect
    // list of two numbers : List(0) is start, List(1) is end
    var mutualInterval = List(Math.max(Math.min(x1,x2),Math.min(startX,endX)),
      Math.min(Math.max(x1,x2),Math.max(startX,endX)))

    // if the two segments are on two different x intervals,
    // they definitely don't intersect
    if (Math.max(x1,x2)<Math.min(startX, endX)){
      answer = true
    }
    else {
      var objSlope = 0.0
      var boundarySlope = 0.0
      var b1 = 0.0
      var b2 = 0.0

      if ((x1 - x2 == 0) &&
        (x1 > Math.min(startX,endX)) &&
        (x1 < Math.max(startX,endX))){
        answer = false
      }
      else if ( (startX - endX == 0) &&
        (startX > Math.min(x1,x2)) &&
        (startX < Math.max(x1,x2))) {
        answer = false
      } else {
        objSlope = (y2 - y1) / (x2 - x1)
        boundarySlope = (endY - startY) / (endX - startX)
        b1 = y1 - (objSlope*x1)
        b2 = endY - (boundarySlope*endX)
        if (objSlope == boundarySlope) { answer = true}
        else {
          var Xa = (b2 - b1) / (objSlope - boundarySlope)
          if((Xa < Math.max(Math.min(x1,x2),Math.min(startX,endX))) ||
             (Xa > Math.min(Math.max(x1,x2),Math.max(startX,endX)))){
            answer = true
          }
          else {answer = false}
        }
      }
    }
    answer
  }

  def updateWorld(world : World, dt : Double): Unit = {
    for (obj <- world.objects) {
      updateVelocity(obj, world,dt)
      var newLocation = computePotentialLocation(obj, dt)
      var tester = true
      var done = false
      var i = world.boundaries.length - 1
      while (( i >= 0) && (!done)){
        var bound = world.boundaries(i)
        if (detectCollision(obj,newLocation,bound )== false){
          tester = false
          done = true
        }
        i = i -1
      }
      if (tester){
        obj.location.x = newLocation.x
        obj.location.y = newLocation.y
        obj.location.z = newLocation.z

      } else{
        obj.location.z = newLocation.z
      }
    }
  }
}
