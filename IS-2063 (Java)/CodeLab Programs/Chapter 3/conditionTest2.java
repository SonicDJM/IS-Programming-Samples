public class conditionTest2
{
  public static void main(String[] args)
  {
    int outsideTemp;
    outsideTemp = 100;
    int selfLife = 20;
    
    if (outsideTemp > 90)
    selfLife -= 4;
    
    System.out.println(selfLife);
  }
}