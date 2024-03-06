from transformers import AutoTokenizer, BertForSequenceClassification
import numpy as np
import matplotlib.pyplot as plt
from Teste_extracao import extract_sentences_from_pdf
pred_mapper = {
    0: "POSITIVE",
    1: "NEGATIVE",
    2: "NEUTRAL"
}

tokenizer = AutoTokenizer.from_pretrained("lucas-leme/FinBERT-PT-BR")
finbertptbr = BertForSequenceClassification.from_pretrained("lucas-leme/FinBERT-PT-BR")

sentencas = extract_sentences_from_pdf("Transcricao_do_audio1T23.pdf")[0:50]
tokens = tokenizer(sentencas , return_tensors="pt",
                   padding=True, truncation=True, max_length=512)
finbertptbr_outputs = finbertptbr(**tokens)

preds = [pred_mapper[np.argmax(pred)] for pred in finbertptbr_outputs.logits.cpu().detach().numpy()]
print(preds)
Posi = 0
Neg = 0
Neutral = 0
for t in preds:
    if t =="POSITIVE":
        Posi+=1
    elif t == "NEGATIVE":
        Neg+=1
    else:
        Neutral+=1

# Dados para o gráfico
categorias = ['Positive', 'Neutral', 'Negative']
valores = [Posi, Neutral, Neg]

# Criar o gráfico de barras
plt.bar(categorias, valores)
# Adicionar rótulos aos eixos
plt.xlabel('Categorias')
plt.ylabel('Valores')
# Exibir o gráfico
plt.show()
