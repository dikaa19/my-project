#include<iostream>
#include<string>
using namespace std;

int main(){
    int tabel[3][4]= { {6,4,4,4},{7,8,2,6},{5,8,6,3} };
    int indeks;
    float rerata, jumlah;
    char lanjut;
    string pilih;
    
    for(int i=0; i<3; i++)
    {
        for (int j = 0; j < 4; j++)
        {
        cout << tabel[i][j]<<" ";
        }
        cout << endl;
    }
    do{
    jumlah = 0;
    rerata = 0;
    cout <<"Apa yang ingin anda hitung (baris/kolom) : ";
    cin >> pilih;
    if (pilih == "baris")
    {
        cout <<"baris ke berapa yang ingin anda hitung? : ";
        cin  >> indeks;
        indeks -= 1;
        for (int k = 0; k < 4; k++)
        {
            cout << tabel[indeks][k]<<" ";
            jumlah += tabel[indeks][k];
        }
        rerata = jumlah / 4;
        cout << endl;
        cout << "jumlah = "<<jumlah<<endl;
        cout << "rerata = "<<rerata<<endl;
    }
    else if (pilih == "kolom")
    {
        cout <<"kolom ke berapa yang ingin anda hitung? : ";
        cin  >> indeks;
        indeks -= 1;
        for (int l = 0; l < 3; l++)
        {
            cout << tabel[l][indeks]<<" ";
            jumlah += tabel[l][indeks];
        }
        rerata = jumlah / 3;
        cout << endl;
        cout << "jumlah = "<<jumlah<<endl;
        cout << "rerata = "<<rerata<<endl;
    }
    cout << "Apakah mau lanjut menghitung?: ";
    cin >> lanjut;
    }while(lanjut == 'y');
    
    return 0;
}