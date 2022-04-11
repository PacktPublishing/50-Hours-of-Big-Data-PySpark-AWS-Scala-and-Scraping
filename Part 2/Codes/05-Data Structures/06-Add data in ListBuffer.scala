import scala.io.StdIn.readLine
import scala.collection.mutable.ListBuffer

object Main {

  def main(args: Array[String]): Unit = 
  {

    var listBuffer = ListBuffer(1,2,3);
    println(listBuffer);

    listBuffer += 4;
    println(listBuffer);


    0 +=: listBuffer;
    println(listBuffer);


  }

}

