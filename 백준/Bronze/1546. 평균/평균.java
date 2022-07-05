import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        long N = Integer.parseInt(reader.readLine());
        String input = reader.readLine();
        String[] score = input.split(" ");
        double max = 0, answer = 0;

        for(int i=0; i<N; i++) {
            long this_score = Integer.parseInt(score[i]);
            answer += this_score;
            if(this_score >= max) {
                max = this_score;
            }
        }

        answer = answer/max * 100.0 / N;

        writer.write(Double.toString(answer));
        writer.flush();
        writer.close();
    

    }
}