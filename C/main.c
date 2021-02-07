#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

int premierPart1(int n);
int premierPart2(int n);
int premierPart3(int n);
double * tab_execution(int (* premier)(int), int * tab1);
double execution_time(int (* premier)(int), int n);
int writeCSV(int * tab1, double * results_part1, double * results_part2, double * results_part3);


int main(){
    int tab1[12] = {1000003, 2000003, 4000037, 8000009, 16000057, 32000011, 64000031, 128000003, 256000001, 512000009, 1024000009, 2048000011};

    int (* fonctions [3])(int) = {premierPart1 , premierPart2 , premierPart3};

    double *results_part1 = tab_execution(fonctions[0], tab1);
    double *results_part2 = tab_execution(fonctions[1], tab1);
    double *results_part3 = tab_execution(fonctions[2], tab1);

    writeCSV(tab1, results_part1, results_part2, results_part3);

    for(int i=0; i<12; i++){
        printf("%d %.10lf\n", tab1[i] , results_part1[i]);
    }

    for(int i=0; i<12; i++){
        printf("%d %.10lf\n", tab1[i] , results_part2[i]);
    }

    for(int i=0; i<12; i++){
        printf("%d %.10lf\n", tab1[i] , results_part3[i]);
    }

    return 0;
}

//  Fonction  qui  prend en parametre une fonction est un tebleau d'entier n et qui retourne le temps d'execution de chaque n dans un autre tableau
double * tab_execution(int (* premier)(int), int * tab1){

    double *tab2 = malloc(12 * sizeof(double));

    for(int i=0; i<12; i++){
        tab2[i] = execution_time(premier, tab1[i]);
    }

    return tab2;
}

//  Fonction  qui  retourne  le  temps d’execution de la fonction donner en parametre
double execution_time(int (* premier)(int), int n){
    clock_t t1 , t2;

    t1 = clock ();
    premier(n);
    t2 = clock ();

    double temps_exe = (double) (t2 -t1)/CLOCKS_PER_SEC;
    return temps_exe;
}

// la fonctin retourne 1 si n est premier et 0 sinon
int premierPart1(int n) {
    for (int i=2; i<n; i++) {
        if (n % i == 0) {
            printf("%d n'est pas premier\n", n);
            return 0;
        }
    }
    printf("%d est premier\n", n);
    return 1;
}

// la fonctin retourne 1 si n est premier et 0 sinon
int premierPart2(int n) {
    for (int i=2; i<=(n/2); i++) {
        if (n % i == 0) {
            printf("%d n'est pas premier\n", n);
            return 0;
        }
    }
    printf("%d est premier\n", n);
    return 1;
}

// la fonctin retourne 1 si n est premier et 0 sinon
int premierPart3(int n) {
    for (int i=2; i<=sqrt(n); i++) {
        if (n % i == 0) {
            printf("%d n'est pas premier\n", n);
            return 0;
        }
    }
    printf("%d est premier\n", n);
    return 1;
}

int writeCSV(int * tab1, double * results_part1, double * results_part2, double * results_part3){

    FILE* fp = NULL;
    fp=fopen("C_TP2.csv","w+");

    if (fp == NULL){
        return 0;
    }

    fprintf(fp,"nb,T_part1,T_part2,T_part3");
    for(int i=0; i<12; i++){
        fprintf(fp,"\n%d,%.10lf,%.10lf,%.10lf", tab1[i], results_part1[i], results_part2[i], results_part3[i]);
    }
    fclose(fp);

    return 1;
}
