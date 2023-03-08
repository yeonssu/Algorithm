import java.util.Scanner;

public class SW1 {
    static int answer;
    static int R;
    static int C;
    static int[][] graph;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0,0,-1,1};
    static boolean[] visited = new boolean[26];
    public static void main(String[] args) throws Exception{
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();

        for (int t = 0; t < T; t++) {
            R = scanner.nextInt();
            C = scanner.nextInt();
            scanner.nextLine();

            graph = new int[R][C];
            for (int i = 0; i < R; i++) {
                String value = scanner.nextLine();
                for (int j = 0; j < value.length() ; j++) {
                    graph[i][j] = value.charAt(j) - 'A';
                }
            }
            dfs(0,0,0);
            System.out.printf("#%d %d\n",t+1,answer);
            answer = 0;
        }
    }

    static void dfs(int x, int y, int count){
        if (visited[graph[x][y]]) {
            answer = Math.max(answer,count);
        }
        else {
            visited[graph[x][y]] = true;
            for (int i = 0; i < 4; i++) {
                int xValue = x + dx[i];
                int yValue = y + dy[i];

                if(xValue>=0 && yValue>=0 && xValue<R && yValue<C) dfs(xValue,yValue, count+1);
            }
            visited[graph[x][y]] = false;
        }
    }

}
