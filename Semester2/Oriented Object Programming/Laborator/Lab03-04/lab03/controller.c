#include <stdio.h>
#include <stdlib.h>
#include "ui.h"
#include "repository.h"
#include "controller.h"

void controllerInitialSetup(Controller **currentController) {
    *currentController = malloc(sizeof(Controller));
    repositoryInitialSetup(&((*currentController)->currentStock));
}

Medication controllerGetMedication(Controller *currentController, int index) {
    return repositoryGetMedication(currentController->currentStock, index);
}

Stock *controllerGetAllMedications(Controller *currentController) {
    return repositoryGetAllMedications(currentController->currentStock);
}

int controllerAddMedication(Controller *currentController, char name[100], int concentration, int quantity, float price) {
    return repositoryAddMedication(currentController->currentStock, name, concentration, quantity, price);
}

void controllerUpdateMedication(Controller *currentController, int index, char name[100], int concentration, int quantity, float price) {
    repositoryUpdateMedication(currentController->currentStock, index, name, concentration, quantity, price);
}

void controllerDeleteMedication(Controller *currentController, int index) {
    repositoryDeleteMedication(currentController->currentStock, index);
}

Stock controllerSearchMedication(Controller *currentController, char subString[100]) {
    return repositorySearchMedications(currentController->currentStock, subString);
}

Stock controllerSearchMedicationSorted(Controller *currentController, char subString[100]) {
    return repositorySearchMedicationsSorted(currentController->currentStock, subString);
}

Stock controllerGetMedicationByQuantity(Controller *currentController, int quantity) {
    return repositoryGetMedicationByQuantity(currentController->currentStock, quantity);
}

void controllerUndo(ActionArray *currentActionArray, Controller *currentController) {
    repositoryUndo(currentActionArray, currentController->currentStock);
}

void controllerRedo(ActionArray *currentActionArray, Controller *currentController) {
    repositoryRedo(currentActionArray, currentController->currentStock);
}

void controllerAddUiState(ActionArray *currentActionArray, Controller *currentController) {
    repositoryAddUiState(currentActionArray, currentController->currentStock);
}

void controllerCleanup(Controller *currentController) {
    repositoryCleanup(currentController->currentStock);
}

void controllerCleanupActionArray(ActionArray *currentActionArray) {
    repositoryCleanupActionArray(currentActionArray);
}