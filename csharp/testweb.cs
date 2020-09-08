using System;
using System.Collections;
using System.Net;
using System.Text;
using System.IO;

public class Test
{
    public static void Main(string[] args)
    {
        HttpWebRequest request = (HttpWebRequest)WebRequest.Create(args[0]);
        request.Method = "GET";
        HttpWebResponse response = (HttpWebResponse)request.GetResponse();
        Stream receiveStream = response.GetResponseStream();
        StreamReader readStream = new StreamReader(receiveStream, Encoding.UTF8);
        Console.WriteLine(readStream.ReadToEnd());
        response.Close();
        readStream.Close();
        Console.ReadKey();
    }
}