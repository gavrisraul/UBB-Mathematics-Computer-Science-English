#include <string.h>

#include "ui.h"
#include "test.h"

int main(int argc, char *argv[]) {
    if (argc == 2 && strcmp(argv[1], "test") == 0)
        runTests();
    else {
        Ui *currentUi;
        initialSetup(&currentUi);
        populate(currentUi);
        runApplication(currentUi);
    }
}
