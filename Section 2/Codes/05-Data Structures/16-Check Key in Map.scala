import scala.io.StdIn.readLine
import scala.collection.mutable.Map

object Main {

  def main(args: Array[String]): Unit = 
  {
    var map = Map("A"->"Apple", "B"->"Ball");

    if(map.contains("A"))
    {
      println("A is in the map");
    }
    if(map.contains("C"))
    {
      println("C is in the map");
    }


  }
  

}

