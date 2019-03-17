#ifndef REPOSITORY
#define REPOSITORY

#include <string.h>
#include <stdlib.h>

#include "domain.h"
#include "utils.h"


typedef struct {
    medication     medications[100];
    int            length;
}    stock;


void    repositoryInitialSetup(stock **currentStock);

void    repositoryGetMedication(stock *currentStock, int index);

void    repositoryGetAllMedications(stock *currentStock);

void     repositoryAddMedication(stock *currentStock, char name[100], int concentration, int quantity, float price);

void     repositoryUpdateMedication(stock *currentStock, int index, char name[100], int concentration, int quantity, float price);

void    repositoryDeleteMedication(stock *currentStock, int index);

void    repositorySearchMedications(stock *currentStock, char    subString[100]);

void    repositorySearchMedicationsSorted(stock *currentStock, char    subString[100]);

#endif