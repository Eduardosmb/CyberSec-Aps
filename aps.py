import socket
import threading
import dearpygui.dearpygui as dpg

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

def escanear_porta(host, porta):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        resultado = sock.connect_ex((host, porta))
        if resultado == 0:
            servico = portas_bem_conhecidas.get(porta, "Serviço Desconhecido")
            dpg.add_text(f"Porta {porta}: Aberta ({servico})", parent="results_group")
        sock.close()
    except socket.error:
        dpg.add_text(f"Não foi possível conectar ao servidor {host}.", parent="results_group")

def iniciar_escanemento(sender, app_data, user_data):
    dpg.delete_item("results_group", children_only=True)  
    
    host = dpg.get_value("host_input")
    try:
        porta_inicio = int(dpg.get_value("start_port_input"))
        porta_fim = int(dpg.get_value("end_port_input"))

        
        if not (1 <= porta_inicio <= 65535 and 1 <= porta_fim <= 65535):
            raise ValueError("As portas devem estar no intervalo de 1 a 65535.")

        
        if porta_inicio > porta_fim:
            raise ValueError("A porta inicial deve ser menor ou igual à porta final.")
            
    except ValueError as e:
        dpg.add_text(f"Erro: {str(e)}", parent="results_group", color=[255, 0, 0])
        return

    def escanear_intervalo():
        threads = []
        for porta in range(porta_inicio, porta_fim + 1):
            thread = threading.Thread(target=escanear_porta, args=(host, porta))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        dpg.add_text("Escaneamento de portas concluído.", parent="results_group", color=[0, 255, 0])

    threading.Thread(target=escanear_intervalo).start()

def main():
    dpg.create_context()

    with dpg.window(label="Scanner de Portas", width=600, height=400):
        dpg.add_text("Insira os dados para escanear as portas de um host.", color=[150, 150, 250])

        dpg.add_input_text(label="Host", tag="host_input", width=300)
        dpg.add_input_text(label="Porta Inicial", tag="start_port_input", width=100)
        dpg.add_input_text(label="Porta Final", tag="end_port_input", width=100)
        
        dpg.add_button(label="Iniciar Escaneamento", callback=iniciar_escanemento)

        dpg.add_separator()
        dpg.add_text("Resultados:", color=[100, 250, 100])
        with dpg.group(tag="results_group"):
            pass  

    dpg.create_viewport(title='Scanner de Portas', width=600, height=400)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    main()
