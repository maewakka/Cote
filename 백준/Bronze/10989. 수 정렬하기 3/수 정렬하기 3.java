import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(reader.readLine());

        int[] numArray = new int[N];
        for(int i=0; i<N; i++) {
            numArray[i] = Integer.parseInt(reader.readLine());
        }
        Arrays.sort(numArray);
        for(int i=0; i<N; i++) {
            writer.write(Integer.toString(numArray[i]));
            writer.newLine();
        }
        writer.close();
    }
}
