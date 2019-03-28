#include <string.h>
#include <assert.h>
#include <stdio.h>
#include "ui.h"
#include "repository.h"
#include "test.h"

void populate(Ui *currentUi) {
    controllerAddMedication(currentUi->currentController, "algocalmin", 12, 13, 19);
    controllerAddMedication(currentUi->currentController, "algoceva", 12, 13523, 1);
    controllerAddMedication(currentUi->currentController, "algoaltceva", 12, 134, 12);
    controllerAddMedication(currentUi->currentController, "strepsil c", 12, 131, 76);
    controllerAddMedication(currentUi->currentController, "strepsil b", 12, 243, 22);
    controllerAddMedication(currentUi->currentController, "strepsil a", 14, 54, 42);
    controllerAddMedication(currentUi->currentController, "panadol", 13, 333, 11);
    controllerAddMedication(currentUi->currentController, "restantsonium", 12, 22, 123);
    controllerAddMedication(currentUi->currentController, "algebra", 12, 111, 10);
    controllerAddMedication(currentUi->currentController, "medicament", 12, 1, 1223);
    controllerAddMedication(currentUi->currentController, "medicament lol", 12, 0, 13);
}

void testRepositoryAdd() {
    printf("\t\tTesting repository add functionality...\n");
    Stock *testStock;
    repositoryInitialSetup(&testStock);
    repositoryAddMedication(testStock, "test name", 1, 2, 3.0);
    assert(testStock->length == 1);
    assert(testStock->medications[0].concentration == 1);
    assert(testStock->medications[0].quantity == 2);
    assert(testStock->medications[0].price == 3.0);
    assert(strcmp(testStock->medications[0].name, "test name") == 0);
    printf("\t\tAdd functionality tests are OK!\n\n");
}

void testRepositoryDelete() {
    printf("\t\tTesting repository delete functionality...\n");
    Stock *testStock;
    repositoryInitialSetup(&testStock);
    repositoryDeleteMedication(testStock, 0);
    assert(testStock->length == -1);
    printf("\t\tDelete functionality tests are OK!\n\n");
}

void testRepositoryUpdate() {
    printf("\t\tTesting repository update functionality...\n");
    Stock *testStock;
    repositoryInitialSetup(&testStock);
    repositoryAddMedication(testStock, "test name", 1, 2, 3.0);
    repositoryUpdateMedication(testStock, 0, "changed name", 4, 5, 6.0);
    assert(testStock->length == 1);
    assert(testStock->medications[0].concentration == 4);
    assert(testStock->medications[0].quantity == 5);
    assert(testStock->medications[0].price == 6.0);
    assert(strcmp(testStock->medications[0].name, "changed name") == 0);
    printf("\t\tUpdate functionality tests are OK!\n\n");
}

void testRepository() {
    printf("\tRunning repository tests...\n\n");
    testRepositoryAdd();
    testRepositoryDelete();
    testRepositoryUpdate();
    printf("\tAll repository tests finished OK!\n\n\n");
}

void testControllerAdd() {
    printf("\t\tTesting controller add functionality...\n");
    Controller *testController;
    controllerInitialSetup(&testController);
    controllerAddMedication(testController, "test name", 1, 2, 3.0);
    assert(testController->currentStock->length == 1);
    assert(testController->currentStock->medications[0].concentration == 1);
    assert(testController->currentStock->medications[0].quantity == 2);
    assert(testController->currentStock->medications[0].price == 3.0);
    assert(strcmp(testController->currentStock->medications[0].name, "test name") == 0);
    printf("\t\tAdd functionality tests are OK!\n\n");
}

void testControllerDelete() {
    printf("\t\tTesting controller delete functionality...\n");
    Controller *testController;
    controllerInitialSetup(&testController);
    controllerDeleteMedication(testController, 0);
    assert(testController->currentStock->length == -1);
    printf("\t\tDelete functionality tests are OK!\n\n");
}

void testControllerUpdate() {
    printf("\t\tTesting repository update functionality...\n");
    Controller *testController;
    controllerInitialSetup(&testController);
    controllerAddMedication(testController, "test name", 1, 2, 3.0);
    controllerUpdateMedication(testController, 0, "changed name", 4, 5, 6.0);
    assert(testController->currentStock->length == 1);
    assert(testController->currentStock->medications[0].concentration == 4);
    assert(testController->currentStock->medications[0].quantity == 5);
    assert(testController->currentStock->medications[0].price == 6.0);
    assert(strcmp(testController->currentStock->medications[0].name, "changed name") == 0);
    printf("\t\tUpdate functionality tests are OK!\n\n");
}

void testController() {
    printf("\tRunning controller tests...\n\n");
    testControllerAdd();
    testControllerDelete();
    testControllerUpdate();
    printf("\tAll controller tests finished OK!\n\n\n");
}

void runTests() {
    printf("Running tests...\n");
    testRepository();
    testController();
    printf("Finished running tests!\n");
}
