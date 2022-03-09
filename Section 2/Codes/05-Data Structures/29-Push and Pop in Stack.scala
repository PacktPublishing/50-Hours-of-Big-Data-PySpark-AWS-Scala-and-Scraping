import scala.io.StdIn.readLine
import scala.collection.mutable.Stack

object Main {

  def main(args: Array[String]): Unit = 
  {
    var stack = Stack[Int]();

    stack.push(1);
    println(stack);
    stack.push(2);
    println(stack);
    stack.push(3);
    println(stack);
    stack.push(1);
    println(stack);


    println(stack.pop());
    println(stack);
    println(stack.pop());
    println(stack);

   
  }
  

}

