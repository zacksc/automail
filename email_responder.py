from huggingface_hub import InferenceClient

class EmailResponder:
    def __init__(self, api_token):
        self.client = InferenceClient(
            provider="together",
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            api_key=api_token
        )

    def gerar_resposta(self, conteudo_email, categoria):
        if categoria == "produtivo":
            prompt = f"O seguinte email é produtivo e requer ação. Gere uma resposta educada e profissional: {conteudo_email}"
        else:
            prompt = f"O seguinte email é improdutivo (apenas felicitações ou agradecimentos) e não requer ação. Gere uma resposta cordial e neutra: {conteudo_email}"

        messages = [
            {
                "role": "system",
                "content": (
                    "Você é um assistente de respostas de e-mail que deve sempre responder em "
                    "português brasileiro, nunca utilize outro idioma e não traduza para inglês. "
                    "Responda de forma clara, cordial e objetiva, sem usar saudações formais como 'Estimado' ou 'Prezado'"
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]

        try:
            response = self.client.chat.completions.create(
                messages=messages,
                max_tokens=256,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            print("EXCEÇÃO:", e)
            return "Erro ao processar a resposta da IA."
