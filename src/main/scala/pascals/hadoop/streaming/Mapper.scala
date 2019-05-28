package pascals.hadoop.streaming

object Mapper extends App {
  val separator: String = "\t"
  scala.io.StdIn.readLine.split(separator).toList match {
    case key :: value :: Nil =>
      println(s"$key$separator$value")
      println(s"$value$separator$key")
    case key :: values =>
      println(s"$key$separator${values.mkString(separator)}")
      values.foreach{ value =>
        values.filterNot(elm => elm == value) match {
          case Nil =>
          case connections: List[String] =>
            println(s"$value$separator${connections.mkString(separator)}")
        }

      }
    case _ =>
  }

}
