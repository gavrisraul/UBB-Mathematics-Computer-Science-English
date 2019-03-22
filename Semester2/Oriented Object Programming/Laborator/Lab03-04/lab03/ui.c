#include <stdio.h>
#include <stdlib.h>
#include "domain.h"
#include "controller.h"
#include "ui.h"
#include "test.h"

void initialSetup(Ui **currentUi) {
    *currentUi = malloc(sizeof(Ui));
    controllerInitialSetup(&((*currentUi)->currentController));
}

void getMedication(Ui *currentUi) {
    int index;

    printf("Enter medication index: ");
    scanf("%d", &index);

    Medication result = controllerGetMedication(currentUi->currentController, index);

    printf("Medication at index %d:\n", index);
    printf("\tname - %s\n", result.name);
    printf("\tconcentration - %d\n", result.concentration);
    printf("\tquantity - %d\n", result.quantity);
    printf("\tprice - %f\n", result.price);
    printf("\n");
}

void getAllMedications(Ui *currentUi) {
    Stock *result = controllerGetAllMedications(currentUi->currentController);

    printf("Printing all stock medication:\n");

    for (int i = 0; i < result->length; i++) {
        printf("\tmedication index - %d\n", i);
        printf("\tname - %s\n", result->medications[i].name);
        printf("\tconcentration - %d\n", result->medications[i].concentration);
        printf("\tquantity - %d\n", result->medications[i].quantity);
        printf("\tprice - %f\n", result->medications[i].price);
        printf("\n");
    }
}

void addMedication(Ui *currentUi) {
    char name[100];
    int concentration;
    int quantity;
    float price;

    printf("Please specify medication features:\n");
    printf("\tname - ");
    scanf("%s", name);
    printf("\tconcentration - ");
    scanf("%d", &concentration);
    printf("\tquantity - ");
    scanf("%d", &quantity);
    printf("\tprice - ");
    scanf("%f", &price);

    int result = controllerAddMedication(currentUi->currentController, name, concentration, quantity, price);

    if (result == 0)
        printf("Adding new medication!\n");
    else
        printf("Updating existing medication %d quantity\n", result);
}

void updateMedication(Ui *currentUi) {
    char name[100];
    int index, concentration, quantity;
    float price;

    printf("Enter medication index: ");
    scanf("%d", &index);
    printf("Please specify medication features:\n");
    printf("\tname - ");
    scanf("%s", name);
    printf("\tconcentration - ");
    scanf("%d", &concentration);
    printf("\tquantity - ");
    scanf("%d", &quantity);
    printf("\tprice - ");
    scanf("%f", &price);

    controllerUpdateMedication(currentUi->currentController, index, name, concentration, quantity, price);
}

void deleteMedication(Ui *currentUi) {
    int index;

    printf("Enter medication index: ");
    scanf("%d", &index);

    controllerDeleteMedication(currentUi->currentController, index);
}

void searchMedication(Ui *currentUi) {
    char subString[100];

    printf("Enter substring to search for: ");
    fgetc(stdin);
    fgets(subString, sizeof(subString), stdin);
    subString[strlen(subString) - 1] = '\0';
    Stock result = controllerSearchMedication(currentUi->currentController, subString);

    printf("\nResults:\n");
    for (int i = 0; i < result.length; i++) {
        printf("\tmedication index - %d\n", i);
        printf("\tname - %s\n", result.medications[i].name);
        printf("\tconcentration - %d\n", result.medications[i].concentration);
        printf("\tquantity - %d\n", result.medications[i].quantity);
        printf("\tprice - %f\n", result.medications[i].price);
        printf("\n");
    }
}

void searchMedicationSorted(Ui *currentUi) {
    char subString[100];

    printf("Enter substring to search for: ");
    fgetc(stdin);
    fgets(subString, sizeof(subString), stdin);
    subString[strlen(subString) - 1] = '\0';
    Stock result = controllerSearchMedicationSorted(currentUi->currentController, subString);

    printf("\nResults:\n");
    for (int i = 0; i < result.length; i++) {
        printf("\tmedication index - %d\n", i);
        printf("\tname - %s\n", result.medications[i].name);
        printf("\tconcentration - %d\n", result.medications[i].concentration);
        printf("\tquantity - %d\n", result.medications[i].quantity);
        printf("\tprice - %f\n", result.medications[i].price);
        printf("\n");
    }
}

void getMedicationByQuantity(Ui *currentUi) {
    int quantity;

    printf("Enter limit quantity: ");
    scanf("%d", &quantity);

    Stock result = controllerGetMedicationByQuantity(currentUi->currentController, quantity);

    printf("\nResults:\n");
    for (int i = 0; i < result.length; i++) {
        printf("\tmedication index - %d\n", i);
        printf("\tname - %s\n", result.medications[i].name);
        printf("\tconcentration - %d\n", result.medications[i].concentration);
        printf("\tquantity - %d\n", result.medications[i].quantity);
        printf("\tprice - %f\n", result.medications[i].price);
        printf("\n");
    }
}

void printMenu() {
    printf("\nAvailable options:\n");
    printf("\t0 - close the application\n");
    printf("\t1 - get medication from stock\n");
    printf("\t2 - get all medications from stock\n");
    printf("\t3 - add new medication from stock\n");
    printf("\t4 - update an existing medication from stock\n");
    printf("\t5 - delete medication from stock\n");
    printf("\t6 - search for medication from stock\n");
    printf("\t7 - search for medication from stock and sort by concentration\n");
    printf("\t8 - get medication from stock with atleast a given quantity left\n");
}

int getNextOption() {
    int option;

    printMenu();

    printf("Enter your option: ");
    scanf("%d", &option);

    while (option < 0 || option > 8) {
        printf("\nInvalid option!\n");
        printMenu();
        printf("\nChoose a valid option: ");
        scanf("%d", &option);
    }

    return option;
}

void runApplication() {
    Ui *currentUi;
    int currentOption;

    initialSetup(&currentUi);
    populate(currentUi);

    currentOption = getNextOption();
    while (currentOption != 0) {
        switch (currentOption) {
        case 1:
            getMedication(currentUi);
            break;
        case 2:
            getAllMedications(currentUi);
            break;
        case 3:
            addMedication(currentUi);
            break;
        case 4:
            updateMedication(currentUi);
            break;
        case 5:
            deleteMedication(currentUi);
            break;
        case 6:
            searchMedication(currentUi);
            break;
        case 7:
            searchMedicationSorted(currentUi);
            break;
        case 8:
            getMedicationByQuantity(currentUi);
            break;
        }
        currentOption = getNextOption();
    }
}
