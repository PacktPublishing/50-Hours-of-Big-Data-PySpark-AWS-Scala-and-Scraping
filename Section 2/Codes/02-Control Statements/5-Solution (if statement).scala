import scala.io.StdIn.readLine

object Main {
  def main(args: Array[String]): Unit = {
   
    var x = readLine("Enter your age: ");
    var age = x.toInt;


    if(age > 13)
    {
      println("Welcome to PlayLand, You can enter the gate.");
    }
    else
    {
      println("Welcome to PlayLand but you are not allowed to move further.");
    }

  }
}
