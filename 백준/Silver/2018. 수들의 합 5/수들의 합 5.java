import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(reader.readLine());
        int start_point = 1;
        int end_point = 1;
        int sum = 1, answer = 1;

        while(end_point != N) {

            if(sum == N) {
                answer += 1;
                end_point++;
                sum+=end_point;
            } else if (sum > N) {
                sum-=start_point;
                start_point++;
            } else if (sum < N) {
                end_point++;
                sum+=end_point;
            }
        }

        writer.write(Integer.toString(answer));
        writer.flush();
        writer.close();

    }
}