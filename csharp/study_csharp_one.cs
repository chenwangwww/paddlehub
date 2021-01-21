using System;
using System.Collections;
using System.Collections.Generic;

public class Book
{
    public String title;
    public static List<Book> books = new List<Book>();
    public void addBook(Book book)
    {
        books.Add(book);
        StaticFunc();
    }
    public static void StaticFunc()
    {
        Console.WriteLine("StaticFunc");
    }
    public virtual void Update()
    {
        Console.WriteLine(" Base Update");
    }
}

public abstract class MiddleBook: Book
{
    public int bookId = 12;
}

public class SpecialBook: MiddleBook
{
    // public void Update()
    // {
    //     base.Update();
    //     Console.WriteLine("Update");
    // }
}

class Program
{
    // static HashSet<int> lowNumbers = new HashSet<int>();
    // static HashSet<int> highNumbers = new HashSet<int>();

    public class A {
        public virtual void M(){}
        public virtual void Mn(){}

    }
    public class B: A{
        public sealed override void M(){}
        public override void Mn(){}
    }
    
    public class C:B{
        // public override void M(){}
        public override void Mn(){}
    }

    public static void Main(string[] args)
    {
        // for (int i = 0; i < 6; i++)
        // {
        //     lowNumbers.Add(i);
        // }

        // for (int i = 3; i < 10; i++)
        // {
        //     highNumbers.Add(i);
        // }

        // DisplaySet(lowNumbers);
        // DisplaySet(highNumbers);
        // HashSet<int> allteams = new HashSet<int>(lowNumbers);
        // allteams.UnionWith(highNumbers);
        // DisplaySet(lowNumbers);
        // DisplaySet(allteams);

        // highNumbers.UnionWith(lowNumbers);
        // DisplaySet(highNumbers);
        // Console.WriteLine(highNumbers.Overlaps(lowNumbers));

        // Hashtable ht = new Hashtable();
        // ht.Add("001", "Zara Ali");
        // ht.Add("002", "Abida Rehman");

        // if(ht.Contains("003"))
        // {
        //     Console.WriteLine("already have!");
        // }else
        // {
        //     ht.Add("003", "Joe Holzner");
        // }

        // ICollection key = ht.Keys;
        // foreach (string k in key)
        // {
        //     Console.WriteLine(k + ":" + ht[k]);
        // }

        // foreach (DictionaryEntry item in ht)
        // {
        //     Console.WriteLine(item.Key + ":" + item.Value);
        // }

        // Console.WriteLine(default(int));
        // Console.WriteLine(7/4);
        // Console.WriteLine(2/4);
        
        // WriteXML();
        // ReadXML();

        // List<string> dinosaurs = new List<string>();
        // dinosaurs.Add("Pachycephalosaurus");
        // dinosaurs.Add("Amargasaurus");
        // dinosaurs.Add("");
        // dinosaurs.Add(null);
        // dinosaurs.Add("Mamenchisaurus");
        // dinosaurs.Add("Deinonychus");
        // Display(dinosaurs);

        // Console.WriteLine("----------------------");
        // dinosaurs.Sort(CompareDinosByLength);
        // Display(dinosaurs);

        // Console.WriteLine("陈望".Length);

        Book book1 = new Book();
        book1.addBook(book1);
        // Console.WriteLine(Book.books.Count);
        SpecialBook book2 = new SpecialBook();
        // Console.WriteLine(SpecialBook.books.Count);
        book2.Update();
        Console.WriteLine(book2.bookId);

    }

    static void DisplaySet(HashSet<int> set)
    {
        Console.Write("{");
        foreach (int i in set)
        {
            Console.Write(" {0}", i);
        }
        Console.WriteLine(" }");
    }

    public static void WriteXML()
    {
        Book overview = new Book();
        overview.title = "Serialization Overview";
        System.Xml.Serialization.XmlSerializer writer = new System.Xml.Serialization.XmlSerializer(typeof(Book));
        var path = "./SerializationOverview.xml";
        Console.WriteLine(path);
        System.IO.FileStream file = System.IO.File.Create(path);
        writer.Serialize(file, overview);
        file.Close();
    }

    public static void ReadXML()
    {
        // var b = new Book{title = "SerialView"};
        // var writer = new System.Xml.Serialization.XmlSerializer(typeof(Book));
        // var wfile = new System.IO.StreamWriter("./SerialView.xml");
        // writer.Serialize(wfile, b);
        // wfile.Close();

        System.Xml.Serialization.XmlSerializer reader = new System.Xml.Serialization.XmlSerializer(typeof(Book));
        System.IO.StreamReader file = new System.IO.StreamReader("./SerialView.xml");
        Book overview = (Book)reader.Deserialize(file);
        file.Close();
        Console.WriteLine(overview.title);
    }

    private static int CompareDinosByLength(string x, string y)
    {
        if(x == null)
        {
            if(y == null)
            {
                return 0;
            }
            else
            {
                return -1;
            }
        }
        else
        {
            if(y == null)
            {
                return 1;
            }
            else
            {
                int retval = x.Length.CompareTo(y.Length);
                if(retval != 0)
                {
                    return retval;
                }
                else
                {
                    return x.CompareTo(y);
                }
            }
        }
    }

    private static void Display(List<string> list)
    {
        foreach (string s in list)
        {
            if(s == null)
                Console.WriteLine("null");
            else
                Console.WriteLine("\"{0}\"", s);
        }
    }
}