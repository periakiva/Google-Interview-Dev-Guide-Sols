#include<iostream>
#include<stdio.h>
#include<string>
#include<string.h>
using namespace std;

int main(int argc, char **argv){

    char foo[] = {'h','e','l','l','o'};
    for(int i=0;i<(unsigned)strlen(foo);i++)
        cout << foo[i];

    cout << endl;
    for(int i=strlen(foo);i>=0;i--)
        cout << foo[i];



}

