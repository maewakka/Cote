import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        int N, k = 0;

        String[] first_line = reader.readLine().split(" ");
        N = Integer.parseInt(first_line[0]);
        k = Integer.parseInt(first_line[1]);

        String[] input = reader.readLine().split(" ");
        int[] score = new int[N];
        for(int i=0; i<N; i++) {
            score[i] = Integer.parseInt(input[i]);
        }

        Arrays.sort(score);

        System.out.println(score[N-k]);
    }
}
