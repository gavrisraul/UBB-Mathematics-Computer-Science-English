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
* Function to check for the gcd of two numbers
* .in: 152 52
* .out: 4
*/
int gcd(int a, int b){
    if(b == 0)
        return a;
    return
        gcd(b, a%b);
}

/*
* Function that checks if the numbers have
* the same digits
* .in: 123 123123
* .out: 1
* .in: 215 5246
* .out: 0
*/
int same_digits(int a, int b){
    int x[10] = {0}, y[10] = {0};
    while(a){
        x[a % 10] = 1;
        a /= 10;
    }
    while(b){
        y[b % 10] = 1;
        b /= 10;
    }
    for(int cif = 0; cif <= 9; ++cif)
        if(x[cif] != y[cif])
            return 0;
    return 1;
}

/*
* Function to solve requirement a.
* .in:
* .out:
*/
void solve_a(int n, struct vector *p_v){
    scanf("%d", &n);
    int i = 0, nr = 3;
    while(i < 8){
        if(is_prime(nr))
            p_v->arr[p_v->length++] = nr;
        i++;
        nr++;
    }
    write_vector(p_v);
}

/*
* Function to solve requirement b.  Prints the longest
* contiguous subsequence that every 2 elements have the
* same digits
* .in: 6 -> 231 231 1231 231 21321 231
* .out: 6
* .in: 6 -> 321 656 65 565 321 213
* .out: 3
*/
void solve_b(struct vector *p_v){
    read_vector(p_v);
    int i, j = 1, mx_subseq = 1;
    for(int i = 1; i < p_v->length; ++i){
        if(same_digits(p_v->arr[i], p_v->arr[i + 1]))
            j++;
        else
            j = 1;
        mx_subseq = max(j, mx_subseq);
    }
    printf("%d\n", mx_subseq);
}

int abs(int a){
    if(a < 0)
        return a;
    return a;
}

/*
* Function to check if 2 numbers are twin primes
* .in: 3 5
* .out: 1
* .in: 14 12
* .out: 0
*/
int twin_primes(int a, int b){
    int diff = abs(a - b);
    if(diff == 2)
        if(is_prime(a) && is_prime(b))
            return 1;
    return 0;
}

void solve_8_lab_activity(int n){
    scanf("%d", &n);
    int nr1 = 2, i = 0;;
    int nr2 = nr1 + 2;
    while(i < n){
        if(twin_primes(nr1, nr2)){
            printf("%d %d\n", nr1, nr2);
            i++;
        }
        nr1++;
        nr2++;
    }
}

/*
* Function to print the menu of the application
*/
void menu(){
    int option;
    char menu[256];
    strcat(menu, "\n\t1.solve_a\n");
    strcat(menu, "\t2.solve_b\n");
    strcat(menu, "\t3.solve_8_lab_activ\n");
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
            case 3:{
                int n;
                solve_8_lab_activity(n);
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

