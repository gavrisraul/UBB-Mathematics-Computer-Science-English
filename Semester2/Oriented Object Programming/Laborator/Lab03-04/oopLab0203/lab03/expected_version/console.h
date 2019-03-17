#ifndef CONSOLE
#define CONSOLE

#include <stdio.h>
#include <stdlib.h>

#include "repository.h"
#include "console.h"

typedef struct {
    stock     *currentStock;
}    console;

void    consoleInitialSetup(console **currentConsole);

void    consoleGetMedication(console *currentConsole, int index);

void    consoleGetAllMedications(console *currentConsole);

void    consoleAddMedication(console *currentConsole, char name[100], int concentration, int  quantity, float price);

void    consoleUpdateMedication(console *currentConsole, int index, char name[100], int concentration, int  quantity, float price);

void    consoleDeleteMedication(console *currentConsole, int index);

void    consoleSearchMedication(console *currentConsole, char subString[100]);

void    consoleSearchMedicationSorted(console *currentConsole, char subString[100]);

#endif