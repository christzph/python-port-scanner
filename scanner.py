import socket
import sys
from datetime import datetime

def main():
    print("=" * 60)
    print(" PYTHON PORT SCANNER V1.0 - AUDITORIA DE REDES")
    print("=" * 60)

    if len(sys.argv) < 2:
        print("\n[!] Uso: python3 scanner.py <HOST/IP> [PORTA_INICIAL-PORTA_FINAL]")
        print("[!] Exemplo: python3 scanner.py 127.0.0.1 20-80\n")
        target_host = input("[?] Digite o Host ou IP alvo: ").strip()
    else:
        target_host = sys.argv[1]

    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print(f"\n[!] Erro: Não foi possível resolver o hostname '{target_host}'.")
        sys.exit(1)

    start_port = 1
    end_port = 1024

    if len(sys.argv) >= 3 and "-" in sys.argv[2]:
        ports = sys.argv[2].split("-")
        start_port = int(ports[0])
        end_port = int(ports[1])

    print(f"\n[*] Alvo: {target_host} ({target_ip})")
    print(f"[*] Portas: {start_port} até {end_port}")
    print(f"[*] Início: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)

if __name__ == "__main__":
    main()