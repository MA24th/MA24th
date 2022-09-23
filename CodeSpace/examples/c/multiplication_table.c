#include <stdio.h>

// Multiplication Table
// Mustafa Asaad
// SEP 28, 2018

int main() {
    int i, j; // Tracker vars
    
    int table = 10; // Number of tables
    int max = 10; // Item per table
    
    // Outter loop for tables
    for (i = 1; i <= table; i++) {
        // Inner loop for items
        for (j=0; j <= max; j++) {
            // Print iteam muti
            printf("%d x %d = %d\n", i, j, i*j);
        }
        // Blank line between tables 
        puts("\n");
    }
    
    return 0;
}
