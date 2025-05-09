import customtkinter as ctk
import speedtest
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Função para converter bytes em megabytes
def bytes_para_mb(bytes):
    return bytes / (1024 * 1024)

def testar_velocidade():
    def executar_teste():
        status_label.configure(text="Testando...")
        progresso.start()
        try:
            teste = speedtest.Speedtest()
            download = bytes_para_mb(teste.download())
            upload = bytes_para_mb(teste.upload())
            ping = teste.results.ping

            download_label.configure(text=f"{download:.2f} MB")
            upload_label.configure(text=f"{upload:.2f} MB")
            ping_label.configure(text=f"{ping:.2f} ms")
            status_label.configure(text="Teste concluído.")
        except:
            status_label.configure(text="Erro ao testar.")
        progresso.stop()

    threading.Thread(target=executar_teste, daemon=True).start()

# Interface
janela = ctk.CTk()
janela.title("Testador de Conexão")
janela.geometry("400x350")

ctk.CTkLabel(janela, text="Velocidade de Download:", text_color="lime").pack(pady=(10, 0))
download_label = ctk.CTkLabel(janela, text="", text_color="lime")
download_label.pack()

ctk.CTkLabel(janela, text="Velocidade de Upload:", text_color="lime").pack(pady=(10, 0))
upload_label = ctk.CTkLabel(janela, text="", text_color="lime")
upload_label.pack()

ctk.CTkLabel(janela, text="Ping:", text_color="lime").pack(pady=(10, 0))
ping_label = ctk.CTkLabel(janela, text="", text_color="lime")
ping_label.pack()

progresso = ctk.CTkProgressBar(janela, width=200)
progresso.pack(pady=15)
progresso.set(0)

status_label = ctk.CTkLabel(janela, text="", text_color="white")
status_label.pack()

# Botão moderno com efeito hover
botao = ctk.CTkButton(janela, text="Iniciar Teste", text_color="black", fg_color="lime",
                      hover_color="#00aa00", corner_radius=20, command=testar_velocidade)
botao.pack(pady=15)

janela.mainloop()