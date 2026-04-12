#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void menu() {
    printf("\n==============================");
    printf("\n      OSINT OPERATOR (C)      ");
    printf("\n==============================");
    printf("\n1. Only Username (Sherlock)");
    printf("\n2. Only IP (Geo-IP)");
    printf("\n3. Username and IP (Full)");
    printf("\n0. Exit");
    printf("\n------------------------------");
    printf("\n[>] Choice: ");
}

int main() {
    int opcao;
    char alvo[100];
    char comando[500];

    while(1) {
        menu();
        scanf("%d", &opcao);

        if (opcao == 0) break;

        if (opcao == 1 || opcao == 3) {
            printf("\n[+] Digite o Username: ");
            scanf("%s", alvo);
            printf("[*] Chamando Sherlock para: %s...\n", alvo);
            
            // Montando o comando: sherlock username
            sprintf(comando, "sherlock %s --timeout 1", alvo);
            system(comando);
        }

        if (opcao == 2 || opcao == 3) {
            printf("\n[+] Digite o IP: ");
            scanf("%s", alvo);
            printf("[*] Localizando IP: %s...\n", alvo);

            // No C, nao temos 'requests'. Usamos o 'curl' que ja vem no Windows 10/11
            sprintf(comando, "curl -s http://ip-api.com/json/%s", alvo);
            
            printf("\n[!] RESULTADO DA API:\n");
            system(comando);
            printf("\n");
        }

        printf("\n[Pressione Enter para continuar]");
        getchar(); // Limpa o buffer
        getchar(); // Espera o Enter
    }

    return 0;
}
