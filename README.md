# MVP - Classificação de Avaliações de Viagem

Este projeto tem como objetivo aplicar técnicas de Machine Learning para prever a nota de avaliações de viagem, com base em características do review.

## Estrutura do Projeto

- `notebook/`: Notebook do Google Colab com todo o processo de modelagem e análise.
- `backend/`: Aplicação Flask com API que carrega o modelo e responde previsões.
- `frontend/`: Interface simples em HTML para envio de dados.
- `tests/`: Teste automatizado com PyTest.
- `requirements.txt`: Lista de dependências.

## Execução

### Instalar dependências
```bash
pip install -r requirements.txt
```

### Executar backend Flask
```bash
cd backend
python app.py
```

### Abrir frontend
Abra `frontend/index.html` em seu navegador.

### Executar testes
```bash
pytest tests/test_modelo.py
```

## Link do Notebook no Colab
https://colab.research.google.com/drive/1Uo37ibDjeGQzdjtAV7lEo2XqCs-Derit#scrollTo=PriKndi7UIuT

## Link do vídeo de demonstração
https://share.vidyard.com/watch/v6vRazcqjojEuMDBEWpqc5