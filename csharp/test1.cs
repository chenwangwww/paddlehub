using System;
using System.Collections.Generic;
using System.Linq;
using System.Xml.Linq;

// class tt
// {
//     public static void Main(string[] args)
//     {
        // var a = 1;
        // Console.WriteLine(a);
        // Console.ReadKey();

        // var student = new{Name = "Mary Jones", Age = 19, Major = "jis"};
        // Console.WriteLine("{0}, Age {1}, Major:{2}", student.Name,student.Age,student.Major);
        // Console.ReadKey();

        // int[] numbers = {2,5,28};
        // IEnumerable<int> lowNums = from n in numbers
        //                             where n<20
        //                             select n;
        // int numsCount = (from n in numbers
        //                     where n<20
        //                     select n).Count();

        // numbers[2] = -1;
        // foreach (var item in lowNums)
        // {
        //     Console.Write("{0}, ", item);
        // }

        // Console.WriteLine();
        // Console.WriteLine(numsCount);
        // Console.ReadKey();
//     }
// }

class Program
{
    public class Student
    {
        public int StID;
        public string LastName;
    }
    public class CourseStudent
    {
        public string CourseName;
        public int StID;
    }
    static Student[] students=new Student[]{
        new Student{StID=1,LastName="Carson"},
        new Student{StID=2,LastName="Klassen"},
        new Student{StID=3,LastName="Fleming"},
    };
    static CourseStudent[] studentsInCourses=new CourseStudent[]{
        new CourseStudent{CourseName="Art",StID=1},
        new CourseStudent{CourseName="Art",StID=2},
        new CourseStudent{CourseName="History",StID=1},
        new CourseStudent{CourseName="History",StID=3},
        new CourseStudent{CourseName="Physics",StID=3},
    };
    static void Main()
    {
        // var query=from s in students
        //           join c in studentsInCourses on s.StID equals c.StID
        //           where c.CourseName=="History"
        //           select s.LastName;
        // foreach(var q in query)
        // {
        //     Console.WriteLine("Student taking History:{0}",q);
        // }
        // Console.ReadKey();

        // var groupA = new[]{3,4,5,6};
        // var groupB = new[]{6,7,8,9};
        // var someInts = from a in groupA
        //                 from b in groupB
        //                 where a>4 && b<=8
        //                 select new{a,b,sum=a+b};
        // foreach (var item in someInts)
        // {
        //     Console.WriteLine(item);
        // }
        // Console.ReadKey();

        // var students=new[]
        // {
        //     new{LName="Jones",FName="Mary",Age=19,Major="History"},
        //     new{LName="Smith",FName="Bob",Age=20,Major="CompSci"},
        //     new{LName="Fleming",FName="Carol",Age=21,Major="History"},
        // };
        // var query=from s in students
        //           group s by s.Major;
        // foreach(var s in query)
        // {
        //     Console.WriteLine("{0}",s.Key);
        //     foreach(var t in s)
        //     {
        //         Console.WriteLine("      {0},{1},{2},{3}",t.LName,t.FName,t.Age,t.Major);
        //     }
        // }
        // Console.ReadKey();

        // int[] intArray = new int[]{3,4,5,6,7,9};
        // // var cou = intArray.Count(n=>n%2!=0);
        // Func<int,bool> myDel = delegate(int x)
        // {
        //     return x%2!=0;
        // };
        // var cou = intArray.Count(myDel);
        // Console.WriteLine("{0}", cou);
        // Console.ReadKey();

        // XDocument employees1 = new XDocument(
        //     new XElement("Employees",
        //     new XElement("Name", "Bob"),
        //     new XElement("Name", "Sally"))
        // );
        // employees1.Save("s.xml");
        // XDocument employees2 = XDocument.Load("s.xml");
        // Console.WriteLine(employees2);
        // Console.ReadKey();

        // XDocument xd=new XDocument(
        //     new XElement("MyElements",
        //         new XElement("first",
        //             new XAttribute("color","red"),
        //             new XAttribute("size","small")),
        //         new XElement("second",
        //             new XAttribute("color","red"),
        //             new XAttribute("size","midium")),
        //         new XElement("third",
        //             new XAttribute("color","blue"),
        //             new XAttribute("size","large"))
        //     )
        // );
        // Console.WriteLine(xd);
        // xd.Save("SimpleSample.xml");

        XDocument xd = XDocument.Load("SimpleSample.xml");
        XElement rt = xd.Element("MyElements");
        var xyz = from e in rt.Elements()
                where e.Name.ToString().Length == 5
                select e;
        foreach (XElement x in xyz)
        {
            Console.WriteLine(x.Name.ToString());
        }
        Console.WriteLine();
        foreach (XElement x in xyz)
        {
            Console.WriteLine("Name: {0}, color: {1}, size: {2}",
            x.Name,
            x.Attribute("color").Value,
            x.Attribute("size").Value);
        }
        Console.ReadKey();
    }
}