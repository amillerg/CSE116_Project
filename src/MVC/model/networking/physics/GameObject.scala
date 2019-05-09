package MVC.model.networking.physics

class GameObject {

  var destroyed: Boolean = false

  def destroy(): Unit = {
    destroyed = true
  }

}
