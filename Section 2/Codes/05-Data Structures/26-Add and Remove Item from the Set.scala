import scala.io.StdIn.readLine
import scala.collection.mutable

object Main {

  def main(args: Array[String]): Unit = 
  {
      var s = Set[Int]();

      s += 1;
      s += 2;
      s += 1;
      s += 3;
      println(s);

      s -= 1;
      s -= 4;
      println(s);



  }
  

}

