using System;
using System.Linq;
using System.Drawing;
using System.Collections;
using System.Collections.Generic;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

// public class Temperature: IComparable<Temperature>
// {
//     public int CompareTo(Temperature other)
//     {
//         if(other == null)return 1;
//         return m_value.CompareTo(other.m_value);
//     }

//     public static bool operator >(Temperature operand1, Temperature operand2)
//     {
//         return operand1.CompareTo(operand2) == 1;
//     }

//     public static bool operator <(Temperature operand1, Temperature operand2)
//     {
//         return operand1.CompareTo(operand2) == -1;
//     }
//     public static bool operator >=(Temperature operand1, Temperature operand2)
//     {
//         return operand1.CompareTo(operand2) >= 0;
//     }

//     public static bool operator <=(Temperature operand1, Temperature operand2)
//     {
//         return operand1.CompareTo(operand2) <= 0;
//     }

//     protected double m_value = 0.0;
//     public double Celsius
//     {
//         get{
//             return m_value - 273.15;
//         }
//     }
//     public double Kelvin
//     {
//         get{
//             return m_value;
//         }
//         set{
//             if(value<0.0){
//                 throw new ArgumentException("Temperature cannot be less than absolute zero.");
//             }else{
//                 m_value = value;
//             }
//         }
//     }

//     public Temperature(double kelvins)
//     {
//         this.Kelvin = kelvins;
//     }
// }
public class SamplesArray
{
    public static void Main()
    {
        // int[] myIntArray = new int[5]{1,2,3,4,5};
        // Object[] myObjArray = new Object[5]{26,27,28,29,30};
        // Console.WriteLine("-----------------");
        // PrintValues(myIntArray);
        // Console.WriteLine("-----------------");
        // PrintValues(myObjArray);

        // int[,] a = new int[3,4]{
        //     {0, 1, 2, 3} ,   /*  初始化索引号为 0 的行 */
        //     {4, 5, 6, 7} ,   /*  初始化索引号为 1 的行 */
        //     {8, 9, 10, 11}   /*  初始化索引号为 2 的行 */
        // };
        // Console.WriteLine(a.Length);
        // Console.WriteLine(a.Rank);

        // Array myIntArray = Array.CreateInstance(typeof(System.Int32), 5);
        // for (int i = myIntArray.GetLowerBound(0); i<=myIntArray.GetUpperBound(0); i++)
        // {
        //     myIntArray.SetValue(i+1,i);
        // }
        // PrintValues((int[])myIntArray);

        // Array myObjArray = Array.CreateInstance(typeof(System.Object),5);
        // for(int i = myObjArray.GetLowerBound(0); i<=myObjArray.GetUpperBound(0);i++)
        // {
        //     myObjArray.SetValue(i+26,i);
        // }
        // PrintValues((Object[])myObjArray);
        // // Array.Copy(myIntArray, 0, myObjArray, 0, 1);
        // // PrintValues((Object[])myObjArray);
        // Array.Copy(myIntArray, myObjArray, 3);
        // PrintValues((Object[])myObjArray);

        // int[] arr = new int[5]{1,2,3,4,5};
        // int[] tar = new int[8];
        // arr.CopyTo(tar, 2);
        // tar.SetValue(19, 0);
        // PrintValues((int[])tar);

        // Array arr = Array.CreateInstance(typeof(System.Int32), 3,2);
        // PrintValues((int[,])arr);

        // Array arr = Array.CreateInstance(typeof(System.Int32), new int[]{1,2}, new int[]{1,0});
        // arr.SetValue(12,1,0);
        // Array.Reverse(arr);
        // PrintValues((int[,])arr);

        // PointF[] apf = {
        //     new PointF(27.8f, 32.43f),
        //     new PointF(99.2f, 146.8f)
        // };

        // foreach (PointF p in apf)
        // {
        //     Console.WriteLine(p);
        // }

        // Point[] ap = Array.ConvertAll(apf, 
        //     new Converter<PointF, Point>(PointFToPoint));

        // Console.WriteLine("------------------");
        // foreach (Point p in ap)
        // {
        //     Console.WriteLine(p);
        // }

        // SortedList<Temperature, string> temps = new SortedList<Temperature, string>();
        // temps.Add(new Temperature(2017.15), "Boiling point of Lead");
        // temps.Add(new Temperature(0), "Absolute zero");
        // temps.Add(new Temperature(273.15), "Freezing point of water");
        // temps.Add(new Temperature(5100.15), "Boiling point of Carbon");
        // temps.Add(new Temperature(373.15), "Boiling point of water");
        // temps.Add(new Temperature(600.65), "Melting point of Lead");

        // foreach (KeyValuePair<Temperature, string> kvp in temps)
        // {
        //     Console.WriteLine("{0} is {1} degrees Celsius.", kvp.Value, kvp.Key.Celsius);
        // }

        // string[] dinosaurs = {"Pachycephalosaurus",
        //                       "Amargasaurus",
        //                       "Tyrannosaurus",
        //                       "Mamenchisaurus",
        //                       "Deinonychus",
        //                       "Edmontosaurus"};

        // Array.Sort(dinosaurs);
        // foreach (string dino in dinosaurs)
        // {
        //     Console.WriteLine(dino);
        // }

        // int index = Array.BinarySearch(dinosaurs, "dhs");
        // Console.WriteLine(index + ", " + (~index));

        // int[] arr1 = new int[]{1,2,3,4};
        // int[] arr2 = new int[10];

        // Array.ConstrainedCopy(arr1, 1, arr2, 5, 2);
        // Array.Copy(arr1, arr2, 3);
        
        // PrintValues(arr2);

        // int result = Array.Find<int>(arr1, (int p)=>{return p == 3;});
        // Console.WriteLine(result);

        // string[] myArr = new string[10];
        // myArr[0] = "The";
        // myArr[1] = "quick";
        // myArr[2] = "brown";
        // myArr[3] = "fox";
        // myArr[4] = "jumps";
        // myArr[5] = "over";
        // myArr[6] = "the";
        // myArr[7] = "lazy";
        // myArr[8] = "dog";

        // int i = 0;
        // System.Collections.IEnumerator myE = myArr.GetEnumerator();
        // while ((myE.MoveNext()) && (myE.Current != null)){
        //     Console.WriteLine("[{0}] {1}", i++, myE.Current);
        // }

        // int[,] arr =  new int[2,3]{
        //     {1,2,3},{4,5,6}
        // };
        // int len = arr.GetLength(1);
        // Console.WriteLine(len);

        // Point pt = new Point(5,8);
        // Console.WriteLine(pt.GetHashCode());
        // String[] myArr = {"The", "quick", "brown", "fox", "jumps",
        //     "over", "the", "lazy", "dog"};

        // PrintIndexAndValues(myArr);

        // Array.Resize(ref myArr, myArr.Length + 5);
        // Console.WriteLine("--------------");
        // PrintIndexAndValues(myArr);
        // Array.Resize(ref myArr, 4);
        // Console.WriteLine("--------------");
        // PrintIndexAndValues(myArr);
        // Array.Reverse(myArr);
        // Console.WriteLine("--------------");
        // PrintIndexAndValues(myArr);

        // String[] words = { "The", "QUICK", "BROWN", "FOX", "jumps",
        //                  "over", "the", "lazy", "dog" };

        // IComparer revComparer = new ReverseComparer();
        // Array.Sort(words, 1,3,revComparer);
        // PrintIndexAndValues(words);

        // string sentence = "the quick brown fox jumps over the lazy dog";
        // string[] words = sentence.Split(' ');
        // string reversed = words.Aggregate((workingSentence, next)=> next + " " + workingSentence);
        // Console.WriteLine(reversed);
        
        // string[] words = {"alphabet", "Error", "zebra", "Abc", "αυτοκινητοβιομηχανία", "государство",
        //            "1234", ".", ";", " "};
        // Array.ForEach(words, (val)=>{Console.WriteLine(val.StartWithUpper());});

        // Console.WriteLine(typeof(List<>));
        // Console.WriteLine(typeof(Dictionary<,>));

        // int a = 1, b = 2;
        // // string c = $"{a} + {b} = {a+b}";
        // string d = string.Format("{0} + {1} = {2}", a, b, a+b);
        // string path = @"c:\abc\";
        // string path2 = "c:\\abc\\";
        // Console.WriteLine(d);
        // Console.WriteLine(path);
        // Console.WriteLine(path2);

        // var ep = new Employeestruct(12);
        // var ep = new Employeestruct();

        // GenericCacheTest.Show();
        // var b = new B();
        // b.func();

        List<int> intL = new List<int>();
        intL.Add(1);
        intL.Add(12);
        intL.Add(1);
        int index = intL.FindIndex(1,2,x=>x == 1);
        Console.WriteLine(index);
    }

    // public static void PrintIndexAndValues(String[] myArr)  {
    //     for(int i = 0; i < myArr.Length; i++)
    //     {
    //         Console.WriteLine("   [{0}] : {1}", i, myArr[i]);
    //     }
    //     Console.WriteLine();
    // }

    // public static Point PointFToPoint(PointF pf)
    // {
    //     return new Point(((int)pf.X), (int)pf.Y);
    // }

    // public static void PrintValues<T>(T[] arr)
    // {
    //     foreach (T item in arr)
    //     {
    //         Console.Write("\t{0}", item);
    //     }
    //     Console.WriteLine();
    // }
    // public static void PrintValues<T>(T[,] arr)
    // {
    //     foreach (T item in arr)
    //     {
    //         Console.Write("\t{0}", item);
    //     }
    //     Console.WriteLine();
    // }

    // #region testRegion
    // int testregion(){
    //     return 1;
    // }
    // #endregion
}

// public struct Point
// {
//     private int x;
//     private int y;
//     public Point(int x, int y){
//         this.x = x;
//         this.y = y;
//     }
//     public override bool Equals(Object obj)
//     {
//         if(!(obj is Point)) return false;
//         Point p = (Point)obj;
//         return x == p.x & y == p.y;
//     }

//     public override int GetHashCode()
//     {
//         return x ^ y;
//     }
// }

// public class ReverseComparer: IComparer
// {
//     public int Compare(Object x, Object y)
//     {
//         return (StringComparer.CurrentCulture).Compare(y,x);
//     }
// }

// public static class StringLibrary
// {
//     public static bool StartWithUpper(this string str)
//     {
//         if (String.IsNullOrEmpty(str))
//         {
//             return false;
//         }
//         char ch = str[0];
//         return Char.IsUpper(ch);
//     }
// }

// public class Employeestruct
// {
//     private int _fooNumber;

//     Employeestruct(){
//         Console.WriteLine("hello");
//     }
//     public Employeestruct(int fooNumber):this()
//     {
//         _fooNumber = fooNumber;
//         Console.WriteLine("{0} done", _fooNumber);
//     }
// }

// public class Employeestruct
// {
//     private int _fooNumber;
//     readonly int _d = 12;

//     public Employeestruct(){
//         Console.WriteLine("hello");
//         _d = 23;
//         Console.WriteLine(_d);
//         Console.WriteLine(this._d);
//     }
//     public Employeestruct(int fooNumber)
//     {
//         _fooNumber = fooNumber;
//         Console.WriteLine("{0} done", _fooNumber);
//     }
// }

// public class GenericCache<T>
// {
//     static GenericCache()
//     {
//         Console.WriteLine("This is GenericCache 静态构造函数");
//         _TypeTime = string.Format("{0}_{1}", typeof(T).FullName, DateTime.Now.ToString("yyyyMMddHHmmss.fff"));
//     }

//     private static string _TypeTime = "";

//     public static string GetCache()
//     {
//         return _TypeTime;
//     }
// }

// public class GenericCacheTest
// {
//     public static void Show()
//     {
//         for (int i = 0; i < 5; i++)
//         {
//             Console.WriteLine(GenericCache<int>.GetCache());
//             Thread.Sleep(10);
//             Console.WriteLine(GenericCache<long>.GetCache());
//             Thread.Sleep(10);
//             Console.WriteLine(GenericCache<DateTime>.GetCache());
//             Thread.Sleep(10);
//             Console.WriteLine(GenericCache<string>.GetCache());
//             Thread.Sleep(10);
//             Console.WriteLine(GenericCache<GenericCacheTest>.GetCache());
//             Thread.Sleep(10);
//         }
//     }
// }

class A
{
    public virtual void func()
    {
        Console.WriteLine('A');
    }

    public void t(int a)
    {

    }

    public int t()
    {
        return 1;
    }
}

class B: A
{
    public override void func()
    {
        Console.WriteLine("B");
        base.func();
    }
}