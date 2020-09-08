using System;
public class MyClass
{
    [Obsolete("Don't use oldMethod")]
    public static void oldMethod()
    {

    }
    public static void newMethod() { }


}

public class testclass
{
    public static void Main()
    {
        MyClass.newMethod();
        Console.ReadKey();
    }
}