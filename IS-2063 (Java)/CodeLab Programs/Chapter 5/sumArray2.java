public class sumArray2
{ 
  public static double sumArray(double[] a)
  {
    double sum = 0;
    for (int i=0; i < a.length; i++)
    {
      sum = sum + a[i];
    }
    sum = sum / a.length;
    return sum;
  }
  
  public static void main(String[] args)
  { 
    double[] temps = new double[]{1.3,5.7,10.2,25.1,50.0,100.8};
    double avgTemp = sumArray(temps);
    System.out.println(avgTemp);
  }
}
