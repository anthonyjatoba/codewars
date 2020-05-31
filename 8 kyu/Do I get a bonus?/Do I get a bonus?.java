public class Kata{
  public static String bonusTime(final int salary, final boolean bonus) {
    int value = bonus ? 10 * salary : salary;
    return "\u00A3" + value;
  }
}