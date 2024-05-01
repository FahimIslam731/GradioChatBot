import gradio as gr
import openai

openai_api_key = ""

# Initialize a list to store conversation history.
conversation_history = []

def chat_with_openai(message):
    global conversation_history
    conversation_history.append({"role": "user", "content": message})

    try:
        # Make the API call with the full conversation history.
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=conversation_history,
            api_key=openai_api_key
        )
        # Extract the response and append it to the conversation history.
        answer = response['choices'][0]['message']['content']
        conversation_history.append({"role": "assistant", "content": answer})
    except Exception as e:
        answer = f"Error: {str(e)}"
    return answer


with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()

    def respond(message):
        answer = chat_with_openai(message)
        return "", [(message, answer)]

    msg.submit(respond, inputs=msg, outputs=[msg, chatbot])

demo.launch()
