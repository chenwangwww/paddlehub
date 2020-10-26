using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.Serialization;
using System.Runtime.Serialization.Formatters.Binary;
using System.Text;
using System.Threading.Tasks;

namespace seial
{
    [Serializable]
    public class Person
    {
        public string Sno { get; set; }
        public string Name { get; set; }
        public string Sex { get; set; }
        public int Age { get; set; }
        public string Other { get; set; }
        [NonSerialized]
        public string NoSerial;

        public string DisplayInfo()
        {
            return "我的学号是：" + Sno + "\n我的名字是：" + Name + "\n我的性别为：" + Sex + "\n我的年龄：" + Age + "\n非序列化:" + NoSerial + "\n";
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            var me = new Person
            {
                Sno = "1235",
                Name = "wuzhuang",
                Sex = "man",
                Age = 22,
                NoSerial = "bb",
                Other = "\n"
            };
            var he = new Person
            {
                Sno = "12655",
                Name = "wanggang",
                Sex = "man",
                Age = 25,
                NoSerial = "bb2",
                Other = "\n"
            };
            List<Person> personInfo = new List<Person>();
            personInfo.Add(me);
            personInfo.Add(he);
            IFormatter formatter = new BinaryFormatter();

            Stream stream = new FileStream("./csharp/te.txt", FileMode.OpenOrCreate, FileAccess.Write,FileShare.None);
            foreach (Person per in personInfo)
            {
                formatter.Serialize(stream, per);
            }
            stream.Close();

            Stream destream = new FileStream("./csharp/te.txt", FileMode.Open, FileAccess.Read, FileShare.Read);
            var stillme = (Person)formatter.Deserialize(destream);
            var stillhe = (Person)formatter.Deserialize(destream);
            Console.WriteLine(stillme.DisplayInfo());
            Console.WriteLine(stillhe.DisplayInfo());
            destream.Close();
        }
    }
}