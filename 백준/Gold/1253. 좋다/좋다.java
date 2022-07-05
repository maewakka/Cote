import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        int answer = 0;
        int N = Integer.parseInt(reader.readLine());

        String[] input = reader.readLine().split(" ");
        long[] numbers = new long[N];
        long sum = 0;
        for(int i=0; i<N; i++) {
            numbers[i] = Integer.parseInt(input[i]);
        }
        Arrays.sort(numbers);

        for(int k=0; k<N; k++) {
            long this_num = numbers[k];
            int start_point = 0;
            int end_point = N-1;

            while(start_point < end_point) {
                sum = numbers[start_point] + numbers[end_point];
                if(sum == this_num) {
                    if(start_point == k) {
                        start_point++;
                    }
                    else if(end_point == k) {
                        end_point--;
                    }
                    else {
                        answer++;
                        break;
                    }
                }
                else if(sum > this_num) {
                    end_point--;
                }
                else if(sum < this_num) {
                    start_point++;
                }
            }

        }

        writer.write(Integer.toString(answer));
        writer.flush();
        writer.close();

    }
}