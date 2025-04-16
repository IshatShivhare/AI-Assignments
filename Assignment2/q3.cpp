#include<iostream>
#include<vector> 
#include<stdlib.h> 
#include<fstream> 
using namespace std; 
class Perceptron{ 
private: 
 int n; 
 string str; 
 int range=100;          
    
 vector<vector<int>>inputs; 
 vector<int>outputs; 
 vector<int>weights; 
 void generate(){ 
  int p=1<<n; 
  for(int i=0;i<p;++i) 
  { 
   for(int j=0;j<n;++j){ 
    int mask=1<<j; 
    int bit=mask&i; 
    inputs[j][i]=(bit>0)?1:0; 
   } 
  } 
 } 
 void getRandom(){ 
  for(int i=0;i<weights.size();++i){ 
   weights[i]=rand()%range; 
  } 
 } 
public: 
 int train(){ 
  getRandom(); 
  cout<<"Initial Weights: "; 
  for(int it:weights){ 
   cout<<it<<" "; 
  }cout<<endl; 
  int epochs=0; 
  while(true){ 
   epochs++; 
   bool changed=false; 
   for(int i=0;i<inputs[0].size();++i) 
   { 
    int sum=weights[0]; 
    for(int j=0;j<n;++j){ 
     sum+=(weights[j+1]*inputs[j][i]); 
    }      
    int pred=outputs[i]; 
    if(sum>=0 && pred==0){ 
     changed=true; 
     update(i,-1); 
    }else if(sum<0 && pred==1){ 
     changed=true; 
     update(i,1); 
    } 
   } 
   if(!changed){ 
    break; 
   } 
  } 
  cout<<"Final Weights: "; 
  for(int it:weights){ 
   cout<<it<<" "; 
  }cout<<endl; 
  cout<<"Iterations: "<<epochs<<endl; 
  return epochs; 
 } 
private: 
 void update(int col,int diff){ 
  weights[0]+=diff; 
  for(int i=0;i<n;++i){ 
   weights[i+1]=weights[i+1]+diff*(inputs[i][col]); 
  } 
 } 
public: 
Perceptron(int n,string str,vector<int>outputs){ 
this->n=n; 
this->str=str; 
this->outputs=outputs; 
inputs.resize(n,vector<int>(1<<n)); 
weights.resize(n+1,0); 
generate(); 
} 
}; 
int main(){ 
ofstream f("file.txt"); 
Perceptron p(2,"x ^ y",{0,0,0,1}); 
for(int i=0;i<10;++i){ 
int v=p.train(); 
f<<v<<endl; 
} 
}