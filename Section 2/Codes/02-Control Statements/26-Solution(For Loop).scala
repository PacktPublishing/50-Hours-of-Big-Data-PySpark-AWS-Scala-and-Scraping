import scala.io.StdIn.readLine

object Main {
  def main(args: Array[String]): Unit = {

    var x = readLine("Enter number of courses: ");
    var totalCourses = x.toInt;
    var totalMarks = 0;


    for(w <- 1 to totalCourses)
    {
      var y = readLine("Enter course marks: ");
      var marks = y.toInt;
      totalMarks = totalMarks + marks;
      println(totalMarks);

    }

    var averageMarks = totalMarks / totalCourses;

    println(averageMarks);

    if(averageMarks > 90)
    {
      println("A grade");
    }
    else if(averageMarks > 70)
    {
      println("B grade");
    }    
   }
}
