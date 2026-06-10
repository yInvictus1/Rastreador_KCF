# 🎯 Rastreamento de Objetos com OpenCV

Rastreamento de objetos em vídeo usando **OpenCV** com o algoritmo **KCF** (Kernelized Correlation Filters).

---

## 📸 Funcionalidades

- Seleção visual do objeto com o mouse
- Rastreamento em tempo real frame a frame
- Indicação visual quando o objeto é perdido
- Suporte a qualquer arquivo de vídeo (`.mp4`, `.avi`, `.mov`)

---

## 🚀 Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/rastreamento.git
cd rastreamento
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Adicione um vídeo `.mp4` na pasta do projeto

---

## ▶️ Executando

```bash
python main.py              # usa 'race.mp4' como padrão
python main.py meu_video.mp4
```

### Controles

| Tecla | Ação |
|-------|------|
| **Mouse** | Selecione o objeto arrastando um retângulo |
| **ENTER / ESPAÇO** | Confirma a seleção |
| **C** | Cancela a seleção |
| **ESC** | Encerra o rastreamento |

---

## 🛠️ Tecnologias

| Tecnologia | Uso |
|---|---|
| [OpenCV](https://opencv.org/) | Processamento de vídeo e rastreamento |
| Python 3.10+ | Linguagem base |

---

## 📁 Estrutura do projeto

```
rastreamento/
├── main.py             # Script principal
├── requirements.txt    # Dependências
├── .gitignore          # Arquivos ignorados pelo Git
└── README.md           # Este arquivo
```

---

## 📝 Licença

Este projeto é de uso livre para fins educacionais.
