import scala.io.StdIn.readLine

object Main {

  def main(args: Array[String]): Unit = {
    var inc = (x:Int) => x + 1;  
    var x = inc(4);
    println(x);

    var mul = (x:Int, y:Int) => x*y;
    println(mul(2,4))
  
  }

 

}

