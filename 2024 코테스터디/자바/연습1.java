import java.io.*;

// 홀짝판단
public class 연습1 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int number = Integer.parseInt(br.readLine());

    if (number % 2 == 0) {
      System.out.println(number + "is even");
    } else {
      System.out.println(number + "is Odd");
    }
  }
}
