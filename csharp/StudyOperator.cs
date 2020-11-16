using System;

public readonly struct Fraction
{
    private readonly int num;
    private readonly int den;
    public Fraction(int numerator, int denominator)
    {
        if(denominator == 0)
        {
            throw new ArgumentException("Denominator cannot be zero.", nameof(denominator));
        }
        num = numerator;
        den = denominator;
    }
    public static Fraction operator +(Fraction a) => a;
    public static Fraction operator -(Fraction a) => new Fraction(-a.num, a.den);
    public static Fraction operator +(Fraction a, Fraction b)
                                        => new Fraction(a.num * b.den + b.num * a.den, a.den * b.den);
    public static Fraction operator -(Fraction a, Fraction b)
                                        => a + (-b);
    public static Fraction operator *(Fraction a, Fraction b)
                                        => new Fraction(a.num * b.num, a.den * b.den);
    public static Fraction operator /(Fraction a, Fraction b)
    {
        if(b.num == 0)
        {
            throw new DivideByZeroException();
        }
        return  new Fraction(a.num * b.den, a.den * b.num);
    }
    public override string ToString()
    {
        return $"{num} / {den}";
    }
}

public static class Op
{
    public static void Main()
    {
        var a = new Fraction(5,4);
        var b = new Fraction(1,2);
        Console.WriteLine(-a);
        Console.WriteLine(a + b);
    }
}