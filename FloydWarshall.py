Problem Statement



The Floyd-Warshall Algorithm is for solving all pairs of shortest-path problems. The problem is to find the shortest distances between every pair of vertices in a given edge-weighted directed graph. 

Input format :
The first line of input represents the size N.

The next N*N Matrix represents the distance.

Note: The distance between one city and itself will be 0, and the distance will be 999 if there is no direct edge between the two cities.

Output format :
The output prints the shortest distance between every pair of cities.

If there is no shortest path between two cities, then print INF.



Refer to the sample output for formatting specifications.

Sample test cases :
Input 1 :
4
0 5 999 10
999 0 3 999
999 999 0 1
999 999 999 0
Output 1 :
0 5 8 9 
INF 0 3 4 
INF INF 0 1 
INF INF INF 0 


Problem:
def floyd(n, graph):
    dist=[row[:] for row in graph]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != 999 and dist[k][j] != 999:
                    dist[i][j]=min(dist[i][j], dist[i][k]+dist[k][j])
                    
    for i in range(n):
        for j in range(n):
            if dist[i][j]==999:
                print("INF", end=" ")
            else:
                print(dist[i][j], end=" ")
        print()
n=int(input())
graph=[]
for _ in range(n):
    row=list(map(int, input().split()))
    graph.append(row)
floyd(n, graph)
