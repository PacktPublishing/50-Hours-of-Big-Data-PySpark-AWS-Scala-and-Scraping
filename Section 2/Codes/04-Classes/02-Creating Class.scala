import scala.io.StdIn.readLine

class Student{
  var name = "";
  var roll = "";
}


object Main {

  def main(args: Array[String]): Unit = 
  {
      var s1 = new Student();
      var s2 = new Student();

      s1.name = "Hello";
      s1.roll = "123";

      s2.name = "World";
      s2.roll = "456";


      println(s1.name);
      println(s2.name);
  }
  

}

