public class methodInt
{ 
  public static void printLarger(int a, int b)
  {
    if(a > b)
    {
      System.out.println(a);
    }
    if(b > a)
    {
      System.out.println(b);
    }
  }
  
  public static void main(String[] args)
  { 
    int larger = 45;
    int smaller = 15;
    printLarger(larger, smaller);
  }
}

