#ifndef UI
#define UI

#include <stdio.h>
#include <stdlib.h>
#include "controller.h"
#include "test.h"

typedef struct {
    Controller *currentController;
} Ui;

/*
* Creates the ui
* in: controller for ui
* out: ui
*/
void initialSetup(Ui **currentUi);

/*
* Get medication from controller/ui
* in: ui / inputs
* out: medication
*/
void getMedication(Ui *currentUi);

/*
* Get all medications from controller / ui
* in: ui / inputs
* out: all medications
*/
void getAllMedications(Ui *currentUi);

/*
* Add medication to controller / ui
* in: ui / inputs
* out: new medications
*/
void addMedication(Ui *currentUi);

/*
* Update a given medication to controller / ui
* in: ui / inputs
* out: updated medication
*/
void updateMedication(Ui *currentUi);

/*
* Delete medication from controller / ui
* in: ui / inputs
* out: controller without the given medication
*/
void deleteMedication(Ui *currentUi);

/*
* Search for a given medication into controller / ui
* in: ui / inputs
* out: searched medication if exists
*/
void searchMedication(Ui *currentUi);

/*
* Get medication by quantity from controller / ui
* in: ui / inputs
* out: searched medication if exists
*/
void getMedicationByQuantity(Ui *currentUi);

/*
* Prints the menu with the choices
*/
void printMenu();

/*
* Gets the next option
*/
int getNextOption();

/*
* Runs the application
*/
void runApplication();

#endif