package pascals.hadoop.streaming

import scala.io.StdIn

class Reducer(val separator: String = "\t",  val inputSource: StdIn.type = scala.io.StdIn) {

  var key: String = _
  var aggregate_network: Set[String] = _
  var connections: (String, Set[String]) = _
  def reduceTask(): Unit = {

    inputSource.readLine.split(separator).toList match {
      case node :: values =>
        connections = Tuple2(node, values.toSet)
        if (key == node) {
          aggregate_network = aggregate_network.union(values.toSet)
        }
        else {
          if (key != null) {
            /* If a new key is encountered, print out the aggregated state of the previous key first*/
            println(s"$key$separator${aggregate_network.toList.sorted.mkString(separator)}")
          }
          aggregate_network = values.toSet
          key = node
        }
    }

    if (key == connections._1) {
      /*The if may not be required*/
      println(s"$key$separator${aggregate_network.toList.sorted.mkString(separator)}")
    }
  }
}

object Reducer extends App {
  val reducer = new Reducer("\t", StdIn)
  reducer.reduceTask()
}
