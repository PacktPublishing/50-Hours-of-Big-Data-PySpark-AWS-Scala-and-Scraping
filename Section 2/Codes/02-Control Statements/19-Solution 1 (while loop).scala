import scala.io.StdIn.readLine

object Main {
  def main(args: Array[String]): Unit = {

    var x = readLine("Enter marks: ");
    var marks = x.toInt;
    


    println(marks < 0 && marks > 100)
    println(marks < 0 || marks > 100)

    while(marks < 0)
    {
        x = readLine("Enter marks: ");
        marks = x.toInt;
    }

    while(marks > 100)
    {
      x = readLine("Enter marks: ");
      marks = x.toInt;
    }
 





  }
}
