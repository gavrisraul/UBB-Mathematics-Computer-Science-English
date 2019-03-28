#include <string.h>

int strIsContained(char needle[100], char haystack[100]) {
    void *voidPointer;
    char *start;
    voidPointer = NULL;
    start = strstr(needle, haystack);
    if (start == voidPointer)
        return 0;
    return 1;
}
