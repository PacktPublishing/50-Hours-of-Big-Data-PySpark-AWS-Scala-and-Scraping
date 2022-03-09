import scala.io.StdIn.readLine

object Main {

  def main(args: Array[String]): Unit = {

    foo(12,11,33);

  
  }


  def foo(b: Int, a:Int = 5, c:Int = 12, d:Int = 15): Unit = {

	  println(b);
	  
      println(a);
      println(c);
      println(d);

  }

}

