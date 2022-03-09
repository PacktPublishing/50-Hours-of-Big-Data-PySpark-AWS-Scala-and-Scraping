import scala.io.StdIn.readLine

object Main {
  def main(args: Array[String]): Unit = {


      //2
      //4
      //6
      //1
      //2


      var sum = 0;

      for(w <- 1 to 5)
      {
        var x = readLine("Enter number: ");
        var num = x.toInt;

        sum = sum + num;
        println(sum);

      }

      println(sum);

   }
}
