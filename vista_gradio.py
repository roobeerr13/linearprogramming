import gradio as gr
from recursos.recursos import Recursos
from soldados.soldados import Soldados

# Instancia de gestión
gestor_recursos = Recursos()
gestor_soldados = Soldados()

def agregar_recurso(tipo, cantidad):
    gestor_recursos.agregar_recurso(tipo, int(cantidad))
    return gestor_recursos.obtener_recursos()

def agregar_soldado(tipo, ataque, defensa, cantidad):
    gestor_soldados.reclutar_soldado(tipo, int(ataque), int(defensa), int(cantidad))
    return gestor_soldados.obtener_soldados()

def mostrar_recursos():
    return gestor_recursos.obtener_recursos()

def mostrar_soldados():
    return gestor_soldados.obtener_soldados()

# Construcción de la interfaz
with gr.Blocks() as interfaz:
    gr.Markdown("# 🏰 Gestión de Recursos y Tropas")

    with gr.Row():
        gr.Markdown("## 🔹 Agregar Recursos")
        tipo_recurso = gr.Textbox(label="Tipo de recurso")
        cantidad_recurso = gr.Textbox(label="Cantidad")
        boton_recurso = gr.Button("Agregar")
        salida_recursos = gr.Dataframe(label="Estado actual de los recursos")

    boton_recurso.click(fn=agregar_recurso, inputs=[tipo_recurso, cantidad_recurso], outputs=[salida_recursos])

    with gr.Row():
        gr.Markdown("## ⚔️ Reclutar Soldados")
        tipo_soldado = gr.Textbox(label="Tipo de soldado")
        ataque_soldado = gr.Textbox(label="Ataque")
        defensa_soldado = gr.Textbox(label="Defensa")
        cantidad_soldado = gr.Textbox(label="Cantidad")
        boton_soldado = gr.Button("Reclutar")
        salida_soldados = gr.Dataframe(label="Estado actual de los soldados")

    boton_soldado.click(fn=agregar_soldado, inputs=[tipo_soldado, ataque_soldado, defensa_soldado, cantidad_soldado], outputs=[salida_soldados])

    gr.Markdown("### 📊 Estado de los Recursos y Soldados")
    boton_mostrar_recursos = gr.Button("Actualizar Recursos")
    boton_mostrar_soldados = gr.Button("Actualizar Soldados")

    salida_actual_recursos = gr.Dataframe(label="Recursos")
    salida_actual_soldados = gr.Dataframe(label="Soldados")

    boton_mostrar_recursos.click(fn=mostrar_recursos, inputs=[], outputs=[salida_actual_recursos])
    boton_mostrar_soldados.click(fn=mostrar_soldados, inputs=[], outputs=[salida_actual_soldados])

    interfaz.launch()