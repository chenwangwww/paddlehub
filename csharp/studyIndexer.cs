using System;
using System.Collections;

namespace Demo
{
    public class EntrantInfo
    {
        public string Name{get;set;}
        public int Num{get;set;}
        public string Department{get;set;}
    }
    public class IndexerForEntrantInfo
    {
        private ArrayList ArrLst;
        public IndexerForEntrantInfo()
        {
            ArrLst = new ArrayList();
        }
        public string this[string name, int num]
        {
            get
            {
                foreach (EntrantInfo en in ArrLst)
                {
                    if(en.Name == name && en.Num == num)
                    {
                        return en.Department;
                    }
                }
                return null;
            }
            set
            {
                ArrLst.Add(new EntrantInfo()
                {
                    Name = name,
                    Num = num,
                    Department = value
                });
            }
        }
        public ArrayList this[int num]
        {
            get
            {
                ArrayList temp = new ArrayList();
                foreach (EntrantInfo en in ArrLst)
                {
                    if(en.Num == num)
                    {
                        temp.Add(en);
                    }
                }
                return temp;
            }
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            IndexerForEntrantInfo info = new IndexerForEntrantInfo();
            info["zhangsan", 101] = "renshibu";
            info["lisi", 102] = "xingzhengbu";
            Console.WriteLine(info["zhangsan", 101]);
            Console.WriteLine(info["lisi", 102]);
            Console.WriteLine();
            foreach (EntrantInfo en in info[102])
            {
                Console.WriteLine(en.Name);
                Console.WriteLine(en.Department);
            }
        }
    }
}