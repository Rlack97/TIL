import java.io.*;

//덧셈

public class 연습2 {
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int num1 = Integer.parseInt(br.readLine());
    int num2 = Integer.parseInt(br.readLine());

    int sum = num1 + num2;
    System.out.println(sum);
  }
}