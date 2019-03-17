#include <stdio.h>
#include <stdlib.h>

#include "console.h"
#include "ui.h"
#include "test.h"


void initialSetup(ui **currentUi) {
    *currentUi = malloc(sizeof(ui));
    consoleInitialSetup(&((*currentUi)->currentConsole));
}


void     getMedication(ui *currentUi) {
    int     index;

    printf("Enter medication index: ");
    scanf("%d", &index);

    consoleGetMedication(currentUi->currentConsole, index);
}

void     getAllMedications(ui *currentUi) {
    consoleGetAllMedications(currentUi->currentConsole);
}


void    addMedication(ui *currentUi) {
    char     name[100];
    int      concentration;
    int      quantity;
    float    price;

    printf("Please specify medication features:\n");
    printf("\tname - ");
    scanf("%s", name);
    printf("\tconcentration - ");
    scanf("%d", &concentration);
    printf("\tquantity - ");
    scanf("%d", &quantity);
    printf("\tprice - ");
    scanf("%f", &price);

    consoleAddMedication(currentUi->currentConsole, name, concentration, quantity, price);
}


void    updateMedication(ui *currentUi) {
    char     name[100];
    int      index, concentration, quantity;
    float    price;

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

    consoleUpdateMedication(currentUi->currentConsole, index, name, concentration, quantity, price);
}


void     deleteMedication(ui *currentUi) {
    int     index;

    printf("Enter medication index: ");
    scanf("%d", &index);

    consoleDeleteMedication(currentUi->currentConsole, index);
}


void     searchMedication(ui *currentUi) {
    char     subString[100];

    printf("Enter substring to search for: ");
    fgetc(stdin);
    fgets(subString, sizeof(subString), stdin);
    subString[strlen(subString) - 1] = '\0';
    consoleSearchMedication(currentUi->currentConsole, subString);
}

void     searchMedicationSorted(ui *currentUi) {
    char     subString[100];

    printf("Enter substring to search for: ");
    fgetc(stdin);
    fgets(subString, sizeof(subString), stdin);
    subString[strlen(subString) - 1] = '\0';
    consoleSearchMedicationSorted(currentUi->currentConsole, subString);
}

void    printMenu() {
    printf("\nAvailable options:\n");
    printf("\t0 - close the application\n");
    printf("\t1 - get medication from stock\n");
    printf("\t2 - get all medications from stock\n");
    printf("\t3 - add new medication from stock\n");
    printf("\t4 - update an existing medication from stock\n");
    printf("\t5 - delete medication from stock\n");
    printf("\t6 - search for medication from stock\n");
    printf("\t7 - search for medication from stock and sort by concentration\n");
}


int    getNextOption() {
    int    option;

    printMenu();

    printf("Enter your option: ");
    scanf("%d", &option);

    while (option < 0 || option > 7) {
        printf("\nInvalid option!\n");
        printMenu();
        printf("\nChoose a valid option: ");
        scanf("%d", &option);
    }

    return option;
}

void    runApplication() {
    ui          *currentUi;
    int         currentOption;

    initialSetup(&currentUi);
    populate(currentUi);

    currentOption = getNextOption();
    while (currentOption != 0) {
        if (currentOption == 1)
            getMedication(currentUi);
        if (currentOption == 2)
            getAllMedications(currentUi);
        else if (currentOption == 3)
            addMedication(currentUi);
        else if (currentOption == 4)
            updateMedication(currentUi);
        else if (currentOption == 5)
            deleteMedication(currentUi);
        else if (currentOption == 6)
            searchMedication(currentUi);
        else if (currentOption == 7)
            searchMedicationSorted(currentUi);
        currentOption = getNextOption();
    }
}
