import scala.io.StdIn.readLine
import scala.collection.mutable.Map

object Main {

  def main(args: Array[String]): Unit = 
  {
    var m = Map("A" -> "Apple", "B" -> "Ball", "C"->"Cat");
    println(m);
    println(m("A"));
    println(m("B"));
    println(m("C"));

  }
  

}

