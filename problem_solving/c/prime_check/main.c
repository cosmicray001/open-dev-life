#include <stdio.h>

int main()
{
    int n;
    int isPrime = 1; // Initially set to Prime (true)
    printf("\t-: Prime Number Checker :-\n");
    printf("Enter a number: ");
    scanf("%d",&n);
    for (int i = 2; i * i < n; i++)
    {
        if (n % i == 0)
        {
            isPrime = 0;
        }
    }
    if (isPrime)
    {
        printf("%d is Prime Number.\n", n);
    }
    else
    {
        printf("%d is not a Prime number i.e. Composite number.\n", n);
    }
}
