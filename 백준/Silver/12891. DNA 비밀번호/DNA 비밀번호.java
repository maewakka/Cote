import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] firstLine = reader.readLine().split(" ");
        int S = Integer.parseInt(firstLine[0]);
        int P = Integer.parseInt(firstLine[1]);

        String DNA_string = reader.readLine();

        String[] input = reader.readLine().split(" ");

        int slide_count = S - P + 1;
        int slide_point = P;
        int answer = 0;
        int[] check = new int[4];
        int A=0, C=0, G=0, T=0;

        for(int i=0; i<P; i++) {
            if(DNA_string.charAt(i) == 'A') {
                A++;
            }
            else if(DNA_string.charAt(i) == 'C') {
                C++;
            }
            else if(DNA_string.charAt(i) == 'G') {
                G++;
            }
            else if(DNA_string.charAt(i) == 'T') {
                T++;
            }
        }

        check[0] = A;
        check[1] = C;
        check[2] = G;
        check[3] = T;
        int true_count = 0;

        for(int j=0; j<4; j++) {
            if(check[j] >= Integer.parseInt(input[j])) {
                true_count++;
            }
        }
        if(true_count == 4) {
            answer++;
        }

        for(int i=1; i<slide_count; i++) {
            char left = DNA_string.charAt(i-1);
            char last = DNA_string.charAt(i-1+P);

            if(left == 'A') {
                check[0]--;
            } else if(left == 'C') {
                check[1]--;
            } else if(left == 'G') {
                check[2]--;
            } else if(left == 'T') {
                check[3]--;
            }

            if(last == 'A') {
                check[0]++;
            } else if(last == 'C') {
                check[1]++;
            } else if(last == 'G') {
                check[2]++;
            } else if(last == 'T') {
                check[3]++;
            }

            true_count = 0;
            for(int j=0; j<4; j++) {
                if(check[j] >= Integer.parseInt(input[j])) {
                    true_count++;
                }
            }
            if(true_count == 4) {
                answer++;
            }
        }

        writer.write(Integer.toString(answer));
        writer.flush();
        writer.close();

    }
}