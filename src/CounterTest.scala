


object CounterTest extends App {


    val actorSystem = ActorSystem()

    import scala.concurrent.duration._

    val mylist: List[numberClass] = List(new numberClass("4"),
      new numberClass("5"), new numberClass("7"))
    /*val one = system.actorOf(Props(classOf[Counter], "1"))
  val two = system.actorOf(Props(classOf[Counter], "2"))
  val three = system.actorOf(Props(classOf[Counter], "3"))*/

    val new_list = for (numberclass <- mylist) yield {
      actorSystem.actorOf(Props(classOf[Counter], numberclass.number))
    }

    val supervisor = actorSystem.actorOf(Props(classOf[Supervisor], actorSystem))

    // two ways of doing it :

    //1
    /*for (item<- new_list){
    item ! Start
  }*/
    //2
    new_list.foreach((f: ActorRef) => f ! Start)


  actorSystem.scheduler.schedule(0.milliseconds, 500.milliseconds, supervisor, Update)

  }

