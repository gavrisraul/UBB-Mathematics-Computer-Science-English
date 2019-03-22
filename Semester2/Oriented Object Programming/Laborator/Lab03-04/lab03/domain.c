#include <string.h>
#include <stdlib.h>
#include "domain.h"

char *toString(Medication *currentMedication) {
    char strRepr[100];

    strcpy(strRepr, "This medication is called: ");
    strcat(strRepr, currentMedication->name);

    return strRepr;
}

char *getName(Medication *currentMedication) {
    return currentMedication->name;
}

int getConcentration(Medication *currentMedication) {
    return currentMedication->concentration;
}

int getQuantity(Medication *currentMedication) {
    return currentMedication->quantity;
}

int getPrice(Medication *currentMedication) {
    return currentMedication->price;
}

Medication *createMedication(char name[], int concentration, int quantity, float price) {
    Medication *newMedication = malloc(sizeof(Medication));

    strcpy(newMedication->name, name);
    newMedication->concentration = concentration;
    newMedication->quantity = quantity;
    newMedication->price = price;

    return newMedication;
}

void destroyMedication(Medication *currentMedication) {
    free(currentMedication->name);
    free(currentMedication);
}