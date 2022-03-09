import scala.io.StdIn.readLine
class Number(var value: Int)
{
  def printValue(): Unit = {
    print(value);
  }

  def sum(n: Number) : Int = {
    return value + n.value
  }

  def isGreater(n: Number): Boolean = {

    if (n.value > value)
    {
      return true;
    }
    else
    {
      return false;
    }
  }

  
}


object Main {

  def main(args: Array[String]): Unit = 
  {
    var n1 = new Number(10);
    var n2 = new Number(20);

    println(n1.sum(n2));
    println(n1.isGreater(n2));
    println(n2.isGreater(n1));
  


  }
  

}

