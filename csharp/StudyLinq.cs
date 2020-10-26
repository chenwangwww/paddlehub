using System;
using System.Linq;
using System.Collections;
using System.Collections.Generic;
public class program
{
    public static void Main(string[] args)
    {
        // string[] fruits = { "apple", "banana", "mango", "passionfruit", "grape" };
        // var query = fruits.Select((fruit, index) =>
        //         new { index, str = fruit.Substring(0, index) });
        // foreach (var item in query)
        // {
        //     Console.WriteLine("{0}", item);
        // }
        // Console.WriteLine("------------------------------------");
        // foreach (var item in fruits)
        // {
        //     Console.WriteLine("{0}", item);
        // }

        // string[] words = {"Tuesday", "Mardi"};
        // string[] lowerWords = new string[words.Length];
        // for (int i = words.GetLowerBound(0); i <= words.GetUpperBound(0); i++)
        // {
        //     lowerWords[i] = words[i].ToLowerInvariant();
        // }
        // foreach (var word in words)
        // {
        //     Console.WriteLine(word);
        // }
        // Console.WriteLine("----------------");
        // foreach (var word in lowerWords)
        // {
        //     Console.WriteLine(word);
        // }

        // string sentence = "the quick brown fox jumps over the lazy dog";
        // string[] words = sentence.Split(' ');
        // string reversed = words.Aggregate((workingSentence, next)=> next + " " + workingSentence);
        // Console.WriteLine(reversed);

        // Pet[] pets = { new Pet { Name="Barley", Age=10 },
        //            new Pet { Name="Boots", Age=4 },
        //            new Pet { Name="Whiskers", Age=6 } };

        // bool allStartWithB = pets.All(pet => pet.Name.StartsWith("B"));
        // Console.WriteLine("{0} pet names start with 'B'.", allStartWithB ? "All" : "Not all");

        // int[] arr = {1,2,4,6};
        // bool b = arr.All((item)=>item<63);
        // Console.WriteLine("{0}", b);

        // List<int> numbers = new List<int>{1,2};
        // bool b = numbers.Any();
        // Console.WriteLine("the list {0} empty.", 
        //     b ? "is not" : "is");

        // Pet[] pets =
        // { new Pet { Name="Barley", Age=8, Vaccinated=true },
        //   new Pet { Name="Boots", Age=4, Vaccinated=false },
        //   new Pet { Name="Whiskers", Age=1, Vaccinated=false } };

        // bool unvaccinated = pets.Any(p=>p.Age > 1 && p.Vaccinated == false);
        // Console.WriteLine(unvaccinated);

        // List<int> numbers = new List<int>{1,2,3,4};
        // numbers = numbers.Append(5).ToList();
        // Console.WriteLine(string.Join(", ", numbers));

        // Clump<string> fruits = new Clump<string>{ "apple", "passionfruit", "banana",
        //     "mango", "orange", "blueberry", "grape", "strawberry" };
        // IEnumerable<string> query = fruits.Where(fruit=>fruit.Contains("o"));
        // foreach (var item in query)
        // {
        //     Console.WriteLine(item);
        // }

        // List<int> grades = new List<int>{78, 92, 100, 37, 81};
        // double average = grades.Average();
        // Console.WriteLine(average);

        // System.Collections.ArrayList fruits = new System.Collections.ArrayList();
        // fruits.Add("mango");
        // fruits.Add("apple");
        // fruits.Add("lemon");
        // IEnumerable<string> query = fruits.Cast<string>().OrderBy(fruit=>fruit).Select(fruit=>fruit);
        // foreach (string fruit in query)
        // {
        //     Console.WriteLine(fruit);
        // }

        // int[] arr = new int[5]{1,2,3,4,5};
        // bool b = arr.Contains(1);
        // Console.WriteLine(b);
        // Console.WriteLine(arr is IEnumerable<int>);
        // Console.WriteLine(arr.GetType());

        // Pet[] pets = { new Pet { Name="Barley", Vaccinated=true },
        //            new Pet { Name="Boots", Vaccinated=false },
        //            new Pet { Name="Whiskers", Vaccinated=false } };
        // int num = pets.Count((p)=>p.Vaccinated == false);
        // Console.WriteLine(num);

        // int[] arr = new int[5]{1,1,2,3,4};
        // IEnumerable<int> dis = arr.Distinct();
        // foreach (var i in dis)
        // {
        //     Console.WriteLine(i);
        // }

        // int a = arr.ElementAtOrDefault(100);
        // Console.WriteLine(a);

        // double[] numbers1 = {2.0, 2.0, 2.1, 2.2, 2.3, 2.3, 2.4, 2.5};
        // double[] numbers2 = {2.2, 2.3};
        // IEnumerable<double> oo = numbers1.Except(numbers2);
        // foreach (var item in oo)
        // {
        //     Console.WriteLine(item);
        // }

        // List<Pet> pets = new List<Pet>{
        //     new Pet { Name="Barley", Age=8.3 },
        //     new Pet { Name="Boots", Age=4.9 },
        //     new Pet { Name="Whiskers", Age=1.5 },
        //     new Pet { Name="Daisy", Age=4.3 }
        // };
        // var query = pets.GroupBy(
        //     pet => Math.Floor(pet.Age),
        //     pet => pet.Age,
        //     (baseAge, ages) => new{
        //         Key = baseAge,
        //         Count = ages.Count(),
        //         Min = ages.Min(),
        //         Max = ages.Max()
        //     }
        // );
        // foreach (var result in query)
        // {
        //     Console.WriteLine(result.Key);
        //     Console.WriteLine(result.Count);
        //     Console.WriteLine(result.Min);
        //     Console.WriteLine(result.Max);
        // }

        // Person magnus = new Person { Name = "Hedlund, Magnus" };
        // Person terry = new Person { Name = "Adams, Terry" };
        // Person charlotte = new Person { Name = "Weiss, Charlotte" };

        // Pet barley = new Pet { Name = "Barley", Owner = terry };
        // Pet boots = new Pet { Name = "Boots", Owner = terry };
        // Pet whiskers = new Pet { Name = "Whiskers", Owner = charlotte };
        // Pet daisy = new Pet { Name = "Daisy", Owner = magnus };
        // List<Person> people = new List<Person> { magnus, terry, charlotte };
        // List<Pet> pets = new List<Pet> { barley, boots, whiskers, daisy };
        // var query = people.Join(pets,
        // Person=>Person,
        // pet=>pet.Owner,
        // (Person, pet)=>
        // new{OwnerName = Person.Name, Pet = pet.Name});
        // foreach (var obj in query)
        // {
        //     Console.WriteLine("{0} - {1}", obj.OwnerName, obj.Pet);
        // }

        // ArrayList fruits = new ArrayList(4);
        // fruits.Add("Mango");
        // fruits.Add("Orange");
        // fruits.Add("apple");
        // fruits.Add(3.6);
        // fruits.Add("banana");
        // IEnumerable<string> query = fruits.OfType<string>();
        // foreach (string fruit in query)
        // {
        //     Console.WriteLine(fruit);
        // }

        // IEnumerable<string> strings = Enumerable.Repeat("100", 3);
        // foreach (var str in strings)
        // {
        //     Console.WriteLine(str);
        // }

        // PetOwner[] petOwners = 
        // {
        //     new PetOwner { Name="Higa, Sidney",
        //         Pets = new List<string>{ "Scruffy", "Sam" } },
        //     new PetOwner { Name="Ashkenazi, Ronen",
        //         Pets = new List<string>{ "Walker", "Sugar" } },
        //     new PetOwner { Name="Price, Vernette",
        //         Pets = new List<string>{ "Scratches", "Sugar", "Diesel" } }
        // };
        // IEnumerable<string> query = petOwners.SelectMany(petOwner=>petOwner.Pets);
        // foreach (var pet in query)
        // {
        //     Console.WriteLine(pet);
        // }

        Pet pet1 = new Pet { Name = "Turbo", Age = 2 };
        Pet pet2 = new Pet { Name = "Peanut", Age = 8 };
        List<Pet> pets1 = new List<Pet> { pet1, pet2 };
        List<Pet> pets2 = new List<Pet> { pet1, pet2 };
        bool equal = pets1.SequenceEqual(pets2);
        Console.WriteLine(equal);
    }

    class Pet
    {
        public string Name { get; set; }
        public int Age { get; set; }
    }

    // class Pet
    // {
    //     public string Name{get;set;}
    //     public double Age{get;set;}
    //     public bool Vaccinated{get;set;}
    // }

    // class Clump<T>: List<T>
    // {

    // }

    // class Person
    // {
    //     public string Name { get; set; }
    // }
    // class Pet
    // {
    //     public string Name { get; set; }
    //     public Person Owner { get; set; }
    // }
    // class PetOwner
    // {
    //     public string Name { get; set; }
    //     public List<string> Pets { get; set; }
    // }
}
