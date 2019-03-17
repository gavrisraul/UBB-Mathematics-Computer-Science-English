#include <stdio.h>
#include <math.h>
#include <string.h>

/*
* Struct vector with length and static arr
*/
struct vector{
    int length;
    int arr[100];
};

/*
* Function to read a vector struct
*/
void read_vector(struct vector  *p_v){
    scanf("%d", &p_v->length);
    for(int i = 1; i <= p_v->length; ++i)
        scanf("%d", &p_v->arr[i]);
}

/*
* Function to write a vector struct
*/
void write_vector(struct vector *p_v){
    for(int i = 0; i < p_v->length; ++i)
        if(p_v->arr[i])
            printf("%d ", p_v->arr[i]);
}

/*
* Function to check if a number is prime or not
* .in: 2
* .out: 1
* .in: 4
* .out: 0
*/
int is_prime(int nr){
    if(nr <= 1)
        return 0;
    for(int d = 2; d <= sqrt(nr); ++d)
        if(nr % d == 0)
            return 0;
    return 1;
}

/*
* Function to check for the maximum of two numbers
* .in: 1 2
* .out: 2
*/
int max(int a, int b){
    if(a > b)
        return a;
    return b;
}

/*
* Function to solve requirement a. Prints all prime
* numbers smaller than n and stores them in a vector
* .in: 10
* .out: 2 3 5 7
*/
void solve_a(int n, struct vector *p_v){
    scanf("%d", &n);
    for(int nr = 1; nr <= n; ++nr)
        if(is_prime(nr))
            p_v->arr[p_v->length++] = nr;
    write_vector(p_v);
}

/*
* Function to solve requirement b. Prints the longest
* contiguous subsequence that every 2 element their sum
* is prime
* .in: 6 -> 1 6 1 6 1 6
* .out: 6
* .in: 6 -> 1 6 1 6 2 4
* .out: 4
*/
void solve_b(struct vector *p_v){
    read_vector(p_v);
    int i, j = 1, mx_subseq = 1;
    for(int i = 1; i < p_v->length; ++i){
        if(is_prime(p_v->arr[i] + p_v->arr[i + 1]))
            j++;
        else
            j = 1;
        mx_subseq = max(j, mx_subseq);
    }
    printf("%d\n", mx_subseq);
}

/*
* Function to print the menu of the application
*/
void menu(){
    int option;
    char menu[256];
    strcat(menu, "\n\t1.solve_a\n");
    strcat(menu, "\t2.solve_b\n");
    strcat(menu, "\t0.exit\n");
    printf("%s", menu);
    scanf("%d", &option);
    while(1){
        switch(option){
            case 1:{
                int n;
                struct vector v;
                solve_a(n, &v);
                break;
            }
            case 2:{
                struct vector v;
                solve_b(&v);
                break;
            }
            case 0:
                return;
            break;
            default:
            break;
        }
        printf("%s", menu);
        scanf("%d", &option);
    }
}

/*
* Check on ram
*/
void main(){
    menu();
    return;
}

