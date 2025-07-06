import fitz

class FileReader:
    @staticmethod
    def read_text_file(arquivo):
        return arquivo.read().decode("utf-8")

    @staticmethod
    def read_pdf_file(arquivo):
        conteudo_pdf = ""
        with fitz.open(stream=arquivo.read(), filetype="pdf") as doc:
            for pagina in doc:
                conteudo_pdf += pagina.get_text()
        return conteudo_pdf

    @staticmethod
    def read_file(arquivo):
        if arquivo.filename.endswith(".txt"):
            return FileReader.read_text_file(arquivo)
        elif arquivo.filename.endswith(".pdf"):
            return FileReader.read_pdf_file(arquivo)
        return "Formato de arquivo não suportado."
