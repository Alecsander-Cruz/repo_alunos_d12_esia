# Contexto do pacote MiniLoja

- Disciplina D1.2 (Desenvolvimento Assistido por IA), 24h; caso didático fictício, sem aplicação real a implantar.
- Runtime de referência: Python 3.11 ou superior, somente biblioteca padrão. O pacote foi verificado com Python 3.12.3.
- `caso/`: contrato (`regras.md`), código em `caso/miniloja/`, suíte existente em `caso/testes_existentes/` e dados sintéticos; `testes/`: verificações e ferramenta de mutação; `apoio/`: materiais textuais; `exercicios/aula-1/` a `aula-6/`: registros.
- Verificações do caso, na raiz desta pasta: `python -B testes/test_miniloja.py --codigo caso`.
- Há onze verificações: no material inicial, oito passam e três falham (as três são tarefas do bloco 1). Código de saída `1` indica falhas e `0` indica sucesso no conjunto executado. Os testes não atribuem nota ao aluno.
- Suíte existente do caso: `python -B testes/test_miniloja.py --codigo caso --existentes` (26 testes; parte deles é tautológica de propósito).
- `--codigo DIR` seleciona a pasta com o pacote `miniloja` (pode ser uma cópia de trabalho); `--teste TestMiniLoja.nome` seleciona uma verificação. Resultados textuais observados ficam em `apoio/resultado-textual.md`.
- Leia `caso/regras.md` antes de pedir qualquer mudança: o contrato vale mais que o código atual.
- Não alterar `testes/` nem `caso/regras.md`. Qualquer mudança no caso deve ter escopo declarado, plano revisado e verificação; registrar assistência, evidência, decisão e limite.
