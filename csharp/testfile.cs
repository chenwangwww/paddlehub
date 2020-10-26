using System;
using System.IO;
using System.Diagnostics;
using System.ComponentModel;

namespace FileIOApplication
{
    class Program
    {
        // static void Main(string[] args)
        // {
        //     FileStream F = new FileStream("test.dat", 
        //         FileMode.OpenOrCreate, FileAccess.ReadWrite);
        //     for(int i = 1; i<=20;i++)
        //     {
        //         F.WriteByte((byte)i);
        //     }
        //     F.Position = 0;
        //     for(int i = 0; i<=20;i++)
        //     {
        //         Console.Write(F.ReadByte() + " ");
        //     }
        //     F.Close();
        //     Console.ReadKey();
        // }

        static void Main()
        {
            using (Process mypro = new Process())
            {
                mypro.StartInfo.UseShellExecute = true;
                mypro.StartInfo.FileName = ".\\studyTask.exe";
                mypro.StartInfo.CreateNoWindow = true;
                mypro.Start();
                Console.WriteLine("hello");
            }
        }
    }
}