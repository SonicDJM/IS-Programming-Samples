public class ifLoopIntro
{
  public static void main(String[] args)
  {
    int hoursWorked;
    hoursWorked = 50;
    boolean workedOvertime;
    
    if (hoursWorked > 40)
    workedOvertime = true;
    else
    workedOvertime = false;
    
    System.out.println(workedOvertime);
  }
}