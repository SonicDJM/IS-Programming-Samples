public class minComp
{ 
  public static int min(int a, int b)
  {
    int value;
     if (b > a)
     {
       value = a;
     }
     else
     {
       value = b;
     }
     return value;
  }
  
  public static void main(String[] args)
  { 
    int big = 40;
    int small = 10;
    int value = min(small, big);
    System.out.println(value);
  }
}
