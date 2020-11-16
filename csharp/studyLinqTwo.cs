using System;
using System.Reflection;
using System.Linq;
using System.Collections;
using System.Collections.Generic;
using System.Xml.Linq;
using System.Globalization;
using System.Text.RegularExpressions;

namespace  Lin
{
    class Customer
    {
        public string name = "";
        public string city = "";
    }
    // class Student
    // {
    //     public string First{get;set;}
    //     public string Last{get;set;}
    //     public int ID{get;set;}
    //     public string Street{get;set;}
    //     public string City{get;set;}
    //     public List<int> Scores;
    // }
    class Teacher
    {
        public string First{get;set;}
        public string Last{get;set;}
        public int ID{get;set;}
        public string City{get;set;}
    }
    class StudyLing
    {
        // static Customer[] arr = {
        //     new Customer{name = "chen", city = "hz"},
        //     new Customer{name = "chen1", city = "hz"},
        //     new Customer{name = "chen2", city = "hz2"},
        //     new Customer{name = "chen3", city = "hz3"},
        //     new Customer{name = "chen4", city = "hz2"},
        // };
        // static Customer[] arr2 = {
        //     new Customer{name = "wang", city = "s"},
        //     new Customer{name = "wang1", city = "s"},
        //     new Customer{name = "wang2", city = "hz2"},
        //     new Customer{name = "wang3", city = "hz3"},
        //     new Customer{name = "wang4", city = "hz2"},
        // };
        static void Main(string[] args)
        {
            // var queryCustomerByCity = 
            //     from cust in arr
            //     group cust by cust.city;

            // foreach (var customerGroup in queryCustomerByCity)
            // {
            //     Console.WriteLine(customerGroup.Key);
            //     foreach (Customer customer in customerGroup)
            //     {
            //         Console.WriteLine("     {0}", customer.name);
            //     }
            // }

            // var custQuery = 
            //     from cust in arr
            //     group cust by cust.city into custGroup
            //     where custGroup.Count() >= 2
            //     orderby custGroup.Key descending
            //     select custGroup;

            // foreach (var customerGroup in custQuery)
            // {
            //     Console.WriteLine(customerGroup.Key);
            //     foreach (Customer customer in customerGroup)
            //     {
            //         Console.WriteLine("     {0}", customer.name);
            //     }
            // }

            // var innerJoinQuery = 
            //     from cust in arr
            //     join dist in arr2 on cust.city equals dist.city
            //     select new {custName = cust.name, distName = dist.name, city = cust.city};

            // foreach(var item in innerJoinQuery)
            // {
            //     Console.WriteLine(item.custName + ", " + item.distName + ", " + item.city);
            // }

            // IEnumerable<Customer> custQuery = 
            //     from cust in arr
            //     where cust.city == "hz2"
            //     select cust;

            // foreach(var cust in custQuery)
            // {
            //     Console.WriteLine(cust.name);
            // }

            // List<Student> students = new List<Student>()
            // {
            //     new Student { First="Svetlana",
            //         Last="Omelchenko",
            //         ID=111,
            //         Street="123 Main Street",
            //         City="Seattle",
            //         Scores= new List<int> { 97, 92, 81, 60 } },
            //     new Student { First="Claire",
            //         Last="O’Donnell",
            //         ID=112,
            //         Street="124 Main Street",
            //         City="Redmond",
            //         Scores= new List<int> { 75, 84, 91, 39 } },
            //     new Student { First="Sven",
            //         Last="Mortensen",
            //         ID=113,
            //         Street="125 Main Street",
            //         City="Lake City",
            //         Scores= new List<int> { 88, 94, 65, 91 } },
            // };

            // Create the second data source.
            // List<Teacher> teachers = new List<Teacher>()
            // {
            //     new Teacher { First="Ann", Last="Beebe", ID=945, City="Seattle" },
            //     new Teacher { First="Alex", Last="Robinson", ID=956, City="Redmond" },
            //     new Teacher { First="Michiyo", Last="Sato", ID=972, City="Tacoma" }
            // };
            // var peopleInSeattle = (from student in students
            //         where student.City == "Seattle"
            //         select student.Last)
            //         .Concat(from teacher in teachers
            //             where teacher.City == "Seattle"
            //             select teacher.Last);

            // foreach (var item in peopleInSeattle)
            // {
            //     Console.WriteLine(item);
            // }

            // var studentsToXML = new XElement("Root",
            //     from student in students
            //     let scores = string.Join(",", student.Scores)
            //     select new XElement("student",
            //             new XElement("First", student.First),
            //             new XElement("Last", student.Last),
            //             new XElement("Scores", scores)
            //             )
            //         );
            // Console.WriteLine(studentsToXML);

            // double[] radii = {1,2,3};
            // IEnumerable<string> output = 
            //     radii.Select(r => string.Format("Area for a circle with a radius of '{0}' = {1:F2}", r, r * r * Math.PI));
            //     // radii.Select(r => $"Area for a circle with a radius of '{r}' = {r * r * Math.PI:F2}");

            // foreach (string s in output)
            // {
            //     Console.WriteLine(s);
            // }

            // string formatString = "{0, -10}({0, 8:X8})\n" +
            //         "{1, 10}({1, 8:X8})\n" +
            //         "{2,10}({2,8:X8})";
            // int value1 = 16932;
            // int value2 = 15421;
            // string result = String.Format(formatString, value1, value2, value1 & value2);
            // Console.WriteLine(result);

            // double p1 = 10000;
            // double p2 = -2420.5;
            // double p3 = 0.00;
            // Console.WriteLine(string.Format("{0:#,###0.00;#,###0.000;}", p1));
            // Console.WriteLine(String.Format("{0:#,###0.00;-#,###0.000;}", p2));
            // Console.WriteLine(String.Format("{0:#,###0.00;#,###0.000;#,###0.0000}", p3));

            // double p1 = 1000000;
            // Console.WriteLine(string.Format("{0:E3}", p1));

            // DateTime date1 = new DateTime(2008, 4, 10, 6, 30, 5);
            // Console.WriteLine(date1.ToString("F", CultureInfo.CreateSpecificCulture("zh-cn")));
            // DateTime date1 = new DateTime(2010, 8, 12, 16, 32, 18, 506);
            // Console.WriteLine(date1.ToString("M/dd/yyyy H:mm:ss.FF"));

            // int[] numbers = {5,10,8,3,6,12};
            // IEnumerable<int> numQuery1 = 
            //     from num in numbers
            //     where num % 2 == 0
            //     orderby num
            //     select num;

            // IEnumerable<int> numQuery2 = numbers.Where(num => num % 2 == 0).OrderBy(n => n);
            // foreach (int i in numQuery1)
            // {
            //     Console.Write(i + " ");
            // }
            // Console.WriteLine(System.Environment.NewLine);
            // foreach (int i in numQuery2)
            // {
            //     Console.Write(i + " ");
            // }

            // string text = @"Historically, the world of Data and the world of objects" +  
            // @" have not been well integrated. Programmers work in C# or Visual Basic" +  
            // @" and also in SQL or XQuery. On the one side are concepts such as classes," +  
            // @" objects, fields, inheritance, and .NET APIs. On the other side" +  
            // @" are tables, columns, rows, nodes, and separate languages for dealing with" +  
            // @" them. Data types often require translation between the two worlds; there are" +  
            // @" different standard functions. Because the object world has no notion of query, a" +  
            // @" query can only be represented as a string without compile-time type checking or" +  
            // @" IntelliSense support in the IDE. Transferring data from SQL tables or XML trees to" +  
            // @" objects in memory is often tedious and error-prone."; 

            // string searchTerm = "on";
            // string[] source = text.Split(new char[]{'.', '?', '!', ' ', ';', ':', ','}, StringSplitOptions.RemoveEmptyEntries);
            // var matchQuery = from word in source
            //     where word.ToLowerInvariant() == searchTerm.ToLowerInvariant()
            //     select word;
            // int wordCount = matchQuery.Count();
            // Console.WriteLine("{0} {1}", wordCount, searchTerm);

            // string pattern = @"\b\w+es\b";
            // Regex rgx = new Regex(pattern);
            // foreach (Match match in rgx.Matches(text))
            // {
            //     Console.WriteLine("Found '{0}' at position {1}",
            //             match.Value, match.Index);
            // }

            // string pattern = "es";
            // Console.WriteLine(text.IndexOf(pattern));

            // string[] sentences = text.Split(new char[]{'.', '?', '!'});
            // string[] wordsToMatch = {"Historically", "Data", "integrated"};
            // var sentenceQuery = from sentence in sentences
            //                     let w = sentence.Split(new char[]{'.', '?', '!', ' ', ';', ':', ','},
            //                                             StringSplitOptions.RemoveEmptyEntries)
            //                     where w.Distinct().Intersect(wordsToMatch).Count() == wordsToMatch.Count()
            //                     select sentence;
            // foreach (string str in sentenceQuery)
            // {
            //     Console.WriteLine(str);
            // }          

            // string aString = "ABCDE99F-J74-12-89A";
            // IEnumerable<char> stringQuery = 
            //     from ch in aString
            //     where Char.IsDigit(ch)
            //     select ch;
            // foreach (char c in stringQuery)
            // {
            //     Console.Write(c + " ");
            // }
            // int count = stringQuery.Count();
            // Console.WriteLine("count = {0}", count);
            // IEnumerable<char> stringQuery2 = aString.TakeWhile(c => c != '-');
            // foreach (char c in stringQuery2)
            // {
            //     Console.Write(c);
            // }

            // Assembly info = typeof(int).Assembly;
            // Console.WriteLine(info);

            // Assembly a = Assembly.LoadFrom("studyIter.exe");
            // Type[] types2 = a.GetTypes();
            // foreach (Type item in types2)
            // {
            //     Console.WriteLine(item.FullName);
            // }

            // Type t = typeof(System.String);
            // ConstructorInfo[] ci = t.GetConstructors(BindingFlags.Public | BindingFlags.Instance);
            // PrintMembers(ci);

            // Type d1 = typeof(Dictionary<,>);
            // Console.WriteLine(d1);
            Type[] typeArgs = {typeof(string), typeof(int)};
            Console.WriteLine(typeArgs[0]);
        }

        public static void PrintMembers(MemberInfo[] ms)
        {
            foreach (MemberInfo m in ms)
            {
                Console.WriteLine(m);
            }
        }
    }
}