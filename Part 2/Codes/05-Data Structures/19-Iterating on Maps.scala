import scala.io.StdIn.readLine
import scala.collection.mutable.Map

object Main {

  def main(args: Array[String]): Unit = 
  {

    var map = Map("A"->"Apple","B"->"Ball");

    for((k,v) <- map)
    {
      println(k);
      println(v);
      println("-----------------");

    }


  }
  

}

