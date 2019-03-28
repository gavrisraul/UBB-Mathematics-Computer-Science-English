#include <string.h>
#include <stdlib.h>
#include "domain.h"

char *toString(Medication *currentMedication) {
    char *strRepr;
    strRepr = malloc(sizeof(char) * 100);
    strcpy(strRepr, "This medication is called: ");
    strcat(strRepr, currentMedication->name);
    return strRepr;
}

char *getName(Medication currentMedication) {
    char *name;
    name = malloc(sizeof(char) * 100);
    strcpy(name, currentMedication.name);
    return name;
}

int getConcentration(Medication currentMedication) {
    return currentMedication.concentration;
}

int getQuantity(Medication currentMedication) {
    return currentMedication.quantity;
}

float getPrice(Medication currentMedication) {
    return currentMedication.price;
}

Medication *createMedication(char name[], int concentration, int quantity, float price) {
    Medication *newMedication = malloc(sizeof(Medication));
    strcpy(newMedication->name, name);
    newMedication->concentration = concentration;
    newMedication->quantity = quantity;
    newMedication->price = price;
    return newMedication;
}

Medication *copyMedication(Medication currentMedication) {
    return createMedication(
        getName(currentMedication),
        getConcentration(currentMedication),
        getQuantity(currentMedication),
        getPrice(currentMedication));
}

void destroyMedication(Medication *currentMedication) {
    free(currentMedication->name);
}
