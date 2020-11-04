using System;
using System.Reflection;
using System.Linq;
using System.Linq.Expressions;

class SampleClass
{
    static void Main(string[] args){
        // Console.WriteLine(args.Length);
        // Type type = typeof(int);
        // Console.WriteLine("Methods:");
        // MethodInfo[] methodInfos = type.GetMethods();
        // foreach (MethodInfo item in methodInfos)
        // {
        //     Console.WriteLine(item.ToString());
        // }
        // Console.WriteLine("Members:");
        // MemberInfo[] memberInfos = type.GetMembers();
        // foreach (var item in memberInfos)
        // {
        //     Console.WriteLine(item.ToString());
        // }

        // Expression<Func<int, int, int, int>> expr = (x,y,z)=>(x+y)/z;
        // Console.WriteLine(expr.Compile()(1,2,3));

        // ParameterExpression _parameExp = Expression.Parameter(typeof(string), "MyPara");
        // MethodCallExpression _methodCallexp = Expression.Call(typeof(Console).GetMethod("WriteLine", new Type[]{typeof(string)}), _parameExp);
        // Expression<Action<string>> _consStringExp = Expression.Lambda<Action<string>>(_methodCallexp, _parameExp);
        // _consStringExp.Compile()("hello!!!");

        ParameterExpression _paraA = Expression.Parameter(typeof(int), "a");
        ParameterExpression _paraB = Expression.Parameter(typeof(int), "b");
        BinaryExpression _binadd = Expression.Add(_paraA, _paraB);
        Expression<Func<int, int, int>> _mybin = Expression.Lambda<Func<int, int, int>>(_binadd,
            new ParameterExpression[] { _paraA, _paraB });
        Console.WriteLine("expression:" + _mybin);
        Console.WriteLine(_mybin.Compile()(4,6));
    }
}