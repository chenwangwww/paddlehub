using System;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;

[Serializable]
struct Clo
{
    public int i;
    public int[] iArr;
    public Clo Clone1()
    {
        return (Clo)MemberwiseClone();
    }
    public Clo Clone2()
    {
        MemoryStream stream = new MemoryStream();
        BinaryFormatter formatter = new BinaryFormatter();
        formatter.Serialize(stream, this);
        stream.Position = 0;
        return (Clo)formatter.Deserialize(stream);
    }
}
class Program
{
    static void Main()
    {
        // Clo a = new Clo();
        // a.i = 10;
        // a.iArr = new int[]{7,9,0};
        // Clo b = a.Clone1();
        // Clo c = a.Clone2();
        // a.iArr[0] = 99;
        // a.i = 20;
        // Console.WriteLine(b.i);
        // foreach (var item in b.iArr)
        // {
        //     Console.Write(item + ", ");
        // }
        // Console.WriteLine("\n"+c.i);
        // foreach (var item in c.iArr)
        // {
        //     Console.Write(item + ", ");
        // }

        // decimal a = 100.0M; 
    }
}
public class MyClass
{
    public static void PrintSth()
    {
        Console.WriteLine("Hello");
    }
}