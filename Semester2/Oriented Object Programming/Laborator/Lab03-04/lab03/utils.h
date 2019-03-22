#ifndef UTILS
#define UTILS

#include <string.h>

/*
* Checks if a string contains a substring
* in: "aa" "fsaba  sagg aa"
* out: 1
* in: "daf" "hytn ev afr"
* out: 0
*/
int strIsContained(char needle[100], char haystack[100]);

#endif