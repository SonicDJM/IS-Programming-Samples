public class stringMethod
{ 
  public static String max(String a, String b)
  {
     String max1 = a;
     if (b.compareTo(max1)>0) max1 = b;
     return max1;
  }
  
  public static void main(String[] args)
  { 
    String small = "two";
    String large = "three";
    String value = max(small, large);
    System.out.println(value);
  }
}
