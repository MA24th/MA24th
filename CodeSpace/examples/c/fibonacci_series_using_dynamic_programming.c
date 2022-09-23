#include<stdio.h>

// Fibonacci Series using Dynamic Programming
// Author: Mustafa Asaad
// Creation: 16 JUL, 2021

int fib(int n) 
{
  int f[n+2];
  int i;
  f[0] = 0;
  f[1] = 1;
 

  for (i = 2; i <= n; i++){
      f[i] = f[i-1] + f[i-2];
  }

  return f[n];
}


int main ()
{

  int n;
  int inpt = scanf("%d", &n);
  if ( inpt < 1) {
      printf("FibNum[%d]=> %d\n", 9, fib(9));
      printf("FibNum[%d]=> %d\n", 11, fib(11));
      printf("FibNum[%d]=> %d\n", 50, fib(50));
    
  }
  else {
      printf("FibNum[%d]=> %d", n, fib(n));
  }
  

  return 0;
}