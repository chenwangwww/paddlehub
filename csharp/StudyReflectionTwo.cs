using System;
using System.Linq;
using System.Reflection;
using System.Collections.Generic;
using System.Security.Permissions;

// public interface ITestArgument
// {
    
// }

// public class TestBase{}

// public class Test<T> where T: TestBase, ITestArgument, new(){}
// public class TestArgument: TestBase, ITestArgument
// {
//     public TestArgument(){}
// }

// public class Example
// {
//     private static void DisplayGenericType(Type t)
//     {
//         Console.WriteLine("\r\n{0}", t);
//         Console.WriteLine("     Is this a generic ttype? {0}", t.IsGenericType);
//         Console.WriteLine("     Is this a generic type definition? {0}", t.IsGenericTypeDefinition);
//         Type[] typeParameters = t.GetGenericArguments();
//         Console.WriteLine("     List {0} type arguments:", typeParameters.Length);
//         foreach (Type tParam in typeParameters)
//         {
//             if(tParam.IsGenericParameter)
//             {
//                 DisplayGenericParameter(tParam);
//             }
//             else
//             {
//                 Console.WriteLine("     Type argument: {0}", tParam);
//             }
//         }
//     }
//     private static void DisplayGenericParameter(Type tp)
//     {
//         Console.WriteLine("     Type parameter: {0} position {1}", tp.Name, tp.GenericParameterPosition);
//         Type classConstraint = null;
//         foreach (Type iConstraint in tp.GetGenericParameterConstraints())
//         {
//             if(iConstraint.IsInterface)
//             {
//                 Console.WriteLine("     Interface constraint: {0}", iConstraint);
//             }
//         }
//         if(classConstraint != null)
//         {
//             Console.WriteLine("     Base type constraint: {0}", tp.BaseType);
//         }
//         else
//         {
//             Console.WriteLine("     Base type constraint: None");
//         }
//         GenericParameterAttributes sConstraints = tp.GenericParameterAttributes & GenericParameterAttributes.SpecialConstraintMask;
//         if(sConstraints == GenericParameterAttributes.None)
//         {
//             Console.WriteLine("     No special constraints.");
//         }
//         else
//         {
//             if(GenericParameterAttributes.None != (sConstraints & GenericParameterAttributes.DefaultConstructorConstraint))
//             {
//                 Console.WriteLine("     Must have a parameterless constructor.");
//             }
//             if(GenericParameterAttributes.None != (sConstraints & GenericParameterAttributes.ReferenceTypeConstraint))
//             {
//                 Console.WriteLine("     Must be a reference type.");
//             }
//             if(GenericParameterAttributes.None != (sConstraints & GenericParameterAttributes.NotNullableValueTypeConstraint))
//             {
//                 Console.WriteLine("     Must be a nom-nullable value type.");
//             }
//         }
//     }
//     [PermissionSetAttribute(SecurityAction.Demand, Name="FullTrust")]
    // public static void Main()
    // {
        // Type d1 = typeof(Dictionary<,>);
        // Dictionary<string, Example> d2 = new Dictionary<string, Example>();
        // Type d3 = d2.GetType();
        // Type d4 = d3.GetGenericTypeDefinition();

        // DisplayGenericType(d1);
        // DisplayGenericType(d2.GetType());

        // Type[] typeArgs = {typeof(string), typeof(Example)};
        // Type constructed = d1.MakeGenericType(typeArgs);
        // DisplayGenericType(constructed);
        // object o = Activator.CreateInstance(constructed);
        // Console.WriteLine("\r\nCompare types obtained by different methods:");
        // Console.WriteLine("     Are the constructed types equal?{0}",
        //         (d2.GetType() == constructed));
        // Console.WriteLine("     Are the generic definitions equal?{0}",
        //         (d1 == constructed.GetGenericTypeDefinition()));

        // DisplayGenericType(typeof(Test<>));

        // Dog adog = new Dog();
        // adog.func1();
        // adog.func2();
        // Animal aanimal = adog;
        // aanimal.func1();
        // List<Dog> lstDogs = new List<Dog>();
        // List<Animal> lstAnimal2 = lstDogs.Select(d => (Animal)d).ToList();
        // IEnumerable<Dog> someDogs = new List<Dog>();
        // IEnumerable<Animal> someAnimals = someDogs;

        // IMyList<Animal> myAnimals = new MyList<Animal>();
        // IMyList<Dog> myDogs = myAnimals;
        // int x = 3, y = 40;
        // TestRef(ref x, ref y);
        // Console.WriteLine("x:{0}, y:{1}", x,y);

//         int[] a1 = {1,2,3}, a2 = {10,20,40};
//         TestRefTwo(a1, a2);
//         foreach (var item in a1)
//         {
//             Console.WriteLine(item);
//         }
//     }

//     static void TestRef(ref int x, ref int y)
//     {
//         int temp;
//         temp = y; y = x; x = temp;
//     }
//     static void TestRefTwo(int[] a1, int[] a2)
//     {
//         int[] temp;
//         // temp = a2; a2 = a1; a1 = temp;
//         a1[2] = a2[2];
//     }
// }

// public abstract class Animal
// {
//     public void func1(){
//         Console.WriteLine("func1");
//     }
// }
// public class Dog: Animal
// {
//     public void func2(){
//         Console.WriteLine("func2");
//     }
// }
// public interface IMyList<in T>
// {
//     void ChangeT(T t);
// }
// public class MyList<T>: IMyList<T>
// {
//     public void ChangeT(T t)
//     {

//     }
// }

class TestClass
{
    private string _value;
    public TestClass(string value)
    {
        this._value = value;
    }
    public string GetValue()
    {
        return this._value;
    }
}
class Program
{
    public static void Main(String[] args)
    {
        Type t = Type.GetType("TestClass");
        object[] constructParams = new object[]{"hello"};
        TestClass obj = (TestClass)Activator.CreateInstance(t, constructParams);
        Console.WriteLine(obj.GetValue());
    }
}