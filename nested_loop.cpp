#include<iostream>
using namespace std;

int main(){
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            if(j < 2){
                cout <<" 1 ";
            }else{
                cout <<" 0 ";
            }

        }
        cout<<endl;
    }
    cout<<endl;
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            if(i < 3){
                cout <<" 1 ";
            }else{
                cout <<" 0 ";
            }

        }
        cout<<endl;
    }
    cout<<endl;
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            if(i != j){
                cout <<" 1 ";
            }else{
                cout <<" 0 ";
            }

        }
        cout<<endl;
    }
    return 0;
}