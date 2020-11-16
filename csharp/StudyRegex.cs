using System;
using System.Globalization;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;

public class Example
{
    // delegate void MultiDelegate();
    //  static MultiDelegate myMultiDelegate;
    public static unsafe void Main()
    {
        // string pattern; 
        // pattern = "hello\tworld";
        // Console.WriteLine(pattern);
        // CultureInfo ci = CultureInfo.CreateSpecificCulture("");
        // ci.NumberFormat.NegativeSign = "\u203E";
        // double[] numbers = {-1.0, -16.3, -103};
        // foreach(var number in numbers)
        // {
        //     Console.WriteLine(number.ToString(ci));
        // }

        // string text = "1A 2B 3C 4D 5E 6F 7G 8H 9I 10J 11Q 12J 13K 14L 15M 16N ffee80a #800080";
        // string strPattern = @"\b((\d+)([a-z]))\s+";
        // Regex rex = new Regex(strPattern, RegexOptions.IgnoreCase);
        // MatchCollection matches = rex.Matches(text);

        // foreach (Match match in matches)
        // {
        //     GroupCollection groups = match.Groups;
        //     Console.WriteLine("{0}共有{1}个分组:{2}", match.Value, groups.Count, strPattern);
            
        //     for (int i = 0; i < groups.Count; i++)
        //     {
        //         Console.WriteLine("分组{0}为{1}, 位置为{2}, 长度为{3}", i,
        //             groups[i].Value, groups[i].Index, groups[i].Length);
        //     }
        // }

        // string text = "I've found this amazing URL at http://www.sohu.com, and then find ftp://ftp.sohu.comisbetter.";
        // string pattern = @"\b(?<protocol>\S+)://(?<address>\S+)\b";
        // MatchCollection matches = Regex.Matches(text, pattern);
        // foreach (Match match in matches)
        // {
        //     GroupCollection groups = match.Groups;
        //     Console.WriteLine(string.Format("URL: {0}; PROTOCOL: {1}; ADDRESS: {2}",
        //                         match.Value, groups["protocol"].Value, groups["address"].Value));
        // }

        // Console.WriteLine("{0:X0000} time out", 124);
        // Apple myApple = new Apple();
        // myApple.SayHello();
        // myApple.Chop();

        // Fruit myFruit = new Apple();
        // myFruit.SayHello();
        // myFruit.Chop();

        // Fruit myFruit = new Apple();
        // myFruit.SayHello();
        // myFruit.Chop();

        // Apple myApple = (Apple)myFruit;
        // myApple.SayHello();
        // myApple.Chop();

        // Console.WriteLine("111".DefaultStr());

        // List<BadGuy> badGuys = new List<BadGuy>();
        // badGuys.Add(new BadGuy("Harvey", 50));
        // badGuys.Add(new BadGuy("Magneto", 100));
        // badGuys.Add(new BadGuy("pip", 5));
        // badGuys.Sort();
        // foreach (BadGuy guy in badGuys)
        // {
        //     Console.WriteLine(guy.name + "  " + guy.power);
        // }

        // myMultiDelegate += PowerUp;
        // myMultiDelegate += TurnRed;
        // myMultiDelegate -= TurnRed;
        // myMultiDelegate();

        string a = "100", b = a;
        b = "101";
        Console.WriteLine(a);
        int c = 100;
        int* d = &c;
        *d = 101;
        Console.WriteLine(c);
        Console.WriteLine((int)d);
    }
    static void PowerUp()
    {
        Console.WriteLine("orb is powering up!");
    }
    static void TurnRed()
    {
        Console.WriteLine("turn red");
    }
}

public class Fruit
{
    public Fruit()
    {
        Console.WriteLine("1st Fruit Constructor Called");
    }
    public void Chop()
    {
        Console.WriteLine("The fruit has been chopped.");
    }
    public void SayHello()
    {
        Console.WriteLine("Hello, I am a fruit.");
    }
}

public class Apple: Fruit
{
    public Apple()
    {
        Console.WriteLine("1st Apple Constructor Called");
    }
    public new void Chop()
    {
        base.Chop();
        Console.WriteLine("The apple has been chopped.");
    }
    public new void SayHello()
    {
        base.SayHello();
        Console.WriteLine("Hello, I an an apple.");
    }
}

public static class ExtensionMethods
{
    public static string DefaultStr(this System.String str)
    {
        return "default string!";
    }
}
public class BadGuy: IComparable<BadGuy>
{
    public string name;
    public int power;
    public BadGuy(string newName, int newPower)
    {
        name = newName;
        power = newPower;
    }
    public int CompareTo(BadGuy other)
    {
        if(other == null)
        {
            return 1;
        }
        return -(power - other.power);
    }
}