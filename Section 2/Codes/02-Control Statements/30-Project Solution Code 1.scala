import scala.io.StdIn.readLine

object Main {
  def main(args: Array[String]): Unit = {

    var X = 50;
    
    for(w<- 1 to 5)
    {
      var x = readLine("Enter your guess: ");
      var guess = x.toInt;

      if(guess < X)
      {
        println("Your guess is less than the actual number.");
        println(5-w);
      }
      else if (guess > X)
      {
        println("Your guess is greater than the actual number.");
        println(5-w);
      }
      else
      {
        println("You won.");
        println(w);
      }


    }


        
   }
}
