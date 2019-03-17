#include <string.h>

#include "ui.h"
#include "test.h"


void    populate(ui *currentUi) {
    consoleAddMedication(
        currentUi->currentConsole,
        "algocalmin",
        12,
        13,
        19
    );
    consoleAddMedication(
        currentUi->currentConsole,
        "algoceva",
        12,
        13523,
        1
    );
    consoleAddMedication(
        currentUi->currentConsole,
        "algoaltceva",
        12,
        134,
        12
    );
    consoleAddMedication(
        currentUi->currentConsole,
        "strepsil c",
        12,
        131,
        76
    );
    consoleAddMedication(
        currentUi->currentConsole,
        "strepsil b",
        12,
        243,
        22
    );
    consoleAddMedication(
        currentUi->currentConsole,
        "strepsil a",
        14,
        54,
        42
    );
    consoleAddMedication(
        currentUi->currentConsole,
        "panadol",
        13,
        333,
        11
    );
    consoleAddMedication(
        currentUi->currentConsole,
        "restantsonium",
        12,
        22,
        123
    );
    consoleAddMedication(
        currentUi->currentConsole,
        "algebra",
        12,
        111,
        10
    );
    consoleAddMedication(
        currentUi->currentConsole,
        "medicament",
        12,
        1,
        1223
    );
    consoleAddMedication(
        currentUi->currentConsole,
        "medicament lol",
        12,
        0,
        13
    );
}
