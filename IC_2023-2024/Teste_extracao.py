import fitz  # PyMuPDF
import regex as re


def extract_sentences_from_pdf(pdf_path):
    sentences = []

    # Abre o arquivo PDF
    pdf_document = fitz.open(pdf_path)

    # Itera sobre as páginas do PDF
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text = page.get_text()

        # Divide o texto em frases usando o ponto final como separador
        sentence_list = re.split(r'(?<=[.!?])\s+', text)

        # Adiciona as frases à lista de frases
        sentences.extend(sentence_list)

    # Fecha o documento PDF
    pdf_document.close()

    return sentences


if __name__ == "__main__":
    pdf_path = "Transcricao_do_audio1T23.pdf"
    sentences = extract_sentences_from_pdf(pdf_path)

    # Exibe as frases
    for i, sentence in enumerate(sentences):
        print(f"Frases {i + 1}: {sentence}")