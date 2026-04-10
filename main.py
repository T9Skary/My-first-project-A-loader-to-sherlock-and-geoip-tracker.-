import requests
import subprocess

def investigar():
    print("\n" + "="*30)
    print("      OPERADOR DE OSINT      ")
    print("="*30)
    print("1. Apenas Username (Sherlock)")
    print("2. Apenas IP (Geo-IP)")
    print("3. Username e IP (Completo)")
    print("0. Sair")
    print("-" * 30)

    opcao = input("[>] Escolha uma opção: ")

    # Definindo o caminho que você me passou
    caminho_sherlock = r"C:\Users\User\AppData\Local\Python\pythoncore-3.14-64\Scripts\sherlock.exe"

    if opcao == '1' or opcao == '3':
        user = input("\n[+] Digite o Username: ")
        print(f"[*] Iniciando Sherlock para: {user}...")
        try:
            # Roda o Sherlock direto da pasta Scripts
            subprocess.run([caminho_sherlock, user, "--timeout", "1"])
        except FileNotFoundError:
            print("[!] Erro: Sherlock não encontrado no caminho especificado.")

    if opcao == '2' or opcao == '3':
        ip_alvo = input("\n[+] Digite o IP: ")
        print(f"[*] Localizando IP: {ip_alvo}...")
        try:
            response = requests.get(f"http://ip-api.com/json/{ip_alvo}").json()
            if response['status'] == 'success':
                print(f"\n[!] RESULTADOS PARA {ip_alvo}:")
                print(f"País: {response['country']} ({response['countryCode']})")
                print(f"Cidade: {response['city']}")
                print(f"Provedor (ISP): {response['isp']}")
                print(f"Coordenadas: {response['lat']}, {response['lon']}")
            else:
                print("[!] IP inválido ou não encontrado.")
        except Exception as e:
            print(f"[!] Falha na conexão: {e}")

    if opcao == '0':
        print("Finalizando operação...")
        exit()

if __name__ == "__main__":
    while True:
        investigar()
        input("\n[Pressione Enter para voltar ao menu]")