import scala.io.StdIn.readLine
class Number(var value: Int)
{
  def printValue(): Unit = {
    print(value);
  }

  def sum(n: Number) : Int = {
    return value + n.value
  }

}


object Main {

  def main(args: Array[String]): Unit = 
  {
    var n1 = new Number(10);
    var n2 = new Number(20);
    


    println(n1.sum(n2));


  }
  

}

