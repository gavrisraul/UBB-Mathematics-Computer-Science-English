#pragma once
#include <stdio.h>
#include <stdlib.h>
#include "repository.h"

typedef struct {
  Stock *currentStock;
} Controller;

void controllerInitialSetup(Controller **currentController);

Medication controllerGetMedication(Controller *currentController, int index);

Stock *controllerGetAllMedications(Controller *currentController);

int controllerAddMedication(Controller *currentController, char name[100], int concentration, int quantity, float price);

void controllerUpdateMedication(Controller *currentController, int index, char name[100], int concentration, int quantity, float price);

void controllerDeleteMedication(Controller *currentController, int index);

Stock controllerSearchMedication(Controller *currentController, char subString[100]);

Stock controllerSearchMedicationSorted(Controller *currentController, char subString[100]);

Stock controllerGetMedicationByQuantity(Controller *currentController, int quantity);

void controllerUndo(ActionArray *currentActionArray, Controller *currentController);

void controllerRedo(ActionArray *currentActionArray, Controller *currentController);

void controllerAddUiState(ActionArray *currentActionArray, Controller *currentController);

void controllerCleanup(Controller *currentController);

void controllerCleanupActionArray(ActionArray *currentActionArray);
