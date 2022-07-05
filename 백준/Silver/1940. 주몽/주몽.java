import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(reader.readLine());
        int M = Integer.parseInt(reader.readLine());

        String[] input = reader.readLine().split(" ");
        int[] ingredient = new int[N];
        for(int i=0; i<N; i++) {
            ingredient[i] = Integer.parseInt(input[i]);
        }
        Arrays.sort(ingredient);

        int start_point = 0;
        int end_point = N-1;
        int sum = 0, answer = 0;

        while(end_point > start_point) {
            sum = ingredient[start_point] + ingredient[end_point];
            if(sum == M) {
                answer++;
                start_point++;
                end_point--;
            }
            else if(sum < M) {
                start_point++;
            }
            else if(sum > M) {
                end_point--;
            }

        }

        writer.write(Integer.toString(answer));
        writer.flush();
        writer.close();

    }
}