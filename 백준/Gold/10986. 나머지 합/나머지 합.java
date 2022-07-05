import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] firstLine = reader.readLine().split(" ");
        int N = Integer.parseInt(firstLine[0]);
        int M = Integer.parseInt(firstLine[1]);

        long answer = 0, sum = 0;
        long[] remainder = new long[M+1];

        String[] input = reader.readLine().split(" ");
        long[] sum_array = new long[N];

        for(int i=0; i<N; i++) {
            sum += Integer.parseInt(input[i]);
            sum_array[i] = sum;
        }


        for(int i=0; i<N; i++) {
            int rest = (int) (sum_array[i] % M);
            if(rest == 0) {answer+=1;}
            remainder[rest]++;
        }

        for(int i=0; i<M; i++) {
            if(remainder[i] != 0) {
                answer += remainder[i] * (remainder[i]-1) / 2;
            }
        }

        writer.write(Long.toString(answer));
        writer.flush();
        writer.close();

    }
}