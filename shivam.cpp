#include<bits/stdc++.h>
#include<omp.h>
using namespace std;

 
 class Graph{
  public:
  int n;
  vector<int>v1[6];
  Graph(int n1){
    n=n1;
  }
  void addedge(){
    cout<<"Enter number of edges of graph\n";
    int x;cin>>x;
    for(int i=0;i<x;i++){
      int x,y;cin>>x>>y;
      v1[x].push_back(y);
      v1[y].push_back(x);
    }

    cout<<"Your graph is \n";
    for(auto x:v1){
      for(auto x1:x){
        cout<<x1<<" ";
      }
      cout<<endl;
    }
    
  }

  void bfs(){
    vector<int>visited(6,0);
    queue<int>q1;
    q1.push(0);
    while(q1.size()){
      int ans= q1.front();
      q1.pop();
      cout<<ans<<" ";
      visited[ans]=1;
      for(auto x : v1[ans]){
        if(visited[x]==0){
          q1.push(x);
             visited[x]=1;
        }
         visited[x]=1;

      }
    }
  }
  void dfs(){
     vector<int>visited(6,0);
    stack<int>q1;
    q1.push(0);
    while(q1.size()){
      int ans= q1.top();
      q1.pop();
      cout<<ans<<" ";
      visited[ans]=1;
      for(auto x : v1[ans]){
        if(visited[x]==0){
          q1.push(x);
             visited[x]=1;
        }
         visited[x]=1;

      }
    }
  }
 };
int main(){
  
 Graph g1(5);
 g1.addedge();
 cout<<"BFS :"<<endl;
 g1.bfs();
 g1.dfs();

}


