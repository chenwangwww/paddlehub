using System;
using System.Text.RegularExpressions;

public class Example
{
   public static void Main()
   {
      string input = "Aone two";
      string pattern = @"\bA(?#匹配以A开头的单词)\w+\b";
      string patternRep = @"${word2} ${word1}";

      foreach (Match match in Regex.Matches(input, pattern))
         Console.WriteLine(match.Value);

      // Console.WriteLine(Regex.Replace(input, pattern, patternRep));
      Console.ReadKey();
   }
}