import java.io.IOException;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(reader.readLine());
        String input = reader.readLine();

        int answer = 0;

        for(int i=0; i<N; i++) {
            answer += Character.getNumericValue(input.charAt(i));
        }

        writer.write(Integer.toString(answer));
        writer.flush();
        writer.close();

    }
}