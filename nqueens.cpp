#include <iostream>
using namespace std;

bool isSafe(int** arr,int x,int y,int n){
    for (int row =0 ; row < x ; row++){
        if(arr[row][y] == 1){
            return false;
        }
    }
    int row = x;
    int col = y;
    while (row>=0 and col >=0){
        if(arr[row][col] == 1){
            return false;
        }
        col--;
        row--;
    }
    col = x;
    row = y;
    while (row>=0 and col < x){
        if(arr[row][col] == 1){
            return false;
        }
        col++;
        row--;
    }
    return true;
}

bool nQueens(int** arr , int x , int n){
    if(x>=n){
        return true;
    }
    for (int col = 0; col <n ; col++)
    {
        if(isSafe(arr,x,col,n)){
            arr[x][col] = 1;
            if(nQueens(arr,x+1,n)){
                return true;
            }
            arr[x][col] = 0;
        }

    }
    return false;
    
}




int main(){
    int n;
    cout<<"Enter the number of queen";
    cin>>n;
    int** arr = new int*[n];
    for(int i =0;i<n;i++){
        arr[i]=new int[n];
        for (int j = 0; j < n; j++)
        {
            arr[i][j]=0;
        }
    }
    if(nQueens(arr,0,n)){
        for(int i =0;i<n;i++){
        for (int j = 0; j < n; j++)
        {
            cout<<arr[i][j]<<" ";
        }cout<<endl;
    }
    }
    return 0;
}