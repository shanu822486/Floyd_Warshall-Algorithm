import copy
class Graph:
    
    def __init__(self,v):
        self.V=v
        self.graph=[[1000 for i in range(v)] for j in range(v)] 
        
    
    def AddEdge(self,u,v,w):
        self.graph[u][v]=w
       
        
    
    def Print(self,d):
        for i in range(self.V):
            for j in range(self.V):
                if d[i][j]==1000:
                    print('INF',end='  ')
                else:
                    print(d[i][j],end='   ')
            print()
                
    
    def FloydWarshall(self):
        d = copy.deepcopy(self.graph)
        
        
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    d[i][j]=min(d[i][j],d[i][k]+d[k][j])
                        
        
        self.Print(d)


a=Graph(4)                       
a.AddEdge(0,0,0)
a.AddEdge(0,1,5)
a.AddEdge(0,3,10)
a.AddEdge(1,2,3)
a.AddEdge(1,1,0)
a.AddEdge(2,2,0)
a.AddEdge(2,3,1)
a.AddEdge(3,3,0)

a.FloydWarshall()
    
    
    
    
            
        
