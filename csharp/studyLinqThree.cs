using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    public static List<Student> GetStudents()
    {
        List<Student> students = new List<Student>
        {
            new Student {First="Svetlana", Last="Omelchenko", ID=111, Scores= new List<int> {97, 72, 81, 60}},
            new Student {First="Claire", Last="O'Donnell", ID=112, Scores= new List<int> {75, 84, 91, 39}},
            new Student {First="Sven", Last="Mortensen", ID=113, Scores= new List<int> {99, 89, 91, 95}},
            new Student {First="Cesar", Last="Garcia", ID=114, Scores= new List<int> {72, 81, 65, 84}},
            new Student {First="Debra", Last="Garcia", ID=115, Scores= new List<int> {97, 89, 85, 82}}
        };
        return students;
    }
    public static void Main(string[] args)
    {
        // List<Student> students = new List<Student>
        // {
        //     new Student{LastName="xiaogui",Scores=new List<int>{97,42,91,60}},
        //     new Student { LastName="xiaozhan",Scores=new List<int>{50,92,81,60}},
        //     new Student { LastName="xiaolan",Scores=new List<int>{32,32,81,90}},
        //     new Student{ LastName="xiaowan",Scores=new List<int>{92,22,81,60}}
        // };
        // var query = from student in students
        //             from score in student.Scores
        //             where score >90
        //             select new
        //             {
        //                 last = student.LastName, score
        //             };
        // foreach (var student in query)
        // {
        //     Console.WriteLine("{0} score:{1}", student.last, student.score);
        // }

        // string[] strings = {"A penny saved is a penny earned.", "The aaxly sdj", "the pa is no"};
        // var query = from sentence in strings
        //             let words = sentence.Split(' ')
        //             from word in words
        //             let w = word.ToLower()
        //             where w[0] == 'a' || w[0] == 'e'
        //             select word;
        // foreach (var item in query)
        // {
        //     Console.WriteLine(item);
        // }       

            // string[] str = {"a", "b", "c"};
            // var query = from s in str               
            //             orderby s
            //             select s;
            // foreach (var item in query)
            // {
            //     Console.WriteLine(item);
            // }

        // string[] str = {"aa", "bb", "cc", "dd"};
        // var query = from s in str
        //             group s by s[0]
        //                 into p
        //                 where p.Key != 'd'
        //                 orderby p.Key
        //                 select p;

        // foreach (var item in query)
        // {
        //     Console.WriteLine(item.Key);
        // }

        List<Student> students = GetStudents();
        var studentQuery = from student in students
                            let avg = (int)student.Scores.Average()
                            group student by (avg/10) into g
                            orderby g.Key
                            select g;
        foreach (var studentGroup in studentQuery)
        {
            int temp = studentGroup.Key * 10;
            Console.WriteLine("{0}-{1}", temp, temp+10);
            foreach (var student in studentGroup)
            {
                Console.WriteLine("     {0},{1}:{2}", student.Last, student.First, student.Scores.Average());
            }
        }
    }
}

// struct Student
// {
//     public string LastName;
//     public List<int> Scores;
// }

public class Student
{
    public string First{get;set;}
    public string Last{get;set;}
    public int ID{get;set;}
    public List<int> Scores;
}