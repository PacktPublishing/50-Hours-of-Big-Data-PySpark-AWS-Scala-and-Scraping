import scala.io.StdIn.readLine
import scala.collection.mutable.ListBuffer

object Main {

  def main(args: Array[String]): Unit = 
  {
    var listBuffer = ListBuffer(1,2,3,4,5);

    println(listBuffer(0));
    println(listBuffer(1));

    println("----------");


    for(w <- listBuffer)
    {
      println(w);
    }

  }

}

