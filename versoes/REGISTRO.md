# Registro de rodadas · Triângulo OCR

Uma entrada por rodada, a mais recente no topo. A próxima rodada começa lendo a última entrada e confirmando se a "próxima oportunidade" ainda existe na versão atual.

---

## 2026-11-19 · rodada 6 · v2.5 → v2.6 (`index.html`)

**Origem → entrega.** `index.html` v2.5 (md5 c7c661be, igual ao publicado; arquivado como `versoes/index_v2-5_c7c661be.html`) → `index.html` v2.6 (md5 3bdd3036). Commit local; **não enviado** ao GitHub (publicar só a pedido).

**Problema reproduzido** (oportunidade da rodada 5, e maior do que registrado). Depois de "Adotar B" numa semelhança demonstrada, `decide` ignorava `s.adocao`: o relatório seguia dizendo "A segue como controle até você decidir", oferecia "Adotar B" de novo, o controle da próxima batelada continuava A, e o **resumo ROAST_HISTORY registrava "Próxima prova: controle A"** com a decisão antiga — o histórico de torra contradizia a escolha feita.

**Mudança aplicada.** `decide` com adoção registrada: decisão "Você adotou B como controle em <data>, com base na semelhança demonstrada… O próximo A/B parte de B"; `proximo.controle` = controle adotado; `adotavel` falso (some o botão de adotar). No relatório, a proposta gravada (`s.proximo`) acompanha a adoção salvo troca manual (`controleEditado`). A linha separada "Você escolheu adotar…" saiu (a decisão já diz).

**Evidência (sessão semeada SIM_OK, 12/40, pd 30 %; tablet 768×1024).**
- Antes (v2.5), após adotar: decisão "SIM_OK segue como controle até você decidir"; botões "mantendo SIM_OK" + "Adotar SIM_OKb"; controle da próxima = SIM_OK; resumo "Próxima prova: controle SIM_OK".
- Depois (v2.6), após adotar: decisão "Você adotou SIM_OKb como controle em 19/11/2026…"; botão único "Criar próximo A/B" (abre com SIM_OKb); controle da próxima = SIM_OKb; resumo "Próxima prova: controle SIM_OKb" e decisão nova. Antes de adotar: igual à v2.5.
- Vizinhos: troca manual do controle depois de adotar (OCR_402) mantida; relatório de diferença inalterado; recarregar preserva adoção e próxima batelada; veredito ≤ 676 px; sem erros no console.

**Próxima oportunidade.** Mesma tela pós-adoção: "Quanto posso confiar?" diz "Indicativa: confirme antes de mudar a torra" (repetições em semelhança), mas a decisão "Você adotou B… O próximo A/B parte de B" não propõe a confirmação que a confiança pede. Cenário: semelhança demonstrada com 2 avaliadores → Adotar B. Avaliar se a próxima batelada, nesse caso, deve sugerir uma série de confirmação (outro avaliador ou nova sessão) em vez de um A/B qualquer a partir de B.

---

## 2026-11-19 · rodada 5 · v2.4 → v2.5 (`index.html`)

**Origem → entrega.** `index.html` v2.4 (md5 b1279ba3, igual ao publicado; arquivado como `versoes/index_v2-4_b1279ba3.html`) → `index.html` v2.5 (md5 c7c661be). Commit local; **não enviado** ao GitHub (publicar só a pedido).

**Problema reproduzido** (oportunidade da rodada 4, confirmada no código: `ultimaConfig` copiava os avaliadores e trocar de modo não limpava). Última sessão solo → Nova comparação → Revezamento → Ana e Bia → plano com provadores {Você, Ana, Bia}; a rodada 1 pedia "Prepara Ana · **Prova Você**" — uma pessoa que não existe.

**Mudança aplicada.** `NOME_SOLO = 'Você'` é só o nome provisório do modo sozinho: `ultimaConfig` não o repete (`semProvisorio`), trocar para revezamento/preparador dedicado o remove, e a validação recusa "Você" fora do modo sozinho com explicação. Nomes reais seguem sendo repetidos.

**Evidência (mesmo cenário semeado, v2.4 × v2.5).**
- Antes: avaliadores ao abrir [Você]; após trocar de modo [Você]; plano {Você, Ana, Bia}; rodada 1 "Prova Você".
- Depois: ao abrir []; após trocar []; plano {Ana, Bia}; rodada 1 "Prepara Bia · Prova Ana".
- Vizinhos: "Você" digitado à mão no revezamento → recusado, sessão não criada; solo seguido de solo sem cadastrar ninguém → sessão criada com [Você]; nome real no solo ("Pedro") → repetido, sobrevive à troca de modo, plano {Pedro, Ana}; sem erros no console.
- Armadilha de teste: o servidor local deixou o navegador usar a v2.4 em cache numa primeira tentativa (o teste invalidado foi refeito com `?v=` na URL).

**Próxima oportunidade.** Relatório de semelhança demonstrada depois de adotar B: a decisão continua dizendo "A segue como controle até você decidir" logo acima de "Você escolheu adotar B como controle em …" — duas frases que se contradizem na mesma tela. Cenário: semelhança demonstrada → "Adotar B e criar próximo A/B" → voltar ao relatório. Também observado: após publicar, o celular pode mostrar a versão anterior por alguns minutos (cache do GitHub Pages); vale um aviso de versão nova ou instrução de recarregar.

---

## 2026-11-19 · rodada 4 · v2.3 candidata → v2.4 definitiva (`index.html`)

**Pedido do usuário:** "Quero uma aplicação definitiva, não uma candidata." A partir desta rodada, `index.html` é a aplicação e as rodadas o editam direto (ver CLAUDE.md).

**Origem → entrega.** `triangulo_ocr_v2-3_candidata.html` v2.3 (md5 7e5af323, conferido; arquivado como `versoes/triangulo_ocr_v2-3_candidata_7e5af323.html`) → `index.html` **v2.4** (md5 b1279ba3). A estável anterior (v2.0, 98f2e34d) já estava em `versoes/index_v2-0_98f2e34d.html`. As quatro candidatas da raiz foram removidas depois de conferir cópia idêntica em `versoes/` (v2.0 aefefef7, v2.1 c7bf6007, v2.2 a899fd0e, v2.3 7e5af323). Nada publicado.

**Problema reproduzido** (oportunidade da rodada 3, confirmada). O relatório não respondia "Quanto posso confiar?": rótulos "Síntese | Decisão prática" em 8/8 cenários; diferença com 2 avaliadores, solo e com desvio abriam com a mesma manchete "Distinguimos as torras: 9 de 12 (p = 0,004)", com a ressalva escondida num aparte.

**Mudança aplicada.** `OCRAN.confianca(s)` (pura) → categoria escrita + porquê com o dado; veredito com três rótulos ("O que aconteceu" · "Quanto posso confiar?" · "O que faço agora"); confiança também no resumo ROAST_HISTORY, nota .md, CSV, JSON e Histórico. Sessões migradas da v1 recebem ressalva (a v1 não travava plano nem registrava desvios).

**Evidência (tablet 768×1024).**
- Antes (v2.3): 0/8 relatórios com resposta de confiança.
- Depois (v2.4): 9/9 com a categoria esperada — DIF_SIG sustentada · DIF_SOLO indicativa · DIF_DESV indicativa · DIF_INC sem conclusão · DIF_NULO limitada (até 41 %) · SIM_OK indicativa (repetições, ASTM) · SIM_INC sem conclusão · DESC_SO só observação · sessão migrada da v1 indicativa; veredito termina ≤ 764 px (primeira tela).
- Corrigido durante o teste: a sessão migrada saía "sustentada… sem desvio registrado" — falso para a v1.
- Regressões verificadas: migração com dados da v1 + 8 sessões v2 (10 sessões, chaves v1 byte a byte intactas, moagem preservada, link para concluir série da v1 em `versoes/triangulo_ocr_v1_b3214c3c.html`); sessão completa real no `index.html` (6 rodadas em revezamento, nenhum OCR na prova, 1 botão em todas as "Resposta registrada", ficha em 4 passos, escolha, revelar, relatório); exportações com confiança; sem erros no console.
- Pendente de bancada: leitura das categorias por você no tablet real.

**Próxima oportunidade.** "Nova comparação" herda avaliadores da última sessão; se ela foi solo, o chip "Você" (nome-placeholder do modo solo) continua ao trocar para revezamento e vira um avaliador real no plano. Cenário reproduzido nesta rodada: última sessão solo → Nova comparação → Revezamento → adicionar Ana e Bia → relatório "3 avaliadores (Você 2, Ana 2, Bia 2)". Risco: plano de rodadas com uma pessoa que não existe e repetições divididas por 3.

---

## 2026-11-18 · rodada 3 · v2.2 → v2.3 candidata

**Origem → entrega.** `triangulo_ocr_v2-2_candidata.html` v2.2 (md5 a899fd0e, conferido igual ao registrado; arquivado como `versoes/triangulo_ocr_v2-2_candidata_a899fd0e.html`) → `triangulo_ocr_v2-3_candidata.html` v2.3 candidata (md5 7e5af323). `index.html` (98f2e34d) intacto; nada publicado.

**Problema reproduzido** (oportunidade da rodada 2, confirmada). A ficha descritiva era uma tela única: no tablet 768×1024, 3.176 px de altura, 49 botões, "Seguir para a escolha" a 3.068 px → 2.104 px de rolagem com as xícaras esfriando.

**Mudança aplicada.** A fase `ficha` passa a ter 4 passos na ordem da prova (`PASSOS_FICHA`, salvo em `s.desc.etapa.passo`): acidez/doçura/corpo → finalização/complexidade/limpeza → descritores e ao esfriar → sinais. Cabeçalho "Ficha · passo k de 4" com o nome de quem preenche; "Próximo: …" como ação principal e "Voltar ao passo anterior" discreto. Valor do eixo subiu para a linha do rótulo (`.ap-h`) e o espaçamento dos eixos foi reduzido; alvos de toque continuam ≥ 52 px. Formato da ficha inalterado.

**Evidência (mesma ficha típica: 12 notas, 1 descritor, sinais "nenhum"; tablet 768×1024).**
- Antes (v2.2): 1 tela de 3.176 px; rolagem até "Seguir" 2.104 px; 17 toques.
- Depois (v2.3): 4 passos, botão de avançar a 885–1.017 px → rolagem 0 em todos, **com o relógio de cupping ligado** (sem relógio: 885–998 px); 20 toques (+3 "Próximo"); menor alvo 52 px; dados gravados idênticos (12 × 6, "caramelo", sinais "nenhum").
- Regressões verificadas: recarregar volta no passo salvo; "Voltar à ficha" da escolha cai no último passo; léxico abre no passo 3 e, ao fechar, mantém o passo e o termo; travar → revelar → relatório com notas, descritores, gráfico e tempo; modo solo (Esquerda/Direita, sem OCR, virar xícaras depois de travar) intacto; sem erros no console.
- Margem curta: com relógio, o botão dos passos 1–2 fica a 1.017 de 1.024 px. Sinais com vários itens marcados alongam o passo 4 (rolagem possível nesse caso). Não validado em bancada nem em tablet real.

**Próxima oportunidade.** Relatório: "Quanto posso confiar?" não tem resposta explícita. No relatório de demonstração (tablet), síntese a 310 px, decisão a 439 px e "Próxima batelada" a 853 px estão na primeira tela, mas a força da evidência está diluída numa linha técnica de 125 caracteres em "Distinguimos?" ("9 de 12 acertos · limiar 8 · p = 0,004 · 2 avaliadores (…) · pelo menos 21 %…"); nenhuma linha diz, em português direto, se a conclusão é sólida, exploratória (solo, desvios, repetições desiguais) ou sem conclusão. Cenário: depois de revelar, decidir a próxima batelada do Atilla lendo só a primeira tela. Cuidado: a resposta deve sair de regras transparentes já calculadas (série completa, `exploratory`, avaliadores distintos, limites de pd), sem inventar escala de confiança.

---

## 2026-11-18 · rodada 2 · v2.1 → v2.2 candidata

**Origem → entrega.** `triangulo_ocr_v2-1_candidata.html` v2.1 (md5 c7bf6007, conferido igual ao registrado; arquivado como `versoes/triangulo_ocr_v2-1_candidata_c7bf6007.html`) → `triangulo_ocr_v2-2_candidata.html` v2.2 candidata (md5 a899fd0e). `index.html` (98f2e34d) intacto; nada publicado.

**Problema reproduzido** (oportunidade da rodada 1, confirmada no código). Na tela "Resposta registrada", que é do provador, apareciam "Registrar desvio", "Invalidar a última rodada", "Interromper a série" e "Apagar sessão". Mais grave: a invalidação aceitava qualquer texto, inclusive "fiquei em dúvida, chutei", tirando a rodada da análise e repondo-a. Invalidar respostas incertas descarta justamente os palpites (acerto 1/3) e deixa o p-valor otimista.

**Mudança aplicada.**
- "Resposta registrada" sem controles de sessão (só a ação principal).
- Nas telas de quem prepara ("Quem faz o quê"/"Monte a rodada") e em "Rodadas concluídas", os controles ficam num `<details>` "Algo saiu do protocolo?", sempre fechado ao renderizar.
- Invalidar exige um motivo de protocolo (`INV_MOTIVOS`: pista vista, posição errada, erro de preparo, prova interrompida/contaminada, outro com descrição); aviso "Dúvida na resposta não é motivo"; "Outro" com texto de incerteza (`INCERTEZA`) é recusado com explicação. `motivo` continua texto, então relatório, CSV e sessões antigas não mudam.

**Evidência (mesmo roteiro, revezamento Ana/Bia, n = 6, viewport tablet 768×1024).**
- Antes (v2.1): 5 botões visíveis na "Resposta registrada"; "fiquei em dúvida, chutei" aceito → rodada invalidada, plano 6 → 7.
- Depois (v2.2): 1 botão na "Resposta registrada" (5 de 5 rodadas; também no modo solo); na tela de quem prepara, 1 botão visível e 4 recolhidos; sem motivo → "Escolha o que saiu do protocolo."; "Outro: fiquei em dúvida, chutei" → recusado, rodada segue válida (plano 6); "Provador viu o fundo" → invalidada, reposição para a mesma pessoa (plano 7), controles voltam a fechar.
- Regressões verificadas: recarregar no meio da série volta a "Quem faz o quê" com a invalidação preservada e sem OCR na tela; série completa com 6/6 válidas (reposição contou); relatório lista "rodada do plano 1 (Ana): Provador viu o fundo ou outra pista"; modal cabe no tablet sem rolar; sem erros no console.
- Limite que permanece: no revezamento, quem prepara a rodada seguinte é quem acabou de provar, então essa pessoa ainda alcança "Invalidar" — agora só com motivo de protocolo. Não validado em bancada.

**Próxima oportunidade.** Ficha descritiva no tablet (768×1024): a tela "Ficha descritiva" tem 3,1 alturas de tela (3.176 px), 49 botões, e "Seguir para a escolha" fica a 3.068 px do topo — o provador rola três telas com as duas xícaras esfriando. Cenário: Ana preenche os 6 eixos × 2 posições, depois descritores, "Ao esfriar" e sinais, sempre rolando. Ideia a avaliar: dividir em passos (eixos → descritores/ao esfriar → sinais) ou compactar os controles "Não percebido/Não avaliado", medindo rolagem e toques antes e depois.

---

## 2026-11-18 · rodada 1 · v2.0 → v2.1 candidata

**Origem → entrega.** `index.html` v2.0 (md5 98f2e34d, arquivado como `versoes/index_v2-0_98f2e34d.html`) → `triangulo_ocr_v2-1_candidata.html` v2.1 candidata (md5 c7bf6007). `index.html` não foi alterado e continua a versão estável; nada publicado.

**Problema reproduzido.** O relatório e o planejamento afirmavam mais do que os critérios travados sustentam:
1. Semelhança inconclusiva (40 rodadas, 18 acertos, pd 30 %) → "indício de diferença pequena a média". Os dados dão pd de 0 a 39 % (95 %): não há evidência de diferença.
2. Semelhança demonstrada (40, 12 acertos) → B promovido a controle automaticamente no próximo A/B.
3. Planejamento com n = 29 → "já permite dizer que é pequena (até 27 %)", contradizendo a faixa < 25 %; promessa "use n ≥ 28" falsa para 29 e 32 (dente de serra).
4. Ajuda e decisão citavam n de semelhança sem considerar o número de avaliadores ("cerca de 39"; com 2 avaliadores o n certo é 44).

**Mudança aplicada.**
- Núcleo: `nForSim(pd, β, alvo, k, desde)` e `nSmallPd(k, desde)` andam de k em k a partir de um n e só devolvem um n que cumpre de fato; `kAvaliadores`; `NMAX` no núcleo.
- `decide`: inconclusivo diz que nenhum critério foi atendido e mostra só a faixa de pd; semelhança demonstrada mantém A como controle e explica que adotar B é escolha pelo motivo da mudança; `proximo.adotavel`; n sugeridos exatos e múltiplos de k.
- Relatório: botões "Próximo A/B mantendo A" e "Adotar B e criar próximo A/B" (grava `s.adocao`, mostrado no relatório); n e plano da prova acompanham a regra atual salvo edição manual (`provaEditado`); desfaz o B herdado da v2.0 (`controleEditado` protege edição manual).
- Configuração: `alcanceNulo` decide pelo próprio n e sugere "use n = X"; validação e ajuda sem n fixo.

**Evidência (mesmas 3 sessões semeadas, mesma origem, viewport tablet 768×1024).**
- Antes (v2.0): SIM_18 "indício de diferença pequena a média"; SIM_12 próximo A/B com controle = SIM_12b; n = 29 "pequena (até 27 %)"; ajuda "cerca de 39".
- Depois (v2.1): SIM_18 "nem semelhança nem diferença… compatíveis com torras iguais e com até 39 %… n = 44"; SIM_12 controle = SIM_12, adoção só pelo botão e registrada; n = 29 → "só descarta acima de 27 %… use n = 30"; n = 28 → "pequena (até 24 %)".
- Node: varredura k ∈ {1,2,3}, n inicial 6–90, pd 20–35 %, alvo 80/90 % → 0 n sugeridos que não cumprem o prometido. Regra de semelhança segue batendo com Campden (n 42 → 16) e sensR (p 0,7071).
- Regressões verificadas: relatório de demonstração (diferença detectada) igual; rodada cega real com n = 6 sem OCR na tela de prova, 1 registro após clique duplo, sem placar no "Resposta registrada"; edição manual do plano persiste; sem erros no console.
- Pendente de bancada: nada estatístico; os textos novos não foram lidos por você no tablet real.

**Próxima oportunidade.** Tela "Resposta registrada" (modo dupla e solo, a cada rodada do triângulo): logo após responder, o provador cego vê "Registrar desvio", "Invalidar a última rodada" e "Interromper a série". Controles avançados ao alcance de quem provou, contra a regra de bancada (só a ação principal durante a prova). Cenário: Ana confirma a resposta e, com o tablet na mão, pode invalidar a própria rodada. Ideia: levar essas ações para a tela de quem prepara ("Quem faz o quê") ou atrás de um "Mais ações" com confirmação.
