using System;
using System.Threading;
using System.Threading.Tasks;
using System.Collections.Concurrent;
using System.Collections;
using System.Net;
using System.Text;
using System.IO;

namespace ConsoleApp
{
    class Program
    {
        // static void Main(string[] args)
        // {
        //     var t1 = new Task(()=>TaskMethod("Task 1"));
        //     var t2 = new Task(()=>TaskMethod("Task 2"));
        //     t2.Start();
        //     t1.Start();
        //     Task.WaitAll(t1,t2);
        // }

        // static void TaskMethod(string name)
        // {
        //     Console.WriteLine("Task {0} is running on a thread id {1}. is thread pool thread: {2}",
        //         name, Thread.CurrentThread.ManagedThreadId, Thread.CurrentThread.IsThreadPoolThread);
        // }

        // async static void AsyncFunction()
        // {
        //     await Task.Delay(1);
        //     Console.WriteLine("使用System.Threading.Tasks.Task执行异步操作.");
        //     for (int i = 0; i < 10; i++)
        //     {
        //         Console.WriteLine(string.Format("AsyncFunction:i={0}", i));
        //     }
        // }

        // public static void Main()
        // {
        //     Console.WriteLine("主线程执行业务处理.");
        //     AsyncFunction();
        //     Console.WriteLine("主线程执行其他处理");
        //     for (int i = 0; i < 10; i++)
        //     {
        //         Console.WriteLine(string.Format("Main:i={0}", i));
        //     }
        //     Console.ReadLine();
        // }

        // static Task<int> CreateTask(string name)
        // {
        //     return new Task<int>(() => TaskMethod(name));
        // }

        // static void Main(string[] args)
        // {
        //     TaskMethod("Main Thread Task");
        //     Task<int> task = CreateTask("Task 1");
        //     task.Start();
        //     int result = task.Result;
        //     Console.WriteLine("Task 1 ");
        //     Console.WriteLine("Task 1 Result is: {0}", result);

        //     task = CreateTask("Task 2");
        //     //该任务会运行在主线程中
        //     task.RunSynchronously();
        //     result = task.Result;
        //     Console.WriteLine("Task 2 Result is: {0}", result);

        //     task = CreateTask("Task 3");
        //     Console.WriteLine(task.Status);
        //     task.Start();

        //     while (!task.IsCompleted)
        //     {
        //         Console.WriteLine(task.Status);
        //         Thread.Sleep(TimeSpan.FromSeconds(0.5));
        //     }

        //     Console.WriteLine(task.Status);
        //     result = task.Result;
        //     Console.WriteLine("Task 3 Result is: {0}", result);

        //     #region 常规使用方式
        //     //创建任务
        //     Task<int> getsumtask = new Task<int>(() => Getsum());
        //     //启动任务,并安排到当前任务队列线程中执行任务(System.Threading.Tasks.TaskScheduler)
        //     getsumtask.Start();
        //     Console.WriteLine("主线程执行其他处理");
        //     //等待任务的完成执行过程。
        //     getsumtask.Wait();
        //     //获得任务的执行结果
        //     Console.WriteLine("任务执行结果：{0}", getsumtask.Result.ToString());
        //     Console.ReadKey();
        //     #endregion
        // }

        // static int TaskMethod(string name)
        // {
        //     Console.WriteLine("Task {0} is running on a thread id {1}. Is thread pool thread: {2}",
        //         name, Thread.CurrentThread.ManagedThreadId, Thread.CurrentThread.IsThreadPoolThread);
        //     Thread.Sleep(TimeSpan.FromSeconds(2));
        //     return 42;
        // }

        // static int Getsum()
        // {
        //     int sum = 0;
        //     Console.WriteLine("使用Task执行异步操作.");
        //     for (int i = 0; i < 100; i++)
        //     {
        //         sum += i;
        //     }
        //     return sum;
        // }

        // public static void Main()
        // {
        //     var ret1 = AsyncGetsum();
        //     int result = ret1.Result;                  //阻塞主线程
        //     Console.WriteLine("主线程执行其他处理");
        //     for (int i = 1; i <= 3; i++)
        //         Console.WriteLine("Call Main()");

        //     Console.WriteLine("任务执行结果：{0}", result);
        //     Console.ReadKey();
        // }

        // async static Task<int> AsyncGetsum()
        // {
        //     await Task.Delay(3000);
        //     int sum = 0;
        //     Console.WriteLine("使用Task执行异步操作.");
        //     for (int i = 0; i < 100; i++)
        //     {
        //         sum += i;
        //     }
        //     return sum;
        // }

        // public static void Main()
        // {
        //     Task t = Task.Run( () => {
        //                             Random rnd = new Random();
        //                             long sum = 0;
        //                             int n = 1000000000;
        //                             for (int ctr = 1; ctr <= n; ctr++) {
        //                             int number = rnd.Next(0, 101);
        //                             sum += number;
        //                             }
        //                             Console.WriteLine("Total:   {0:N0}", sum);
        //                             Console.WriteLine("Mean:    {0:N2}", sum/n);
        //                             Console.WriteLine("N:       {0:N0}", n);   
        //                         } );
        //     Console.WriteLine("ttt");
        //     t.Wait();
        //     Console.WriteLine("qqq");
        //     Console.ReadKey();
        // }

        // static void Main(string[] args)
        // {
        //     ConcurrentStack<int> stack = new ConcurrentStack<int>();

        //     //t1先串行
        //     var t1 = Task.Factory.StartNew(() =>
        //     {
        //         stack.Push(1);
        //         stack.Push(2);
        //         stack.Push(3);
        //     });

        //     //t2,t3并行执行
        //     var t2 = t1.ContinueWith(t =>
        //     {
        //         int result;
        //         stack.TryPop(out result);
        //         Console.WriteLine("Task t2 result={0},Thread id {1}", result, Thread.CurrentThread.ManagedThreadId);
        //     });

        //     //t2,t3并行执行
        //     var t3 = t2.ContinueWith(t =>
        //     {
        //         int result;
        //         stack.TryPop(out result);
        //         Console.WriteLine("Task t3 result={0},Thread id {1}", result, Thread.CurrentThread.ManagedThreadId);
        //     });

        //     //t2,t3并行执行
        //     var t5 = t3.ContinueWith(t =>
        //     {
        //         int result;
        //         stack.TryPop(out result);
        //         Console.WriteLine("Task t5 result={0},Thread id {1}", result, Thread.CurrentThread.ManagedThreadId);
        //     });

        //     //等待t2和t3执行完
        //     Task.WaitAll(t2, t3, t5);

        //     //t7串行执行
        //     var t4 = Task.Factory.StartNew(() =>
        //     {
        //         Console.WriteLine("当前集合元素个数：{0},Thread id {1}", stack.Count, Thread.CurrentThread.ManagedThreadId);
        //     });
        //     t4.Wait();
        //     Console.ReadKey();
        // }

        // public static void Main()
        // {
        //     Task<string[]> parent = new Task<string[]>(state =>
        //     {
        //         Console.WriteLine(state);
        //         string[] result = new string[2];
        //         //创建并启动子任务
        //         new Task(() => { result[0] = "我是子任务1。"; }, TaskCreationOptions.AttachedToParent).Start();
        //         new Task(() => { result[1] = "我是子任务2。"; }, TaskCreationOptions.AttachedToParent).Start();
        //         return result;
        //     }, "我是父任务，并在我的处理过程中创建多个子任务，所有子任务完成以后我才会结束执行。");
        //     //任务处理完成后执行的操作
        //     parent.ContinueWith(t =>
        //     {
        //         Array.ForEach(t.Result, r => Console.WriteLine(r));
        //     });
        //     //启动父任务
        //     parent.Start();
        //     //等待任务结束 Wait只能等待父线程结束,没办法等到父线程的ContinueWith结束
        //     //parent.Wait();
        //     Console.ReadLine();

        // }

        // public static void Main()
        // {
        //     // create a three element array of integers
        //     int[] intArray = new int[] {2, 3, 4};

        //     // set a delegate for the ShowSquares method
        //     Action<int> action = new Action<int>(ShowSquares);

        //     Array.ForEach(intArray, action);
        // }

        // private static void ShowSquares(int val)
        // {
        //     Console.WriteLine("{0:d} squared = {1:d}", val, val*val);
        // }

        // private static int TaskMethod(string name, int seconds, CancellationToken token)
        // {
        //     Console.WriteLine("Task {0} is running on a thread id {1}. Is thread pool thread: {2}",
        //         name, Thread.CurrentThread.ManagedThreadId, Thread.CurrentThread.IsThreadPoolThread);
        //     for (int i = 0; i < seconds; i++)
        //     {
        //         Thread.Sleep(TimeSpan.FromSeconds(1));
        //         if (token.IsCancellationRequested) return -1;
        //     }
        //     return 42 * seconds;
        // }

        // private static void Main(string[] args)
        // {
        //     var cts = new CancellationTokenSource();
        //     var longTask = new Task<int>(() => TaskMethod("Task 1", 10, cts.Token), cts.Token);
        //     Console.WriteLine(longTask.Status);
        //     cts.Cancel();
        //     Console.WriteLine(longTask.Status);
        //     Console.WriteLine("First task has been cancelled before execution");
        //     cts = new CancellationTokenSource();
        //     longTask = new Task<int>(() => TaskMethod("Task 2", 10, cts.Token), cts.Token);
        //     longTask.Start();
        //     for (int i = 0; i < 5; i++)
        //     {
        //         Thread.Sleep(TimeSpan.FromSeconds(0.5));
        //         Console.WriteLine(longTask.Status);
        //     }
        //     cts.Cancel();
        //     for (int i = 0; i < 5; i++)
        //     {
        //         Thread.Sleep(TimeSpan.FromSeconds(0.5));
        //         Console.WriteLine(longTask.Status);
        //     }

        //     Console.WriteLine("A task has been completed with result {0}.", longTask.Result);
        // }

        // static int TaskMethod(string name, int seconds)
        // {
        //     Console.WriteLine("Task {0} is running on a thread id {1}. Is thread pool thread: {2}",
        //         name, Thread.CurrentThread.ManagedThreadId, Thread.CurrentThread.IsThreadPoolThread);
        //     Thread.Sleep(TimeSpan.FromSeconds(seconds));
        //     // throw new Exception("Boom!");
        //     return 42 * seconds;
        // }

        // static void Main(string[] args)
        // {
        //     try
        //     {
        //         Task<int> task = Task.Run(() => TaskMethod("Task 2", 2));
        //         int result = task.GetAwaiter().GetResult();
        //         Console.WriteLine("Result: {0}", result);
        //     }
        //     catch (Exception ex)
        //     {
        //         Console.WriteLine("Task 2 Exception caught: {0}", ex.Message);
        //     }
        //     Console.WriteLine("----------------------------------------------");
        //     Console.WriteLine();
        // }

        // public static void Main(string[] args)
        // {
        //     var task1 = new Task(() => 
        //     {
        //         Console.WriteLine("begin");
        //         System.Threading.Thread.Sleep(2000);
        //         Console.WriteLine("finish");
        //     });
        //     Console.WriteLine("before start:" + task1.Status);
        //     task1.Start();
        //     Console.WriteLine("after start:" + task1.Status);
        //     task1.Wait();
        //     Console.WriteLine("after finish:" + task1.Status);
        //     Console.Read();
        // }

        // public static void Main(string[] args)
        // {
        //     var task1 = new Task(() => 
        //     {
        //         Console.WriteLine("task1 begin");
        //         System.Threading.Thread.Sleep(2000);
        //         Console.WriteLine("task1 finished");
        //     });
        //     task1.Start();
        //     task1.ContinueWith<string>(
        //         task=>{
        //             Console.WriteLine("task1 status: {0}", task.Status);
        //             return "this is end";
        //         }
        //     ).ContinueWith(task=>{
        //         Console.WriteLine(task.Result.ToString());
        //     });

        //     Console.Read();
        // }

        // static void Main(string[] args)
        // {
        //     var task1 = new Task(() =>
        //     {
        //         Console.WriteLine("Task 1 Begin");
        //         System.Threading.Thread.Sleep(2000);
        //         Console.WriteLine("Task 1 Finish");
        //     });
        //     var task2 = new Task(() =>
        //     {
        //         Console.WriteLine("Task 2 Begin");
        //         System.Threading.Thread.Sleep(3000);
        //         Console.WriteLine("Task 2 Finish");
        //     });


        //     task1.Start();
        //     task2.Start();
        //     var result = task1.ContinueWith<string>(task =>
        //     {
        //         Console.WriteLine("task1 finished!");
        //         return "This is task result!";
        //     });

        //     Console.WriteLine(result.Result.ToString());


        //     // Console.Read();
        // }

        // public static void Main(string[] args)
        // {
        //     var tokenSource = new CancellationTokenSource();
        //     var token = tokenSource.Token;
        //     var task = Task.Factory.StartNew(()=>{
        //         for (int i = 0; i < 1000; i++)
        //         {
        //             System.Threading.Thread.Sleep(1000);
        //             if(token.IsCancellationRequested)
        //             {
        //                 Console.WriteLine("Abort mission success!");
        //                 return;
        //             }
        //         }
        //     }, token);
        //     token.Register(()=>{
        //         Console.WriteLine("canceled");
        //     });

        //     Console.WriteLine("press enter to cancel task...");
        //     Console.ReadKey();
        //     tokenSource.Cancel();
        //     Console.ReadKey();
        // }

        // public static void Main(string[] args)
        // {
        //     Task<string> task1 = new Task<string>(getStr);
        //     task1.Start();
        //     task1.Wait();
        //     Console.WriteLine(task1.Result.ToString());
        // }

        // public static string getStr()
        // {
        //     HttpWebRequest request = (HttpWebRequest)WebRequest.Create("https://api.shunliandongli.com/v2/receiptpay/getSellerInfo");
        //     request.Method = "GET";
        //     HttpWebResponse response = (HttpWebResponse)request.GetResponse();
        //     Stream receiveStream = response.GetResponseStream();
        //     StreamReader readStream = new StreamReader(receiveStream, Encoding.UTF8);
        //     string str = readStream.ReadToEnd();
        //     response.Close();
        //     readStream.Close();
        //     // Console.WriteLine(str);
        //     return str;
        // }

        // static void Main(string[] args)
        // {
        //     callMethod();
        //     Console.ReadKey();
        // }

        // static async void callMethod()
        // {
        //     Task<int> task = Method1();
        //     Method2();
        //     int count = await task;
        //     Method3(count);
        // }

        // static async Task<int> Method1()
        // {
        //     int count = 0;
        //     return await Task.Run(()=>{
        //         Thread.Sleep(2000);
        //         for (int i = 0; i < 10; i++)
        //         {
        //             Console.WriteLine("Method 1");
        //             count += 1;
        //         }
        //         return count;
        //     });
            
        // }

        // static void Method2()
        // {
        //     for (int i = 0; i < 5; i++)
        //     {
        //         Console.WriteLine("Method 2");
        //     }
        // }

        // static void Method3(int count)
        // {
        //     Console.WriteLine("Total count is " + count);
        // }

        static void Main()
        {
            Task task = new Task(CallMethod);
            task.Start();
            task.Wait();
            Console.ReadKey();
        }

        static async void CallMethod()
        {
            string filePath = ".\\h5\\jquery3_5_1.js";
            Task<int> task = ReadFile(filePath);
            Console.WriteLine("Other work");
            int length = await task;
            Console.WriteLine(String.Format("Total length: {0}", length));
        }

        static async Task<int> ReadFile(string file)
        {
            int length = 0;
            Console.WriteLine("file reading is starting");
            using(StreamReader reader = new StreamReader(file)){
                string s = await reader.ReadToEndAsync();
                length = s.Length;
            }
            Console.WriteLine("file reading is completed");
            return length;
        }
    }
}