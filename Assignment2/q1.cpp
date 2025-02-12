#include<iostream> 
#include<vector> 
#include<sstream> 
using namespace std; 
class Perceptron{ 
private:  
 vector<int>x1={0,0,1,1}; 
 vector<int>x2={0,1,0,1}; 
 vector<vector<int>>y={{0,0,0,1},{0,1,1,1}}; 
 int w0,w1,w2,w3; 
 void train(){ 
  while(true){ 
   bool changed=false; 
   for(int i=0;i<4;++i){ 
    for(int j=0;j<2;++j){ 
     int a=x1[i],b=x2[i],c=j; 
     int pred=y[j][i]; 
     int sum=summation(a,b,c); 
     if(sum>=0 && pred==0){ 
      update(a,b,c,-1); 
      changed=true; 
     }else if(sum<0 && pred==1){ 
      update(a,b,c,1); 
      changed=true; 
     } 
    } 
   }  
   if(!changed){ 
    break; 
   } 
  } 
 } 
 
 int summation(int x,int y,int z){ 
  return w0+w1*x+w2*y+w3*z; 
 } 
 void update(int a,int b,int c,int diff){ 
  w0=w0+diff; 
  w1=w1+diff*a; 
  w2=w2+diff*b; 
  w3=w3+diff*c; 
 } 
public: 
 Perceptron(){ 
  w0=0,w1=0,w2=0,w3=0; 
  train(); 
 } 
 void predict(string str){ 
  vector<string>v; 
  stringstream ss(str); 
  string word; 
  while(ss >> word){ 
   v.push_back(word); 
  } 
  if(v.size()!=3){ 
   cout<<"Invalid String"<<endl; 
   return; 
  } 
  int a=1,b=1,c=0; 
  if(v[0][0]=='~'){ 
   a--; 
  } 
  if(v[2][0]=='~'){ 
   b--; 
  } 
  if(v[1]=="V"){ 
} 
c=1; 
int sum=summation(a,b,c); 
int ans=(sum>=0); 
cout<<str<<" = "<<ans<<endl; 
} 
}; 
int main(){ 
Perceptron p; 
p.predict("x ^ y"); 
p.predict("x ^ ~y"); 
p.predict("~x ^ y"); 
p.predict("~x ^ ~y"); 
p.predict("x V y"); 
p.predict("x V ~y"); 
p.predict("~x V y"); 
p.predict("~x V ~y"); 
} 