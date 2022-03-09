import scala.io.StdIn.readLine

object Main {

  def main(args: Array[String]): Unit = {

    var x = "Hello ";
    var y = "World";
    println(concatination(x,y));

  }

  def concatination(str1: String, str2: String) : String= {

    return str1 + str2;
  }

}

