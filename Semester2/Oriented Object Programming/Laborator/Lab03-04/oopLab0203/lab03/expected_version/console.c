#include <stdio.h>
#include <stdlib.h>

#include "repository.h"
#include "console.h"

void    consoleInitialSetup(console **currentConsole) {
    *currentConsole = malloc(sizeof(console));
    repositoryInitialSetup(&((*currentConsole)->currentStock));
}


void    consoleGetMedication(console *currentConsole, int index) {
    repositoryGetMedication(currentConsole->currentStock, index);
}


void    consoleGetAllMedications(console *currentConsole) {
    repositoryGetAllMedications(currentConsole->currentStock);
}


void    consoleAddMedication(console *currentConsole, char name[100], int concentration, int  quantity, float price) {
    repositoryAddMedication(currentConsole->currentStock, name, concentration, quantity, price);
}

void    consoleUpdateMedication(console *currentConsole, int index, char name[100], int concentration, int  quantity, float price) {
    repositoryUpdateMedication(currentConsole->currentStock, index, name, concentration, quantity, price);
}


void    consoleDeleteMedication(console *currentConsole, int index) {
    repositoryDeleteMedication(currentConsole->currentStock, index);
}


void    consoleSearchMedication(console *currentConsole, char subString[100]) {
    repositorySearchMedications(currentConsole->currentStock, subString);
}

void    consoleSearchMedicationSorted(console *currentConsole, char subString[100]) {
    repositorySearchMedicationsSorted(currentConsole->currentStock, subString);
}