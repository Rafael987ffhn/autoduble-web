AutoDub Web (Projeto Completo)

Este é um projeto local que permite dublar vídeos automaticamente via navegador.

▶ FUNCIONALIDADES:
- Interface web simples
- Upload de vídeos .mp4
- Dublagem com Whisper + gTTS
- Tradução automática (opcional)
- Download automático do vídeo dublado

📦 ESTRUTURA:
- app.py ...................... Arquivo principal Flask
- templates/index.html ........ Página HTML
- uploads/ .................... Vídeos enviados
- outputs/ .................... Vídeos dublados

🛠 COMO USAR:
1. Instale o Python 3.10 ou superior.
2. Instale as dependências:
   pip install -r requirements.txt
3. Execute o servidor:
   python app.py
4. Acesse no navegador:
   http://localhost:5000

🎯 Requisitos:
- Python
- Conexão com internet (para GTTs e tradução)

⛔ Atenção: Este projeto não funciona diretamente no Google Sites!
