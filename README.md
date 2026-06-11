# Gerador de QR Code via Linha de Comando 🚀

Este é um script simples em Python que permite gerar imagens de QR Code diretamente pelo terminal. O script aceita qualquer texto ou link (URL) e salva o resultado no formato de imagem que você escolher (como `.png` ou `.jpg`).

---

## 🛠️ Pré-requisitos e Instalação

Antes de rodar o script, você precisa ter o **Python 3** instalado na sua máquina e instalar as bibliotecas necessárias (`qrcode` e `pillow`).

Abra o seu terminal e execute o comando abaixo para instalar as dependências:

```bash
pip install qrcode pillow
💻 Como Usar
O script foi desenvolvido para ser executado via linha de comando (terminal). Você precisa passar dois argumentos obrigatórios:

O conteúdo do QR Code (texto ou link entre aspas).

O nome do arquivo de saída (com a extensão de imagem desejada).

Sintaxe:
Bash
python GeneratorImage.py "<dados_ou_link>" <nome_do_arquivo.png>
Exemplos Práticos:
Gerar um QR Code para um site:

Bash
python GeneratorImage.py "[https://github.com](https://github.com)" github_qr.png
Gerar um QR Code com um texto simples:

Bash
python GeneratorImage.py "Minha Senha do Wi-Fi ou Texto" texto.png
⚙️ Detalhes Técnicos
O script utiliza as seguintes configurações padrão para a geração do QR Code:

Versão: 1 (Tamanho inicial do QR Code, expande automaticamente se o texto for grande).

Correção de Erro: L (Permite a leitura do código mesmo se até 7% dele estiver danificado ou coberto).

Tamanho do Bloco: 10 pixels por quadrado.

Borda: 4 quadrados de espessura (padrão recomendado para garantir a leitura).

Cores: Código em preto (black) com fundo branco (white).

📝 Licença
Este projeto é livre para uso, modificação e distribuição.
