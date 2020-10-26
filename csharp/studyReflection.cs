using System;
using System.Reflection;

namespace TestSpace
{
    public class TestClass
    {
        private string _value;
        public TestClass(){}
        public TestClass(string value)
        {
            _value = value;
        }
        public string GetValue(string prefix)
        {
            string str = _value == null ? "NULL" : prefix + ": "+_value;
            Console.WriteLine(str);
            return str;
        }
        public string Value{
            set{
                _value = value;
            }
            get{
                return _value == null ? "NULL":_value;
            }
        }

        public static void Main(string[] args)
        {
            Type t = Type.GetType("TestSpace.TestClass");
            object[] constuctParms = new object[]{"timmy"};
            object dObj = Activator.CreateInstance(t,constuctParms);
            MethodInfo method = t.GetMethod("GetValue");
            BindingFlags flag = BindingFlags.Public | BindingFlags.Instance;
            object[] parameters = new object[]{"Hello"};
            object returnValue = method.Invoke(dObj, flag, Type.DefaultBinder, parameters, null);
        }
    }
}