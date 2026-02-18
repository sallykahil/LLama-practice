import gradio as gr
import openai 
client = openai.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="nokeyneeded"
)
def chat_with_model(history, new_message):
    messages = [{"role" : "system" , "content" : "You are a helpful assistant."}]
    for user_message, assistant_response in history:
        messages.append({"role" : "user" , "content" : user_message})
        messages.append({"role" : "assistant" , "content" : assistant_response})
    
    messages.append({"role" : "user" , "content" : new_message})
    
    response =client.chat.completions.create(
        model="phi:latest", 
        temperature=0.3,
        messages = messages
        )

    assistant_message = response.choices[0].message.content
    history.append((new_message,assistant_message))
    return history , ""
def gradio_chat():
    with gr.Blocks() as app:
            gr.Markdown("##ollama phi model chat demo")
            gr.Markdown("## Chat with Ollama")
            chatbot=gr.Chatbot(label="Ollama chatbot")

            user_input = gr.Textbox(label="Your Message",placeholder="Type your message here...",lines=1)
            submit_button = gr.Button("Send")
            output = gr.Markdown()
            submit_button.click(fn=gradio_chat, inputs=user_input, outputs=output)
            def clear_chat():
                chatbot.clear()
                output.update("")
            clear_button = gr.Button("Clear Chat")
            submit_button.click(
            fn=chat_with_model, 
            inputs = [chatbot, user_input],
            outputs = [chatbot, user_input]
            )
            clear_button.click(
            fn=clear_chat,
            inputs = [],
            outputs = [chatbot, user_input]
          )
        
    return app


if __name__ == "__main__":
    app = gradio_chat()
    app.launch()