#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include "repository.h"
#include "domain.h"
#include "utils.h"

void repositoryInitialSetup(Stock **currentStock) {
    *currentStock = malloc(sizeof(Stock));
    (*currentStock)->length = 0;
}

Medication repositoryGetMedication(Stock *currentStock, int index) {
    return currentStock->medications[index];
}

Stock *repositoryGetAllMedications(Stock *currentStock) {
    return currentStock;
}

int repositoryAddMedication(Stock *currentStock, char name[100], int concentration, int quantity, float price) {
    int index = -1;
    for (int i = 0; i < currentStock->length; i++)
        if ((getConcentration(currentStock->medications[i]) == concentration && strcmp(getName(currentStock->medications[i]), name) == 0)) {
            index = i;
            break;
        }
    if (index == -1) {
        Medication newMedication;
        strcpy(newMedication.name, name);
        newMedication.concentration = concentration;
        newMedication.quantity = quantity;
        newMedication.price = price;
        currentStock->medications[currentStock->length++] = newMedication;
        return -1;
    }
    else {
        currentStock->medications[index].quantity = quantity;
        return index;
    }
}

void repositoryUpdateMedication(Stock *currentStock, int index, char name[100], int concentration, int quantity, float price) {
    strcpy(currentStock->medications[index].name, name);
    currentStock->medications[index].concentration = concentration;
    currentStock->medications[index].quantity = quantity;
    currentStock->medications[index].price = price;
}

void repositoryDeleteMedication(Stock *currentStock, int index) {
    while (index < currentStock->length) {
        currentStock->medications[index] = currentStock->medications[index + 1];
        index++;
    }
    currentStock->length--;
}

Stock repositorySearchMedications(Stock *currentStock, char subString[100]) {
    Medication tmpMedication, medicationResults[100];
    int index = 0;
    for (int i = 0; i < currentStock->length; i++)
        if (strIsContained(getName(currentStock->medications[i]), subString) == 1)
            medicationResults[index++] = currentStock->medications[i];
    for (int i = 0; i < index; i++)
        for (int j = 0; j < index - i - 1; j++) {
            if (strcmp(getName(medicationResults[j]), getName(medicationResults[j + 1])) > 0) {
                tmpMedication = medicationResults[j];
                medicationResults[j] = medicationResults[j + 1];
                medicationResults[j + 1] = tmpMedication;
            }
        }
    Stock resultStock;
    for (int i = 0; i < index; i++)
        resultStock.medications[i] = medicationResults[i];
    resultStock.length = index;
    return resultStock;
}

Stock repositorySearchMedicationsSorted(Stock *currentStock, char subString[100]) {
    Medication tmpMedication, medicationResults[100];
    int index = 0;
    for (int i = 0; i < currentStock->length; i++)
        if (strIsContained(getName(currentStock->medications[i]), subString) == 1)
            medicationResults[index++] = currentStock->medications[i];
    for (int i = 0; i < index; i++)
        for (int j = 0; j < index - i - 1; j++)
            if (getConcentration(medicationResults[j]) < getConcentration(medicationResults[j + 1])) {
                tmpMedication = medicationResults[j];
                medicationResults[j] = medicationResults[j + 1];
                medicationResults[j + 1] = tmpMedication;
            }
    Stock resultStock;
    for (int i = 0; i < index; i++)
        resultStock.medications[i] = medicationResults[i];
    resultStock.length = index;
    return resultStock;
}

Stock repositoryGetMedicationByQuantity(Stock *currentStock, int quantity) {
    Medication medicationResults[100];
    int index = 0;
    for (int i = 0; i < currentStock->length; i++)
        if (currentStock->medications[i].quantity > quantity)
            medicationResults[index++] = currentStock->medications[i];
    Stock resultStock;
    for (int i = 0; i < index; i++)
        resultStock.medications[i] = medicationResults[i];
    resultStock.length = index;
    return resultStock;
}

void repositoryUndo(ActionArray *currentActionArray, Stock *currentStock) {
    if (currentActionArray->currentIndex <= 0) {
        printf("You cannot undo any further!");
        return;
    }
    currentActionArray->currentIndex--;
    copyStockData(currentStock, currentActionArray->stockArray[currentActionArray->currentIndex]);
}

void repositoryRedo(ActionArray *currentActionArray, Stock *currentStock) {
    if (currentActionArray->currentIndex == currentActionArray->maxRedoIndex) {
        printf("You cannot redo any further!");
        return;
    }
    currentActionArray->currentIndex++;
    copyStockData(currentStock, currentActionArray->stockArray[currentActionArray->currentIndex]);
}

void copyStockData(Stock *toStock, Stock *fromStock) {
    toStock->length = fromStock->length;
    for (int i = 0; i < toStock->length; i++)
        toStock->medications[i] = fromStock->medications[i];
}

void repositoryAddUiState(ActionArray *currentActionArray, Stock *currentStock) {
    Stock *newStock;
    repositoryInitialSetup(&newStock);
    copyStockData(newStock, currentStock);
    currentActionArray->currentIndex++;
    currentActionArray->maxRedoIndex = currentActionArray->currentIndex;
    currentActionArray->stockArray[currentActionArray->currentIndex] = newStock;
}

void repositoryCleanup(Stock *currentStock) {
    destroyMedication(currentStock->medications);
}

void repositoryCleanupActionArray(ActionArray *currentActionArray) {
    for (int i = 0; i < currentActionArray->maxRedoIndex; i++)
        repositoryCleanup(currentActionArray->stockArray[i]);
    free(currentActionArray->stockArray);
}