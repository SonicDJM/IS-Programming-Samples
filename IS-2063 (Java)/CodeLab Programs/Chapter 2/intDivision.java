public class intDivision
{
  public static void main(String[] args)
  {
    int price = 4321;
    int cents = price % 100;
    int dollar = price / 100;
    System.out.println(dollar + " dollars and " + cents + " cents");
  }
}