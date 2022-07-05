import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] firstLine = reader.readLine().split(" ");
        int N = Integer.parseInt(firstLine[0]);
        int M = Integer.parseInt(firstLine[1]);

        String[] array = reader.readLine().split(" ");
        int[] sum_array = new int[N+1];
        sum_array[0] = 0;
        int sum = 0;

        for(int i=0; i<N; i++) {
            int this_num = Integer.parseInt(array[i]);
            sum += this_num;
            sum_array[i+1] = sum;
        }

        for(int i=0; i<M; i++) {
            String[] Line = reader.readLine().split(" ");
            int A = Integer.parseInt(Line[0]);
            int B = Integer.parseInt(Line[1]);

            int answer = sum_array[B] - sum_array[A-1];
            writer.write(Integer.toString(answer));
            writer.newLine();
        }

        writer.flush();
        writer.close();

    }
}