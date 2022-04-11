import scala.io.StdIn.readLine

object Main {
  def main(args: Array[String]): Unit = {
   
    var x = readLine("Enter age: ");
    var age = x.toInt;

    if (age > 13)
    {
      var specialCard = readLine("Do you want a special card?");
      if (specialCard == "Yes")
      {
        println("Welcome to PlayLand with special card");
      }     
      else
      {
        println("Welcome to playLand");

      } 
    }
    else
    {
      println("You are under age and you are not allowed.");
    }

  }
}
