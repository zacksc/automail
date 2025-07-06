# AutoMail - Classificador e Respondedor Automático de E-mails

## Descrição

O **AutoMail** é um aplicativo web desenvolvido em Flask que classifica e responde automaticamente e-mails em português. Ele utiliza machine learning para identificar se um e-mail é "produtivo" (requer ação) ou "improdutivo" (apenas felicitações/agradecimentos) e gera uma resposta adequada usando um modelo de linguagem da HuggingFace.

## Tecnologias Utilizadas

- **Flask**: Framework web para Python.
- **scikit-learn**: Para classificação de e-mails (Logistic Regression + CountVectorizer).
- **NLTK**: Pré-processamento de texto (stopwords, stemming).
- **PyMuPDF (fitz)**: Leitura de arquivos PDF.
- **huggingface_hub**: Integração com modelos de linguagem (Mixtral-8x7B-Instruct-v0.1 via Together API).
- **HTML/CSS**: Interface web responsiva.

## Estrutura de Pastas

```
classificador-email/
│
├── app.py                  # Arquivo principal Flask
├── email_classificador.py  # Lógica de classificação de e-mails
├── email_responder.py      # Geração de resposta automática via IA
├── leitor_arquivo.py       # Leitura de arquivos .txt e .pdf
├── preprocessar.py         # Funções de pré-processamento de texto
├── __init__.py
│
├── static/
│   └── style.css           # Estilos CSS
│
├── templates/
│   ├── index.html          # Página inicial
│   ├── classificar.html    # Formulário de envio/classificação
│   └── resultado.html      # Exibição do resultado e resposta sugerida
│
└── __pycache__/            # Arquivos compilados Python (gerados automaticamente)
```

## Como Funciona

1. **Entrada**: O usuário pode colar o texto do e-mail ou enviar um arquivo `.txt` ou `.pdf`.
2. **Classificação**: O texto é pré-processado (minúsculas, remoção de stopwords, stemming) e classificado como "produtivo" ou "improdutivo" usando um modelo treinado com scikit-learn.
3. **Resposta Automática**: Dependendo da categoria, uma resposta é gerada automaticamente via modelo Mixtral-8x7B-Instruct-v0.1 da HuggingFace.
4. **Interface**: O resultado e a resposta sugerida são exibidos de forma amigável, com opção de copiar a resposta.

## Instalação

1. Clone o repositório.
2. Instale as dependências:

```sh
pip install -r requirements.txt
```

3. Execute o aplicativo:

```sh
python app.py
```

4. Após rodar o comando acima, acesse o endereço exibido no terminal (geralmente http://localhost:5000) para utilizar o sistema.

## requirements.txt

```
flask
scikit-learn
nltk
PyMuPDF
huggingface_hub
```

## Observações

- Para o funcionamento do NLTK, os pacotes `stopwords` e `rslp` são baixados automaticamente na primeira execução.
- É necessário um token de API válido da HuggingFace para gerar respostas automáticas.
- O aplicativo aceita arquivos `.txt` e `.pdf` para análise.

---

Sinta-se à vontade para adaptar ou expandir a estrutura conforme o projeto evoluir!

## Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.