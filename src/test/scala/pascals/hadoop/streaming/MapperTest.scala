package pascals.hadoop.streaming


import org.scalatest.{FunSuite, Matchers}

import scala.io.StdIn

class MapperTest extends FunSuite with Matchers {

  val mapper = new Mapper("\t", StdIn)



}
