using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    public static void Main(string[] args)
    {
        // List<string> mList = new List<string>();
        // mList.Add("John");
        // string[] tempArr = {"Ha", "Lily"};
        // mList.AddRange(tempArr);
        // var mNewList = mList.Select((value, index)=>
        // new {index, value = value + " new"}).ToList();
        // foreach (var item in mNewList)
        // {
        //     Console.WriteLine("{0}", item);
        // }

        // mList.Insert(1, "Chen");
        // foreach (var item in mList)
        // {
        //     Console.WriteLine(item);
        // }

        // Console.WriteLine("www");
        // Console.WriteLine("\nch");
        // Object s = new object();
        
        List<Part> parts = new List<Part>();
        parts.Add(new Part() {PartName="crank arm", PartId=1234});
        parts.Add(new Part() { PartName = "chain ring", PartId = 1334 });
        parts.Add(new Part() { PartName = "regular seat", PartId = 1434 });

        parts.ForEach(Print);
    }

    static void Print(Part p)
    {
        Console.WriteLine("partname:{0}, partid:{1}", p.PartName, p.PartId);
    }
}

public class Part
{
    public string PartName { get; set; }

    public int PartId { get; set; }
}