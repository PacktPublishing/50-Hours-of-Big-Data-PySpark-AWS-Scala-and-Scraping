import scala.io.StdIn.readLine
class Student(var name: String, var roll: String)
{

}

object Main {

  def main(args: Array[String]): Unit = 
  {
     var s1 = new Student("Hello","123");
     var s2 = new Student("World","456");

     println(s1.name);
     println(s2.name);
  }
  

}

