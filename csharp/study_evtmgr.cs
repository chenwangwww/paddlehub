using System;
using System.Collections.Generic;

public class GameEvent {}

public class GameEventOne: GameEvent{
    public int sp = 2;
}

public class GameEventTwo: GameEvent{
    public string str = "";
}

public static class EventManager
{
    static readonly Dictionary<Type, Action<GameEvent>> s_Events = new Dictionary<Type, Action<GameEvent>>();
    static readonly Dictionary<Delegate, Action<GameEvent>> s_EventLookups = new Dictionary<Delegate, Action<GameEvent>>();
    public static void AddListener<T>(Action<T> evt) where T: GameEvent
    {
        if(!s_EventLookups.ContainsKey(evt))
        {
            Action<GameEvent> newAction = (e) =>evt((T)e);
            s_EventLookups[evt] = newAction;

            Action<GameEvent> internalAction;
            if(s_Events.TryGetValue(typeof(T), out internalAction))
                s_Events[typeof(T)] = internalAction + newAction;
            else
                s_Events[typeof(T)] = newAction;
        }
    }

    public static void RemoveListener<T>(Action<T> evt) where T: GameEvent
    {
        Action<GameEvent> action = null;
        if(s_EventLookups.TryGetValue(evt, out action))
        {
            Action<GameEvent> tempAction = null;
            if(s_Events.TryGetValue(typeof(T), out tempAction))
            {
                tempAction -= action;
                if(tempAction == null)
                    s_Events.Remove(typeof(T));
                else
                    s_Events[typeof(T)] = tempAction;
            }
            s_EventLookups.Remove(evt);
        }
    }

    public static void Broadcast(GameEvent evt)
    {
        Action<GameEvent> action = null;
        if(s_Events.TryGetValue(evt.GetType(), out action))
            action.Invoke(evt);
    }

    public static void Clear()
    {
        s_Events.Clear();
        s_EventLookups.Clear();
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        // EventManager.AddListener<GameEventOne>(func1);
        // EventManager.AddListener<GameEventTwo>(func2);
        // EventManager.AddListener<GameEventTwo>(func3);
        // GameEventTwo two = new GameEventTwo();
        // two.str = "test val";
        // EventManager.Broadcast(two);

        // GameEventOne one = new GameEventOne();
        // one.sp = 2001;
        // EventManager.Broadcast(one);

        bool one = true;
        bool two = false;
        bool three = true;
        Console.WriteLine(one & three);
        Console.WriteLine(one | two);
    }

    public static void func1(GameEventOne evt)
    {
        Console.WriteLine("GameEventOne:{0}", evt.sp);
    }

    public static void func2(GameEventTwo evt)
    {
        Console.WriteLine("GameEventTwo:{0}", evt.str);
    }

    public static void func3(GameEventTwo evt)
    {
        Console.WriteLine("GameEventTwo again:{0}", evt.str);
    }
}