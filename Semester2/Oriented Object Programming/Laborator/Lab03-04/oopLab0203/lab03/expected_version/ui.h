#ifndef UI
#define UI

#include <stdio.h>
#include <stdlib.h>

#include "console.h"


typedef struct {
    console     *currentConsole;
} ui;


#include "test.h"


void initialSetup(ui **currentUi);
void     getMedication(ui *currentUi);
void     getAllMedications(ui *currentUi);
void    addMedication(ui *currentUi);
void    updateMedication(ui *currentUi);
void     deleteMedication(ui *currentUi);
void     searchMedication(ui *currentUi);
void    printMenu();
int    getNextOption();
void    runApplication();

#endif