using System;
using System.Collections;
using System.Collections.Generic;

class Iter
{
    static void Main()
    {
        // foreach (int number in EvenSequence(5, 18))
        // {
        //     Console.Write(number.ToString() + " ");
        // }

        // DaysOfTheWeek days = new DaysOfTheWeek();
        // foreach (var day in days)
        // {
        //     Console.Write(day + " ");
        // }

        // foreach (Person item in new People())
        // {
        //     Console.Write(item.name + " " + item.age + " ");
        // }

        Stack<int> theStack = new Stack<int>();
        for (int i = 0; i < 9; i++)
        {
            theStack.Push(i * i);
        }
        foreach (var item in theStack)
        {
            Console.Write("{0} ", item);
        }
        Console.WriteLine();
        foreach (var item in theStack.TopToBottom)
        {
            Console.Write("{0} ", item);
        }
        Console.WriteLine();
        foreach (var item in theStack.BottomToTop)
        {
            Console.Write("{0} ", item);
        }
    }
    public static IEnumerable<int> EvenSequence(int firstNumber, int lastNumber)
    {
        for (int i = firstNumber; i <= lastNumber; i++)
        {
            if (i % 2 == 0)
            {
                yield return i;
            }
        }
    }

    public class DaysOfTheWeek: IEnumerable
    {
        private string[] days = {"sun", "mon", "tue", "wed", "thu", "fri", "sat"};
        public IEnumerator GetEnumerator()
        {
            for (int i = 0; i < days.Length; i++)
            {
                yield return days[i];
            }
        }
    }
}
public class People: IEnumerable
{
    public Person[] pp = {new Person(){name = "chen", age = 10}, new Person(){
        name = "wang", age = 22
    }};
    public IEnumerator GetEnumerator()
    {
        return new PeopleEnum(this.pp);
    }
}
public class PeopleEnum: IEnumerator
{
    public Person[] _people;
    int position = -1;
    public PeopleEnum(Person[] list)
    {
        _people = list;
    }
    bool IEnumerator.MoveNext()
    {
        Console.WriteLine("IEnumerator.MoveNext");
        return MoveNext();
    }
    public bool MoveNext()
    {
        Console.WriteLine("MoveNext");
        position++;
        return (position < _people.Length);
    }
    public void Reset()
    {
        position = -1;
    }
    object IEnumerator.Current
    {
        get {
            Console.WriteLine("object");
            return Current;
        }
    }
    public Person Current
    {
        get{
            try{
                Console.WriteLine("person");
                return _people[position];
            }catch(IndexOutOfRangeException)
            {
                throw new InvalidOperationException();
            }
        }
    }
}

public class Person
{
    public string name;
    public int age;
}

public class Stack<T>: IEnumerable<T>
{
    private T[] values = new T[100];
    private int top = 0;
    public void Push(T t)
    {
        values[top] = t;
        top++;
    }
    public T Pop()
    {
        top--;
        return values[top];
    }
    public IEnumerator<T> GetEnumerator()
    {
        for (int i = top - 1; i >= 0; i--)
        {
            yield return values[i];
        }
    }
    IEnumerator IEnumerable.GetEnumerator()
    {
        return GetEnumerator();
    }
    public IEnumerable<T> TopToBottom
    {
        get{return this;}
    }
    public IEnumerable<T> BottomToTop
    {
        get {
            for (int i = 0; i <= top - 1; i++)
            {
                yield return values[i];
            }
        }
    }
}