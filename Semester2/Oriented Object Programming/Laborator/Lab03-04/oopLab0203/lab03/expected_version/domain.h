#ifndef DOMAIN
#define DOMAIN

typedef struct {
    char     name[100];
    int      concentration;
    int      quantity;
    float    price;
} medication;

/*
Get string representation of medication
in: medication
out: string representation of medication
*/
char     *toString(medication *currentMedication);

/*
Get medication name
in: medication
out: medication's name
*/
char     *getName(medication *currentMedication);


/*
Get medication concentration
in: medication
out: medication concentration
*/
int     getConcentration(medication *currentMedication);


/*
Get string representation of medication
in: medication
out: medication quantity
*/
int     getQuantity(medication *currentMedication);


/*
Get medication price
in: medication
out: medication's price
*/
int     getPrice(medication *currentMedication);

/*
Create a new medication
in:
out: pointer to allocated memory for the new medication
*/
medication *createMedication();

/*
Dealocate medication memory
in: medication
out:
*/
void    destroyMedication(medication *currentMedication);

#endif