using System;
using System.Collections;
using System.Collections.Generic;

class Person
{
    // public string Name{get; set;}
    // public int Age{get; set;}
    // public override string ToString()
    // {
    //     return "Person: " + Name + " " + Age;
    // }

    static void Main(string[] args)
    {
        // Person person = new Person{Name = "John", Age = 12};
        // Console.WriteLine(person);

        // char[] apple = {'a', 'p', 'p', 'l', 'e'};
        // char[] reversed = apple.Reverse().ToArray();

        MyCollection<Student> sc = new MyCollection<Student>();
        sc.Add(new Student{id=0,name="Tont"});
        sc.Add(new Student{id=1,name="ynt"});
        foreach (var item in sc)
        {
            Console.WriteLine(item);
        }
    }
}

class Student
{
    public int id;
    public string name;
    public override string ToString()
    {
        return string.Format("name: {0}, id: {1};", this.name, this.id);
    }
}

class MyCollection<T>: IEnumerable<T>
{
    public List<T> myco = new List<T>();
    public void Add(T value)
    {
        myco.Add(value);
    }
    public IEnumerator<T> GetEnumerator()
    {
        Console.WriteLine("IEnumerator<T>");
        foreach (var item in myco)
        {
            yield return item;
        }
    }

    IEnumerator IEnumerable.GetEnumerator()
    {
        Console.WriteLine("IEnumerator");
        foreach (var item in myco)
        {
            yield return item;
        }
    }
}