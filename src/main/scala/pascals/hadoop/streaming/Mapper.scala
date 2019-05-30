package pascals.hadoop.streaming

import scala.io.StdIn


class Mapper(val separator: String = "\t",  val inputSource: StdIn.type = scala.io.StdIn) {

  def mapTask(): Unit = {
    inputSource.readLine.split(separator).toList match {
      case key :: value :: Nil =>
        println(s"$key$separator$value")
        println(s"$value$separator$key")
      case key :: values =>
        println(s"$key$separator${values.mkString(separator)}")
        values.foreach { value =>
          values.filterNot(elm => elm == value) match {
            case Nil =>
            case connections: List[String] =>
              println(s"$value$separator${connections.mkString(separator)}")
          }

        }
      case _ =>
    }
  }
}

object Mapper extends App {
  val mapper: Mapper = new Mapper("\t", StdIn)
  mapper.mapTask()

}
