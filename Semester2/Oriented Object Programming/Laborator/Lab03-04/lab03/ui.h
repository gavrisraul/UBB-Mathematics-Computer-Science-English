#pragma once
#include <stdio.h>
#include <stdlib.h>
#include "controller.h"

typedef struct {
    Controller *currentController;
} Ui;

#include "test.h"

void initialSetup(Ui **currentUi);

void getMedication(Ui *currentUi);

void getAllMedications(Ui *currentUi);

void addMedication(Ui *currentUi);

void updateMedication(Ui *currentUi);

void deleteMedication(Ui *currentUi);

void searchMedication(Ui *currentUi);

void getMedicationByQuantity(Ui *currentUi);

void printMenu();

int getNextOption();

void undo(ActionArray *currentActionArray, Ui *currentUi);

void redo(ActionArray *currentActionArray, Ui *currentUi);

void addUiState(ActionArray *currentActionArray, Ui *currentUi);

void runApplication(Ui *currentUi);

void cleanupUi(Ui *currentUi);

void cleanupActionArray(ActionArray *currentActionArray);

