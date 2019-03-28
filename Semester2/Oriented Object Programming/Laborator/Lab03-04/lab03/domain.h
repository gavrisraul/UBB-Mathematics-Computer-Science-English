#pragma once

typedef struct {
    char name[100];
    int concentration;
    int quantity;
    float price;
} Medication;

/*
 * Get string representation of medication
 * in: medication
 * out: string representation of medication
 */
char *toString(Medication *currentMedication);

/*
 * Get medication name
 * in: medication
 * out: medication's name
 */
char *getName(Medication currentMedication);

/*
 * Get medication concentration
 * in: medication
 * out: medication concentration
 */
int getConcentration(Medication currentMedication);

/*
 * Get string representation of medication
 * in: medication
 * out: medication quantity
 */
int getQuantity(Medication currentMedication);

/*
 * Get medication price
 * in: medication
 * out: medication's price
 */
float getPrice(Medication currentMedication);

/*
 * Create a new medication
 * in:
 * out: pointer to allocated memory for the new medication
 */
Medication *createMedication(char name[], int concentration, int quantity, float price);

/*
 * Create a copy of a medication
 * in: medication
 * out:
 */
Medication *copyMedication(Medication currentMedication);

/*
 * Dealocate medication memory
 * in: medication
 * out:
 */
void destroyMedication(Medication *currentMedication);

