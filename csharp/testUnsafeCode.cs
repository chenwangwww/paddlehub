using System;
namespace UnsafeCodeApplication
{
    class TestPointer
    {
        public unsafe static void Main()
        {
            int[] list = {10,100,200};
            fixed(int* ptr = list)
            for(int i=0;i<3;i++)
            {
                Console.WriteLine("Address of list[{0}] = {1}", i,(int)(ptr+i));
                Console.WriteLine("value of list[{0}] = {1}", i, *(ptr+i));
            }
            Console.ReadKey();
        }
    }
}