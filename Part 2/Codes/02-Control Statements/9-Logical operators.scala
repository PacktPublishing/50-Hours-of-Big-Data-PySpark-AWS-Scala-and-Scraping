import scala.io.StdIn.readLine

object Main {
  def main(args: Array[String]): Unit = {
   
    
    println(1<2);
    println(1>2);


    println(1 <  2 && 1 < 5);
    println(1 >  2 && 1 < 5);
    println(1 >  2 && 1 > 5);


    println(1 < 2 || 1 < 5);
    println(1 > 2 || 1 < 5);
    println(1 < 2 || 1 > 5);
    println(1 > 2 || 1 > 5);


    println( !(1 < 2) );
    println( !(1 > 2) );
    println(!(1 <  2 && 1 < 5));
    println(!(1 > 2 || 1 > 5));

  }
}
