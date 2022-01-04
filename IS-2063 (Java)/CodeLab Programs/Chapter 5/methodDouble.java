import java.lang.Math;
public class methodDouble
{ 
  public static double powerTo(double a, int b)
  {
    if(b < 0)
    {
      return 0;
    }
    else
    {
      double temp = Math.pow(a, b);
      return temp;
    }
  }
  
  public static void main(String[] args)
  { 
    double first = 5.5;
    int second = 10;
    //int second = 0; //Alt
    double awns = powerTo(first, second);
    System.out.println(awns);
  }
}
