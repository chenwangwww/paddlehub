using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

class Program
{
    public static void Main()
    {
        Dog aDog = new Dog();
        Animal aAnimal = aDog;
        List<Dog> lstD = new List<Dog>();
        List<Animal> lstA = lstD.Select(d=>(Animal)d).ToList();
        IEnumerable<Dog> someDogs = new List<Dog>();
        IEnumerable<Animal> someAnimals = someDogs;

        IMyList<Dog> myDogs = new MyList<Dog>();
        IMyList<Animal> myAnimals = myDogs;

        Type t = myAnimals.GetType();
        Console.WriteLine(t.GetInterface("IMyList"));
        if(t.get("MyList") != null){
            Console.WriteLine("www");
        }
    }

    public abstract class Animal
    {
        
    }
    public class Dog : Animal
    {

    }

    public interface IMyList<out T>
    {
        T GetElement();
    }

    public class MyList<T>: IMyList<T>
    {
        public T GetElement()
        {
            return default(T);
        }
    }
}