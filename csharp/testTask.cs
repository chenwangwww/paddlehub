using System;
using System.Threading.Tasks;
using System.Collections.Generic;
class Program
{
    // static void Main(string[] args)
    // {
    //     Method1();
    //     Method2();
    //     Console.ReadKey();
    // }

    // public static async Task Method1()
    // {
    //     await Task.Run(()=>{
    //         for (int i = 0; i < 100; i++)
    //         {
    //             Console.WriteLine("Method1:" + i);
    //         }
    //     });
    // }

    // public static void Method2()
    // {
    //     for (int i = 0; i < 25; i++)
    //     {
    //         Console.WriteLine("Method2");
    //     }
    // }

    // static void Main(string[] args)
    // {
    //     callMethod();
    //     Console.ReadKey();
    // }

    // public static async void callMethod()
    // {
    //     Task<int> task = Method1();
    //     Method2();
    //     int count = await task;
    //     Method3(count);
    // }
    // public static async Task<int> Method1()
    // {
    //     int count = 0;
    //     await Task.Run(()=>{
    //         for (int i = 0; i < 50; i++)
    //         {
    //             Console.WriteLine("Method1");
    //             count+=1;
    //         }
    //     });
    //     return count;
    // }
    // public static void Method2()
    // {
    //     for (int i = 0; i < 25; i++)
    //     {
    //         Console.WriteLine("Method2");
    //     }
    // }
    // public static void Method3(int count)
    // {
    //     Console.WriteLine("total:" + count);
    // }

    static void Main(string[] args)
    {
        var test = Power(2,8);
        Console.WriteLine("first");
        foreach (var item in Power(3,4))
        {
            Console.Write("{0}, ", item);
        }
        Console.ReadKey();
    }

    public static IEnumerable<int> Power(int n, int c)
    {
        int result = 1;
        Console.WriteLine("call");
        for (int i = 0; i < c; i++)
        {
            result = result*n;
            yield return result;
        }
        yield return 3;
    }
}