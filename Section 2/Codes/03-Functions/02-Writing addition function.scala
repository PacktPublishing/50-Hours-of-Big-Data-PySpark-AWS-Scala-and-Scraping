import scala.io.StdIn.readLine

object Main {

  def main(args: Array[String]): Unit = {
    
      println(addition(5,6));
      println(addition(2,2));
      println(addition(9,9));
      
   }




  def addition(a: Int, b: Int) : Int = {
    var sum = a + b;
    return sum;
  }



}
