import socket
import threading
import tkinter as tk
from tkinter import messagebox, scrolledtext



portas_bem_conhecidas = {
    20: "Transferência de Dados FTP",
    21: "Controle de Comando FTP",
    22: "Protocolo de Login Remoto SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    993: "IMAPS",
    995: "POP3S",
    135: "RPC",
    139: "NetBIOS",
    1433: "MSSQL",
    3306: "MySQL",
    3389: "RDP",
    8080: "Proxy HTTP",
    8443: "HTTPS Alt"
}


def escanear_porta(host, porta, area_texto):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        resultado = sock.connect_ex((host, porta))
        if resultado == 0:
            servico = portas_bem_conhecidas.get(porta, "Serviço Desconhecido")
            area_texto.insert(tk.END, f"Porta {porta}: Aberta ({servico})\n")
        sock.close()
    except socket.error:
        area_texto.insert(tk.END, f"Não foi possível conectar ao servidor {host}.\n")


def iniciar_escanemento(host_entrada, porta_inicio_entrada, porta_fim_entrada, area_texto):
    area_texto.delete(1.0, tk.END)  

    
    try:
        host = host_entrada.get()
        porta_inicio = int(porta_inicio_entrada.get())
        porta_fim = int(porta_fim_entrada.get())
    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor, insira números de porta válidos.")
        return

    def escanear_intervalo():
        threads = []
        for porta in range(porta_inicio, porta_fim + 1):
            thread = threading.Thread(target=escanear_porta, args=(host, porta, area_texto))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        messagebox.showinfo("Escaneamento Concluído", "Escaneamento de portas concluído.")

    threading.Thread(target=escanear_intervalo).start()


def iniciar_interface_grafica():
    root = tk.Tk()
    root.title("Scanner de Portas")

    tk.Label(root, text="Host:").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(root, text="Porta Inicial:").grid(row=1, column=0, padx=5, pady=5)
    tk.Label(root, text="Porta Final:").grid(row=2, column=0, padx=5, pady=5)

    host_entrada = tk.Entry(root, width=30)
    host_entrada.grid(row=0, column=1, padx=5, pady=5)

    porta_inicio_entrada = tk.Entry(root, width=10)
    porta_inicio_entrada.grid(row=1, column=1, padx=5, pady=5)

    porta_fim_entrada = tk.Entry(root, width=10)
    porta_fim_entrada.grid(row=2, column=1, padx=5, pady=5)

    area_texto = scrolledtext.ScrolledText(root, width=60, height=20)
    area_texto.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    botao_escanear = tk.Button(root, text="Iniciar Escaneamento", 
                               command=lambda: iniciar_escanemento(host_entrada, porta_inicio_entrada, porta_fim_entrada, area_texto))
    botao_escanear.grid(row=4, column=0, columnspan=2, pady=5)

    root.mainloop()


if __name__ == "__main__":
    iniciar_interface_grafica()
