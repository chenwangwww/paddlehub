using System;
using System.Collections;
namespace CollectionApplication
{
    class Program
    {
        static void Main(string[] args)
        {
            ArrayList al = new ArrayList();
            al.Add(45);
            al.Add(78);
            al.Add(33);
            al.Add(56);
            al.Add(12);
            al.Add(23);
            al.Add(9);
            Console.WriteLine("capacity: {0}", al.Capacity);
            Console.WriteLine("Count: {0}", al.Count);

            foreach(int i in al)
            {
                Console.Write(i+" ");
            }
            Console.WriteLine();
            al.Sort();
            foreach (int i in al)
            {
                Console.Write(i+" ");
            }
            Console.ReadKey();
        }
    }
}