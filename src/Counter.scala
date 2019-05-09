
case class Start()
case class IsDone()
case class Done()
case class NotDone()
class numberClass(num: String){
var number = num
}
class Counter(name: String) extends Actor {
    var n = 0
    def countDown(): Unit = {
      if (n >= 0) {
        println(this.name + " - " + n)
        n -= 1
        countDown()
      } else {
        println(this.name + " finished")
      }
    }
    def receive: Receive = {
      case Start =>
        this.n = 20
        countDown()
      case IsDone =>
        if (n <= 0) {
          //sender is my "game" / supervisor
          sender() ! Done
        } else {
          sender() ! NotDone
        }
    }
  }
