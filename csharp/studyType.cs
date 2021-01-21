using System;

public class Program
{
    public static void Main()
    {
        // byte[] bytes = {0,0,0,25};
        // if(BitConverter.IsLittleEndian){
        //     Array.Reverse(bytes);
        //     Console.WriteLine(BitConverter.ToString(bytes));
        // }

        // int i = BitConverter.ToInt32(bytes, 0);
        // Console.WriteLine("int: {0}", i);

        string input = String.Empty;
        try
        {
            int result = Int32.Parse(input);
            Console.WriteLine(result);
        }
        catch (FormatException)
        {
            
            Console.WriteLine(String.Format("Unable to parse {0}", input));
        }

        try
        {
            int numVal = Int32.Parse("-105");
            Console.WriteLine(numVal);
        }
        catch (FormatException e)
        {
            
            Console.WriteLine(e.Message);
        }
        int j = 10;
        if(Int32.TryParse("-105", out j))
        {
            Console.WriteLine(j);
        }
        else
        {
            Console.WriteLine("string could not be parsed.");
        }

        try
        {
            int m = Int32.Parse("abc");
        }
        catch (Exception e)
        {
            Console.WriteLine(e.Message);
        }
    }
}