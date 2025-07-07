from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from preprocessar import preprocessar_texto

class EmailClassifier:
    def __init__(self):
        # Exemplos de treino para cada categoria
        treinos_produtivos = [
            "Preciso atualizar o boleto do pagamento",
            "Qual status da minha solicitação?",
            "Solicito suporte no sistema",
            "Quero saber a previsão do meu chamado",
            "Erro no sistema de faturamento",
            "Preciso de ajuda com o cadastro",
            "Estou com problemas na fatura do cartão",
            "Gostaria de informações sobre minha conta",
            "Poderiam me encaminhar o contrato novamente?",
            "Estou aguardando retorno do suporte técnico"
        ]
        treinos_improdutivos = [
            "Olá, tudo bem? Feliz natal!",
            "Muito obrigado pelo atendimento",
            "Parabéns pela equipe maravilhosa!",
            "Feliz ano novo para toda a equipe",
            "Obrigado pela atenção no atendimento anterior",
            "Desejo um ótimo dia a todos",
            "Agradeço a cordialidade no atendimento",
            "Bom dia! Espero que estejam bem",
            "Obrigado pela presteza",
            "Envio apenas cumprimentos"
        ]
        # Cria as tags correspondentes
        tags_produtivos = ["produtivo"] * len(treinos_produtivos)
        tags_improdutivos = ["improdutivo"] * len(treinos_improdutivos)
        self.treinos = treinos_produtivos + treinos_improdutivos
        self.tags = tags_produtivos + tags_improdutivos

        # Pré-processa os textos de treino
        treinos_processados = [preprocessar_texto(t) for t in self.treinos]
        self.vetorizador = CountVectorizer()
        self.matriz_treino = self.vetorizador.fit_transform(treinos_processados)
        self.modelo = LogisticRegression()
        self.modelo.fit(self.matriz_treino, self.tags)

    def classificar(self, texto):
        # Pré-processa e classifica o texto recebido
        texto_proc = preprocessar_texto(texto)
        matriz_texto = self.vetorizador.transform([texto_proc])
        return self.modelo.predict(matriz_texto)[0]
