#ifndef CONTROLLER
#define CONTROLLER

#include <stdio.h>
#include <stdlib.h>
#include "repository.h"
#include "controller.h"

typedef struct{
    Stock *currentStock;
} Controller;

/*
* Creates the controller
* in: data for controller
* out: pointer to allocated memory for the controller
*/
void controllerInitialSetup(Controller **currentController);

/*
* Get medication from controller at given index
* in: controller, index
* out: medication
*/
Medication controllerGetMedication(Controller *currentController, int index);

/*
* Creates a controller to hold the stock
* in: controller
* out: stock
*/
Stock *controllerGetAllMedications(Controller *currentController);

/*
* Add new medication to the controller
* in: controller, data for medication
* out: new medication to controller
*/
int controllerAddMedication(Controller *currentController, char name[100], int concentration, int quantity, float price);

/*
* Update medication at given index in the controller
* in: controller, data for medication, index
* out: updated medication
*/
void controllerUpdateMedication(Controller *currentController, int index, char name[100], int concentration, int quantity, float price);

/*
* Delete medication from controller
* in: controller, index
* out: controller with freed memory from chosen medication
*/
void controllerDeleteMedication(Controller *currentController, int index);

/*
* Search for medication in the controller
* in: controller, string of medication
* out: medication
*/
Stock controllerSearchMedication(Controller *currentController, char subString[100]);

/*
* Search for medication in sorted controller
* in: controller, string of medication
* out: medication
*/
Stock controllerSearchMedicationSorted(Controller *currentController, char subString[100]);

/*
* Get medication by a given quantity
* in: controller, quantity
* out: medication with the given quantity if exists
*/
Stock controllerGetMedicationByQuantity(Controller *currentController, int quantity);

#endif