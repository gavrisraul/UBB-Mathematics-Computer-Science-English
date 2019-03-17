#include <stdio.h>
/*
    a. Read sequences of positive integer numbers (reading of each sequence
ends by 0, reading of all  thesequences ends  by -1)  and  determine  the
maximum  element of  each  sequence  and  the maxim element of the global
sequence.b. Given a vector of numbers, find the longest contiguous subsequence
such that all elements are in a given interval

    Lab activity - 4 - Read a sequence of natural numbers (sequence ended by 0)
and determine the number of 0 digits of the product ofthe read numbers.
*/


/*
Read a n by m integer matrix and return it's length.
In: array or integer arrays to populate
Out: the length of the array
*/
int     readMatrix(int matrix[][100]) {
    int currentNumber, rowIndex=0, colIndex=0;

    scanf("%d", &currentNumber);
    while (currentNumber != -1) {
       matrix[rowIndex][colIndex++] = currentNumber;
       scanf("%d", &currentNumber);

       if (currentNumber == 0) {
           matrix[rowIndex][colIndex++] = currentNumber;
           rowIndex++;
           colIndex = 0;
           scanf("%d", &currentNumber);
       }
   }

   return rowIndex;
}

/*
Display a given n by m matrix on the screen.
In: len,  array or integer arrays to print
Out: nothing
*/
void     printMatrix(int len, int matrix[][100]) {
    int j=0;

    for (int i=0; i<len; i++) {
        do {
            printf("%d\t", matrix[i][j]);
        } while (matrix[i][j++] != 0);

        printf("\n");
        j = 0;
    }
}

/*
Display the maximum of each sequence and the maximum from all sequences.
In: len the length of the matrix, matrix array or integer arrays to check
Out: nothing
*/
void     printMax(int len, int matrix[][100]) {
    int rowMax, max=matrix[0][0], j=0;

    for (int i=0; i<len; i++) {
        rowMax = matrix[i][0];

        do {
            if (max < matrix[i][j])
                max = matrix[i][j];
            if (rowMax < matrix[i][j])
                rowMax = matrix[i][j];
        } while (matrix[i][j++] != 0);

        printf("Sequence %d max is %d\n", i, rowMax);
        j = 0;
    }
    printf("Array max is %d\n", max);
}

void exa() {
    int     matrix[100][100];
    int     len;

    len = readMatrix(matrix);
    printf("\nMatrix:\n");
    printMatrix(len, matrix);
    printf("\n");
    printMax(len, matrix);
}

/*
Read a vector
In: vectory in memory to read
Out: length of the vector
*/
int     readVector(int vector[]) {
    int currentNumber, index=0;

    scanf("%d", &currentNumber);
    while (currentNumber != -1) {
        vector[index++] = currentNumber;
        scanf("%d", &currentNumber);
    }

    return index;
}

/*
Find the longest subsequnce in between a given interval.
In: len length of the vector, and vector array of integers
Out: nothing
*/
void     longestSubSequence(int len, int vector[]) {
    int     intervalStart, intervalEnd;
    printf("Interval start: ");
    scanf("%d", &intervalStart);
    printf("\n");
    printf("Interval end: ");
    scanf("%d", &intervalEnd);
    printf("\n");

    int     longestStartIndex=-1, longLen=0, currentStartIndex=-1, currentLen=0, i=0;

    while (i < len) {
        if (intervalStart <= vector[i] && vector[i] <= intervalEnd) {
            currentStartIndex = i;
            currentLen = 1;

            while (intervalStart <= vector[i] && vector[i] <= intervalEnd) {
                currentLen++;
                i++;
            }
            if (currentLen > longLen) {
                longestStartIndex = currentStartIndex;
                longLen = currentLen;
            }
        }
        else
            i++;
    }

    printf("Longest subsequence in [%d, %d]:\n", intervalStart, intervalEnd);
    while (intervalStart <= vector[longestStartIndex] && vector[longestStartIndex] <= intervalEnd) {
        printf("%d\t", vector[longestStartIndex]);
        longestStartIndex++;
    }
    printf("\n");
}

void     exb() {
    int     vector[100];
    int     len;

    len = readVector(vector);
    longestSubSequence(len, vector);
}


void     lab2Activity() {
    int n1, n2, product, count;

    printf("\nInput the first number: ");
    scanf("%d", &n1);
    printf("\nInput the second number: ");
    scanf("%d", &n2);

    product = n1 * n2;

    count = 0;
    while (product > 0 && product % 10 == 0) {
        count++;
        product /= 10;
    }

    printf("\nThere are %d trailing 0s in the product of %d and %d (=%d)\n", count, n1, n2, n1 * n2);
}

int     main(void){
    char    option;

    printf("Choose an option:\n");
    printf("\ta - subpoint a\n");
    printf("\tb - subpoint b\n");
    printf("\tc - lab activity 2\n");
    scanf("%c", &option);

    if (option == 'a')
        exa();
    else if (option == 'b')
        exb();
    else if (option == 'c')
        lab2Activity();
    else
        printf("Invalid option!");

};
