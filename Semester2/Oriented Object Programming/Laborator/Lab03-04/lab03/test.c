#include <string.h>
#include "ui.h"
#include "test.h"

void populate(Ui *currentUi){
    controllerAddMedication(currentUi->currentController, "a", 1, 11, 111);
    controllerAddMedication(currentUi->currentController, "b", 2, 22, 222);
    controllerAddMedication(currentUi->currentController, "c", 3, 33, 333);
    controllerAddMedication(currentUi->currentController, "d", 4, 44, 444);
    controllerAddMedication(currentUi->currentController, "e", 5, 55, 555);
    controllerAddMedication(currentUi->currentController, "f", 6, 66, 666);
    controllerAddMedication(currentUi->currentController, "g", 7, 77, 777);
    controllerAddMedication(currentUi->currentController, "h", 8, 88, 888);
    controllerAddMedication(currentUi->currentController, "i", 9, 99, 999);
}
