package MVC.model.networking

import java.net.InetSocketAddress

import akka.actor.{Actor, ActorRef}
import akka.io.{IO, Tcp}
import akka.util.ByteString

case class SendToServer(message: String)

class SocketClient(remote: InetSocketAddress) extends Actor {

  import akka.io.Tcp._
  import context.system

  IO(Tcp) ! Connect(remote)
  var server: ActorRef = _

  override def receive: Receive = {
    case c: Connected =>
      println("Connected to: " + remote)
      this.server = sender()
      this.server ! Register(self)
    case r: Received =>
      println("Received: " + r.data.utf8String)
    case send: SendToServer =>
      println("Sending: " + send.message)
      if (server != null) {
        this.server ! Write(ByteString(send.message))
      }
  }
}
