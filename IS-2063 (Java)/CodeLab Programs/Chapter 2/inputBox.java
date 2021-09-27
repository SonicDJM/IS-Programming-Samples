import javax.swing.JOptionPane;
public class inputBox
{
  public static void main(String[] args)
  {
    String name;
    name = JOptionPane.showInputDialog("Enter your name");
    JOptionPane.showMessageDialog(null, "Your name is: " + name);
  }
}