using System;
using System.Reflection;

[AttributeUsage(AttributeTargets.All)]
public class DeveloperName: Attribute
{
    private string name;
    private string level;
    private bool reviewed;

    public DeveloperName(string name, string level)
    {
        this.name = name;
        this.level = level;
        this.reviewed = false;
        Console.WriteLine("developer");
    }

    public virtual string Name
    {
        get{return name;}
    }

    public virtual string Level
    {
        get{return level;}
    }

    public virtual bool Reviewed
    {
        get {return reviewed;}
        set {reviewed = value;}
    }
}

class TestClass
{
    public float val = 10.0f;
    public bool win;
}

[DeveloperName("Joan Smith", "1")]
class Example
{
    static void Main()
    {
        Console.WriteLine("main");
        GetAttribute(typeof(Example));

        TestClass tt = new TestClass();
        Console.WriteLine(tt.win);
    }

    public static void GetAttribute(Type t)
    {
        DeveloperName myAttribute = 
            (DeveloperName) Attribute.GetCustomAttribute(t, typeof(DeveloperName));

        if(myAttribute == null)
        {
            Console.WriteLine("the attribute was not found.");
        }
        else
        {
            Console.WriteLine("name:{0}", myAttribute.Name);
            Console.WriteLine("level:{0}", myAttribute.Level);
            Console.WriteLine("reviewed:{0}", myAttribute.Reviewed);
        }
    }
}

// namespace TestSpace
// {
    // public class TestClass
    // {
    //     private string _value;
    //     public TestClass(){}
    //     public TestClass(string value)
    //     {
    //         _value = value;
    //     }
    //     public string GetValue(string prefix)
    //     {
    //         string str = _value == null ? "NULL" : prefix + ": "+_value;
    //         Console.WriteLine(str);
    //         return str;
    //     }
    //     public string Value{
    //         set{
    //             _value = value;
    //         }
    //         get{
    //             return _value == null ? "NULL":_value;
    //         }
    //     }

    //     public static void Main(string[] args)
    //     {
    //         Type t = Type.GetType("TestSpace.TestClass");
    //         object[] constuctParms = new object[]{"timmy"};
    //         object dObj = Activator.CreateInstance(t,constuctParms);
    //         MethodInfo method = t.GetMethod("GetValue");
    //         BindingFlags flag = BindingFlags.Public | BindingFlags.Instance;
    //         object[] parameters = new object[]{"Hello"};
    //         object returnValue = method.Invoke(dObj, flag, Type.DefaultBinder, parameters, null);
    //     }
    // }
// }