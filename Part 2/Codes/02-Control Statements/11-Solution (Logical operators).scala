import scala.io.StdIn.readLine

object Main {
  def main(args: Array[String]): Unit = {
   
      var x = readLine("Enter age: ");
      var age = x.toInt;

      var y = readLine("Enter height: ");
      var height = y.toInt;


      if (age > 13 && height >= 5)
      {
         F println("Welcome to the PlayLand");

      }
      else
      {
          println("You are not allowed");
      }


  }
}
