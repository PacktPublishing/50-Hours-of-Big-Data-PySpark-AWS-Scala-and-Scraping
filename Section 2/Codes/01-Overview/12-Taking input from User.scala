import scala.io.StdIn.readLine

object Main {
  def main(args: Array[String]): Unit = {

      var x = readLine("Enter number 1 ");
      var y = readLine("Enter number 2 ");
      var num1 = x.toInt;
      var num2 = y.toInt;


      var z = num1 + num2;

      println(z);
      println(z.getClass.getName);

  }
}
