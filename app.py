import gradio as gr
import requests

N8N_WEBHOOK_URL = "http://localhost:5678/webhook/mensaje"


def responder_chat(mensaje, historial):
    historial = historial or []

    try:
        r = requests.post(
            N8N_WEBHOOK_URL,
            json={"mensaje": mensaje, "sessionId": "sesion_demo_gradio"},
            timeout=15,
        )

        try:
            respuesta = r.json().get("output", r.text)
        except:
            respuesta = r.text

    except Exception as e:
        respuesta = f"Error de conexión: {e}"

    historial.append({"role": "user", "content": mensaje})
    historial.append({"role": "assistant", "content": respuesta})

    return "", historial


with gr.Blocks() as demo:
    gr.Markdown("# 🤖 Chat de Onboarding con Lucía")

    chatbot = gr.Chatbot(label="Conversación", height=500)

    with gr.Row():
        entrada = gr.Textbox(
            placeholder="Escribe tu mensaje...",
            show_label=False,
            scale=8,
        )
        boton = gr.Button("Enviar", variant="primary", scale=2)

    for evento in (entrada.submit, boton.click):
        evento(
            responder_chat,
            [entrada, chatbot],
            [entrada, chatbot],
        )

if __name__ == "__main__":
    demo.launch(theme=gr.Theme.from_hub("d8ahazard/material_design_rd"))
