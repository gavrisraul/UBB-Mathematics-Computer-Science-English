#ifndef REPOSITORY
#define REPOSITORY

#include <string.h>
#include <stdlib.h>
#include "domain.h"
#include "utils.h"

typedef struct {
    Medication medications[100];
    int length;
} Stock;

/*
* Create repository
* in: current stock / medications
* out: repository
*/
void repositoryInitialSetup(Stock **currentStock);

/*
* Get medication in repository by index
* in: currenct stock, index
* out: medication at given index if exists
*/
Medication repositoryGetMedication(Stock *currentStock, int index);

/*
* Get all medications from repository / current stock
* in: current stock
* out: all medications
*/
Stock *repositoryGetAllMedications(Stock *currentStock);

/*
* Add medication to the repository
* in: current stock, medication data
* out: new medication in the stock
*/
int repositoryAddMedication(Stock *currentStock, char name[100], int concentration, int quantity, float price);

/*
* Update medication at given index
* in: current stock, medication data
* out: updated medication at given index
*/
void repositoryUpdateMedication(Stock *currentStock, int index, char name[100], int concentration, int quantity, float price);

/*
* Delete medication from stock
* in: current stock, index
* out: stock without medication at given index
*/
void repositoryDeleteMedication(Stock *currentStock, int index);

/*
* Search for medications by name
* in: stock, name
* out: all medications for given name
*/
Stock repositorySearchMedications(Stock *currentStock, char subString[100]);

/*
* Search medications in sorted stock
* in: stock, name
* out: all medications for given name but sorted
*/
Stock repositorySearchMedicationsSorted(Stock *currentStock, char subString[100]);

/*
* Get medication by a given quantity
* in: stock, quantity
* out: medication
*/
Stock repositoryGetMedicationByQuantity(Stock *currentStock, int quantity);

#endif