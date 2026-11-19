# Registro de rodadas · Triângulo OCR

Uma entrada por rodada, a mais recente no topo. A próxima rodada começa lendo a última entrada e confirmando se a "próxima oportunidade" ainda existe na versão atual.

---

## 2026-11-19 · rodada 13 · v2.12 → v2.13 (`index.html`)

**Origem → entrega.** `index.html` v2.12 (md5 f2793150, igual ao publicado; arquivado como `versoes/index_v2-12_f2793150.html`) → `index.html` v2.13 (md5 no commit). Commit local; **não enviado**. Pedido do usuário: "coisas fora da tela principal quando visto do celular".

**Auditoria (v2.12).** Roteiro de 32 telas e janelas (início, configuração em todas as variantes, prévia do .alog, "Por quê?", A/B em dupla do mapa ao relatório, léxico, triângulo, Histórico, restauração, demonstração, biblioteca, treino) a 360×740 e 320×640. Para cada uma: elementos além da borda, caixas com rolagem lateral e, nas janelas, a ação final dentro da caixa.
- Relatório, "Torra A × B": tabela de 560 px numa área de 294 (254 em 320). Δ e origem ficavam fora da tela.
- Relatório com triângulo, "Rodada a rodada": a página rolava para o lado (479/360 e 479/320).
- Janela do léxico: sem busca, listava o catálogo inteiro (20.461 px) e o "Fechar" ficava a 20.484 px. Com busca, os resultados vinham depois de três seletores e 11 famílias.
- Prévia do .alog a 320: a janela rolava para o lado (tabela Dado/Valor/Origem).
- O resto, incluindo ficha, escolha, triângulo e configuração, estava ok (efeito da v2.11).

**Mudança aplicada.**
- `table.t.empilha` (≤ 620 px): tabelas largas viram blocos rotulados por `data-label` (`.inline` deixa as células na mesma linha). Vence `table.t` e `table.torra-ab{min-width:560px}`, que vêm depois no CSS. Usada em Torra A × B, Rodada a rodada e prévia do .alog. No tablet seguem em colunas.
- Léxico (janela): busca e seletor de "Família" no topo; "Anotar em" e "Intensidade" lado a lado, com a Fase embaixo; resultados logo abaixo. Sem busca nem família, mostra "Digite um termo ou escolha uma família." A página Biblioteca não muda.
- Toda janela: `.box` com `max-height:88dvh` e a última fileira de botões fixa no rodapé da caixa, cobrindo margem e laterais.

**Evidência (depois).** O mesmo roteiro de 32 itens: **32/32 ok** em 320×640, 360×740, 375×667 e 768×1024.
- Léxico a 360: conteúdo de 830 px, "Fechar" visível; com a família Floral, o primeiro "Anotar" aparece aos 403 px. Anotar segue funcionando.
- Torra A × B a 320: 254/254 px, sem rolagem lateral.
- Console limpo.

**Limites.** Emulador, não aparelho: `dvh` e a área segura variam por navegador. A Torra A × B empilhada fica longa (~2.400 px), mas fica dentro de um bloco que abre e fecha.

**Próxima oportunidade.** Conferir no celular real (barra de endereço, teclado aberto na ficha). Seguem abertos: a 2ª ficha mais fria na dupla e o limite de carga (3 °C) com o operador.

---

## 2026-11-19 · rodada 12 · v2.11 → v2.12 (`index.html`)

**Origem → entrega.** `index.html` v2.11 (md5 816953b2, commit local, não publicado; arquivado como `versoes/index_v2-11_816953b2.html`) → `index.html` v2.12 (md5 no commit). Commit local; **não enviado**.

**Oportunidade da rodada 11** (celular real, teclado): depende do aparelho do usuário; segue aberta. Nesta rodada, inspeção por captura no celular (375×667) do passo 3, do léxico e do relatório.

**Problema reproduzido (v2.11).** A impressão livre não era aproveitada. No passo 3 a tela dizia "nenhum ainda" e pedia busca no léxico ou digitação. Para anotar "caramelo" (Esquerda) e "chocolate amargo" (Direita), já escritos, eram ~24 teclas, 2 toques no seletor de lado e 2 em "Anotar". O termo digitado entrava como livre mesmo existindo no catálogo. No celular, a janela do léxico mostra o resultado só depois de "Anotar em", "Fase", "Intensidade", busca e 11 famílias, e é preciso rolar.

**Mudança aplicada.**
- Passo 3: para cada lado, as palavras da impressão livre (`palavrasLivre`: separa por , ; . quebra de linha e " e "; deduplica sem acento; 2–40 letras; até 8) viram botões (`sugLivre`, `data-livresug`, alvos de 52 px). Um toque anota, outro desfaz.
- `termoLex`: correspondência **exata** sem acento com nome, original ou sinônimo do catálogo. Com correspondência, entra com o nome e a família do catálogo e o botão mostra "· léxico" ou "→ Nome do catálogo". Sem ela, entra como termo livre (`livre: true`), sem família. O formato do descritor não mudou.

**Evidência.**
- Antes: ~24 teclas + 4 toques para 2 descritores, ambos como livres. Depois: **2 toques, nada digitado**, "Caramelo" (Doce e caramelizado) e "Chocolate amargo" (Castanhas e cacau) do catálogo. O segundo toque desfaz.
- Casos de borda: "pé de moleque" → livre, sem família; "Floral/floral/FLORAL" → 1 botão; "x" e um texto de 50 letras ignorados; "seco" → "Secura no final" (sinônimo do catálogo, mostrado antes do toque). O estado marcado sobrevive ao recarregar.
- Relatório: "Descritores predominantes" A: Caramelo, pé de moleque · B: Chocolate amargo. Tablet: botões, janela do léxico e termo digitado funcionando juntos; ação visível; sem rolagem lateral (375 e 768).
- Observação: o CSV nunca trouxe descritores (a v2.11 também não); eles seguem no JSON e no relatório.

**Limites.** A separação por " e " pode dividir um termo composto ("pé de moleque e mel" vira dois, o que é correto; um nome com " e " no meio seria dividido). Não há correspondência aproximada, de propósito: "mel" não vira "Melaço".

**Próxima oportunidade.** No celular, a janela do léxico ainda põe a busca e os resultados abaixo de três seletores e 11 famílias. Cenário: passo 3 → "Buscar no léxico" → digitar → o resultado e o "Anotar" ficam fora da tela. Seguem abertos: o teclado no celular real e a 2ª ficha mais fria na dupla.

---

## 2026-11-19 · rodada 11 · v2.10 → v2.11 (`index.html`)

**Origem → entrega.** `index.html` v2.10 (md5 9c87f8fd, igual ao publicado; arquivado como `versoes/index_v2-10_9c87f8fd.html`) → `index.html` v2.11 (md5 no commit). Commit local; **não enviado**.

**Oportunidade da rodada 10** (2ª ficha mais fria na dupla): segue registrada, não foi a prioridade. Ao inspecionar as telas por captura, apareceu um problema maior: o app é usado no **celular** (link publicado), mas todas as medidas eram em 768×1024.

**Problema reproduzido (v2.10, 375×812).**
- Ficha: o botão de avançar ficava em 1.635 / 1.703 / 1.098 / 1.293 px nos passos 1–4, numa tela de 812. Cada eixo ocupava 415 px (Esquerda e Direita empilhadas, cada uma com cabeçalho, régua e dois botões de 52 px).
- Configuração com rolagem lateral: a página media 451 px, porque a tabela de planos (417 px) estourava o cartão (343).
- Régua "não avaliada" parada no 5: tocar sobre o marcador sem arrastar não dispara `input`, e o valor não era gravado.

**Mudança aplicada.**
- Posição da ficha em **uma linha**: [nome e valor | régua 0–10 | ✕ de 52 px]. **0 = "não percebido"** (antes, botão), **✕ = "não avaliado"** (antes, botão). Os estados gravados não mudam (`valor`/`nao_percebido`/`nao_avaliado`), então perfil, relatório e exportações seguem iguais.
- `pointerup` numa régua `.unset` grava o valor tocado.
- No celular (≤ 620 px): âncoras curtas (`ancoras()`, a descrição fica só no tablet), relógio e topo compactos.
- Botão de avançar da ficha e "Travar ficha e escolha" **fixos no rodapé** (`.acts-fixas`), com o contador "N posições sem marcar" (`faltaTxt`), que informa sem bloquear. "Voltar" fica no fluxo.
- Tabela de planos empilhada no celular (rótulos via `data-label`).

**Evidência.**
- 375×812: ação dos passos 1–4 a 742–802 px, visível em todos (antes 1.635/1.703/1.098/1.293). Configuração com largura 375 (antes 451).
- 375×667: passos 1–4 e escolha visíveis (657 px); no fim da rolagem o botão não cobre a última régua; triângulo (rodada, montagem com relógio, prova, confirmação) com ação visível.
- 768×1024: passos 1–2 a 713 px (a ficha também ficou mais curta), régua 205×52, ✕ 52; tabela de planos segue em colunas.
- Estados: 0 → `nao_percebido`, 6 → `valor 6`, ✕ → `nao_avaliado` (✕ desabilitado, "–"). Toque real no centro de uma régua parada no 5 gravou `valor 5` (sem o listener, o valor não muda e o `input` não dispara). O "antes" desse toque na v2.10 não foi reproduzido com clique real: a conversão de coordenadas do emulador não acertou o marcador.
- Biblioteca, treino, Histórico, demonstração, CSV/JSON/MD/Caderno ok. Console: só o bloqueio de vibração do navegador numa aba sem toque, que já acontecia antes.

**Limites.** Medido no emulador do navegador, não num celular real: barra de endereço, teclado e rolagem por toque precisam de conferência no seu aparelho. Arrastar até 0 grava "não percebido"; um arraste acidental até o começo grava isso.

**Próxima oportunidade.** Conferir no celular real a ficha e o rodapé fixo, principalmente com o teclado aberto na impressão livre e nos descritores (passo 3). Segue aberta a 2ª ficha mais fria na dupla.

---

## 2026-11-19 · rodada 10 · v2.9 → v2.10 (`index.html`)

**Origem → entrega.** `index.html` v2.9 (md5 e0696be8, igual ao publicado; arquivado como `versoes/index_v2-9_e0696be8.html`) → `index.html` v2.10 (md5 no commit). O pedido repetiu o da rodada 7. Esta rodada atacou o item ainda não atendido: "fluxo adequado para uma pessoa ou duas" perto dos 30 min. Commit local; **não enviado**.

**Problema reproduzido (v2.9, tablet).** Com Ana e Bruno, na comparação A/B, os dois só conseguiam provar no revezamento. Quem monta vê o mapa, então cada ficha pedia um par novo: 2 pares, 4 xícaras, 50 g, ~47 min estimados. O "embaralhar sem olhar", em que ninguém vê o mapa, recusava a dupla ("No modo sozinho, deixe só um avaliador.").

**Mudança aplicada.**
- O modo `solo` passa a se chamar **"Embaralhar sem olhar"** e aceita 2 ou mais avaliadores **só na comparação A/B**. Com triângulo, a dupla embaralhada é recusada com explicação. "Você" na dupla é recusado.
- Ao travar uma ficha no par embaralhado, se falta alguém (`faltamMesmoPar`: avaliadores sem ficha travada na sessão), a tela "aguarda" diz "Não vire nem mexa nas xícaras: Bruno prova a mesma esquerda e a mesma direita". A ação principal é "Bruno: começar a ficha" (`desc-mesmo-par`, mesmo par, mesmo relógio); há também "Ninguém mais vai provar: virar as xícaras" (`desc-virar`).
- "Qual fundo estava à esquerda?" agora resolve **todas** as fichas pendentes do par com uma resposta.
- A tabela de planos conta os avaliadores no modo embaralhado ("A/B · 2 fichas: 1 par, 2 xícaras, 33 g, 37 min").
- Textos do modo embaralhado corrigidos: "par novo" depois de virar, em vez de "fulano viu o mapa".

**Evidência (tablet 768×1024).**
- Antes: dupla só por revezamento (2 pares, 47 min); embaralhar recusava a dupla.
- Depois: dupla embaralhada aceita; tabela 1 par / 37 min. Ana: 25 toques até travar. Retomada correta na tela "aguarda", na impressão livre de Bruno (texto preservado) e em "Vire as xícaras". Um sorteio só. Uma resposta deu `BA` às duas fichas. Preferências mapeadas certo (Ana esquerda = OCR 502, Bruno direita = OCR 501). Relatório "2 fichas cegas (Ana, Bruno)", com tempo de bancada "1 par, 2 fichas". Nenhuma tela de prova com OCR.
- Vizinhos: sozinho com uma pessoa vira direto; revezamento sem a tela "aguarda"; "Ninguém mais vai provar" vira só a ficha de Ana; terceira pessoa (Carla) recebe par novo, e quem já tem ficha não é chamado de novo. Triângulo sozinho e em revezamento abrem a rodada 1. Botões novos de 60 e 52 px, sem rolar. Biblioteca, treino, Histórico, demonstração e Caderno ok; console limpo.

**Limites.** 37 min é estimativa e passa da meta de 30. O ganho vem de um par a menos e de ninguém precisar ver o mapa, mas as duas fichas seguem uma depois da outra num tablet só. Na bancada, a segunda pessoa prova enquanto a primeira preenche; o "Tempo de bancada" medido vai dizer o real. Provar sem comentar é instrução, não algo que o app garanta.

**Próxima oportunidade.** Com a dupla no mesmo par, a 2ª ficha começa mais tarde (minInicio maior) e pega a xícara mais fria. Avaliar se o relatório deve mostrar isso por ficha ou alternar quem começa. Seguem abertos: o limite da carga (3 °C) com o operador, calibrar `TEMPO` com medidas reais e a montagem cruzada.

---

## 2026-11-19 · rodada 9 · v2.8 → v2.9 (`index.html`)

**Origem → entrega.** `index.html` v2.8 (md5 df2bcaa2; arquivado como `versoes/index_v2-8_df2bcaa2.html`) → `index.html` v2.9 (md5 no commit). Commit local; **não enviado** ao GitHub.

**Oportunidades da rodada 8.** Comparar o tempo medido com a estimativa: segue aberta, porque depende de sessões reais da bancada, que não estão neste navegador. A montagem cruzada na dupla segue como ideia. Nesta rodada, a retomada (mapa, entrega, impressão livre digitada sem sair do campo) foi conferida e está sólida: sem mapa ao recarregar, sem ficha duplicada, texto preservado.

**Problema reproduzido (decisão).** Com os .alog importados, o relatório atribuía o resultado à mudança declarada mesmo quando os arquivos mostravam outra decisão de torra diferente. Cenário: A = OCR 349, B = OCR 350, "O que mudou" = "DROP mais tarde", preferência por B.
- v2.8: "Observação a favor de OCR 350… torrar OCR 350 de novo". "Como cheguei" registrava "não aplica — 1 decisão de torra", e "Manter" dizia "demais decisões iguais ao controle". Nada disso mencionava a carga (BT) 221 → 210 °C, visível só na linha "Torra A × B".
- Varredura dos 28 pares consecutivos reais (340→368): a carga difere ≥ 3 °C em 20 deles (até 17,5 °C). Gás e ar diferem em vários.

**Mudança aplicada.**
- `OCRAN.entradasDif(torra, mudanças)` separa as decisões de **entrada** que diferem (carga BT ≥ 3 °C, peso verde, valores de gás, passos de ar) dos resultados (1C, DROP, DTR, RoR). Os horários dos ajustes não contam, só os valores. Mostra só o passo diferente quando a sequência tem o mesmo tamanho. Se um dos arquivos só registrou a configuração inicial (`gasSemMudanca`, ex.: OCR 363), gás e ar não são comparados. Cada diferença sabe se aparece em "O que mudou" (palavras-chave `DECL`).
- Configuração: aviso "Os .alog mostram outra decisão de torra diferente…" com o botão "Acrescentar a 'O que mudou'" (52 px; o foco volta ao campo).
- `decide`: passo `nao-declarada`; a decisão ganha "Atenção: os .alog mostram também … fora de 'O que mudou' — o resultado vale para essas diferenças juntas… igualar ao controle". "Manter" lista os valores do **controle vigente** (A, ou B depois de adoção registrada). Declarar as diferenças aciona a regra já existente de isolar. O texto chega ao resumo ROAST_HISTORY, à nota .md e ao JSON.

**Evidência (tablet 768×1024, .alog reais).**
- Mesmo cenário, depois: aviso antes de travar; decisão com a frase de atenção; "Manter: carga (BT) como no controle: 221 °C"; passo `nao-declarada` "aplica". Nenhum dado de torra nas 6 telas de prova checadas.
- Ramo declarado (344 × 345, "corte de gás antes do DROP"): o botão acrescentou carga e ar e não repetiu o gás; o aviso sumiu; rascunho recuperado após recarregar; decisão "Isolar uma mudança…".
- Desfechos: diferença sem preferência e semelhança demonstrada com a frase. Adoção registrada mantém o controle B e "Manter" passa a usar os valores de B. Sem .alog, a decisão fica idêntica à da v2.8. 362 × 363: nada acusado.
- Exportações, Caderno, biblioteca, treino e demonstração ok; console sem erro novo.

**Próxima oportunidade.** A carga varia ≥ 3 °C em 20 de 28 pares reais: a maior parte dos A/B vai cair no aviso. Avaliar se o relatório deve mostrar a dispersão da carga entre as sessões (pista de que o pré-aquecimento não é repetível), e se 3 °C é o limite certo para o Atilla, com o operador. Seguem abertos: calibrar `TEMPO` com medidas reais e a montagem cruzada na dupla.

---

## 2026-11-19 · rodada 8 · v2.7 → v2.8 (`index.html`)

**Origem → entrega.** `index.html` v2.7 (md5 b73ad388; arquivado como `versoes/index_v2-7_b73ad388.html`) → `index.html` v2.8 (md5 no commit). O pedido repetiu o da rodada 7 (importação .alog, caminho A/B, relatório), que já estava entregue. A rodada atacou o que ficou em aberto lá: a meta de 30 min sem medida e o custo da dupla. Commit local; **não enviado** ao GitHub.

**Problema reproduzido.** (1) Os 30 min eram só estimativa (`TEMPO`). O app não media a bancada, e a sessão só A/B nem gravava a hora da revelação. Além disso, `desc.aguaEm` era apagada ao sortear um par novo. (2) A tabela de planos dizia "Comparação cega A/B · 25 min" também em dupla. Mas no revezamento a ficha do segundo avaliador pede um par novo e um relógio novo, o que dá ~47 min, sem aviso antes de começar nem na tela "Ficha travada".

**Mudança aplicada.**
- Tempo de bancada **medido**: `tempoBancada(s)` conta do plano travado (`criadaEm`) à revelação (`desc.reveladaEm`, novo, ou `tri.reveladoEm`), separando a parte até a água da parte da água à revelação (`desc.sorteios[].aguaEm`, novo, por par). Aparece no relatório (linha "Tempo de bancada", com a meta de 30 min: dentro ou X min acima), no resumo ROAST_HISTORY, no Histórico e no Caderno (coluna `min_bancada`). Sessão com mais de 2 h aparece como pausa longa e não conta como medida. Demonstração, sessões migradas e sessões antigas sem carimbos não mostram nada.
- Tabela de planos: com 2+ avaliadores mostra "A/B · 1 ficha" (25 min) e "A/B · k fichas". No revezamento, k pares e ~47 min; com preparador dedicado, o mesmo par e ~37 min. Abaixo da tabela, "Medido nas suas últimas comparações A/B" (até 5), para calibrar a estimativa com a bancada real.
- "Ficha travada": o custo da próxima ficha (mesmas xícaras ≈ +12 min; quem montou ou modo sozinho = par novo ≈ +22 min) e o tempo decorrido desde o plano travado.
- Dose exibida com as casas reais (8,25 g, antes 8,3).

**Evidência (navegador, tablet 768×1024).**
- .alog reais OCR 349/350 importados. A anotação longa de `beans` do 349 não virou nome. Rascunho recuperado após recarregar. Arquivo com `exec(...)` recusado sem alterar A/B.
- Tabela: solo 1 linha de 25 min. Revezamento Ana+Bruno: 1 ficha 25 min · 2 fichas 2 pares, 4 xícaras, 50 g, 47 min. Dedicado: 2 fichas, 1 par, 37 min.
- A/B solo completa: carimbos gravados (`sorteios[0].aguaEm`, `desc.reveladaEm`). Com carimbos ajustados a 31 min e água aos 6, o relatório mostra "31 min do plano travado à revelação (até a água 6 min · da água à revelação 25 min) · 1 par, 1 ficha · meta 30 min: 1 min acima". Resumo, Histórico, Caderno e "Medido…" coerentes (31 e 46 min); pausa de 3 h 10 rotulada e excluída.
- Dupla: "Ficha travada" com o custo da próxima ficha; modo sozinho com texto próprio. Backup → apagar → restaurar: carimbos e .alog preservados; sessão sem carimbos (formato v2.7) sem linha e sem erro. Biblioteca, treino, demonstração e exportações ok; console sem erro do app.

**Limites.** As medidas reais começam a existir quando o app for usado na bancada. Os números desta rodada são carimbos ajustados no teste, não cronometragem do usuário. O início conta a partir de "Travar plano e começar": se o plano for travado antes de moer, ou depois, a medida desloca.

**Próxima oportunidade.** Depois de 3 a 5 A/B reais, comparar "Medido" com `TEMPO` e ajustar a estimativa (ou usar a mediana medida na tabela). Se a dupla quiser duas fichas dentro de 30 min, avaliar a montagem cruzada: os dois pares montados ao mesmo tempo, cada um pelo outro, com um relógio só.

---

## 2026-11-19 · rodada 7 · v2.6 → v2.7 (`index.html`)

**Origem → entrega.** `index.html` v2.6 (md5 3bdd3036, igual ao publicado; arquivado como `versoes/index_v2-6_3bdd3036.html`) → `index.html` v2.7 (md5 no commit). Base: pedido do usuário e a proposta `docs/2026-11-19-importacao-alog-e-bancada.md` (outra sessão; mantida fora do commit). Commit local; **não enviado** ao GitHub.

**Problema.** (1) Os dados de torra eram digitados à mão, embora existam os `.alog` do Artisan. (2) O caminho padrão era o triângulo de 12 tríades e a semelhança subia o n sozinha para 39–44: dezenas de preparos para uma decisão de bancada de 30 min.

**Mudança aplicada.**
- `OCRALOG`: leitor próprio do literal Python do `.alog` (só dados; sem `eval`/`Function`; 6 MB, profundidade 40). Sugere OCR pelo nome do arquivo; café só com nome além do código; `title`/`beans` viram pistas, e anotações não viram nome. Extrai carga, TP, fim da secagem, 1C, DROP, total, desenvolvimento, DTR, RoR no 1C, pesos, perda (peso torrado 0 = ausente), cor e eventos de gás/ar com o texto e a unidade do Artisan. Cada valor tem origem: medido, marcado, Artisan, app, digitado. Avisos: lacunas, gás só com a configuração inicial (`gasSemMudanca`), conflitos de código.
- Configuração e relatório: importar A e B, prévia editável, "Aplicar". Arquivo inválido mostra o motivo e não altera nada. O rascunho da configuração sobrevive ao recarregar (`triangulo_ocr_v3_ui.draft`, só o resumo, sem curvas).
- Caminho padrão: "Comparação cega A/B (recomendado)", `mod: 'desc'`. O triângulo é confirmação, com planos curtos (6/9/12 levados ao múltiplo de k) e uma tabela de preparos, xícaras, café, tempo estimado e chance de detectar. A semelhança é opção avançada e não sobe mais o n. "Nova comparação" limita n a 12.
- Relatório: "O que percebi na xícara" (distinguir · descrição · preferência), "Quanto os dados sustentam" (tipo: Observação prática / Diferença detectada / Semelhança demonstrada / Inconclusivo / Sem conclusão) e "O que faço agora". Também tabela Torra A × B, diferenças notáveis e hipóteses com dados do `.alog` (associação, não causa). A próxima prova é proporcional (`proxAB`): A/B curta quando falta preferência ou o triângulo não concluiu; "Criar próximo A/B" herda o modo.
- Ajuda "Por quê?" começa pela A/B e pelo `.alog`.

**Evidência (navegador, tablet 768×1024; .alog reais de `Logs_OCR`).**
- OCR 344/345: valores da prévia iguais à leitura em Python (1C 10:00 · 205,5 °C; DROP 11:24 · 216,5 °C; DTR 12,3 %; 345: DTR 12,0 %, DROP 216,7 °C). O café ficou vazio (só OCR no nome). OCR 347: título "Torra OCR - Catuai Vermelho" vira pista; perda de 12,7 % (3,49 kg). OCR 348: `beans` com anotação longa marcada como anotação. OCR 363: aviso de gás só inicial. A partir de 31 arquivos, o parser deu o mesmo resultado que o `ast` do Python, sem conflito com o `computed` do Artisan.
- Recarregar com A/B importados restaura o rascunho. Arquivos `__import__`, `lambda`, HTML, vazio, `{}`, sem curva: recusados com o motivo, sem execução, A/B intactos. Um derivado sem DROP/1C mostra "ausente no arquivo", sem inventar.
- A/B sozinho: nenhuma pista de OCR da montagem até travar; retomada no passo 3 da ficha; ~33 toques do "Nova comparação" ao relatório. A/B em dupla: quem montou recebe posições novas; retomada no meio da ficha.
- Relatórios: A/B "Observação prática"; triângulo 5/6 "Diferença detectada" (p 0,018); 4/9 "Inconclusivo" (pd até 62 %, "não quer dizer iguais"). Backup (4 sessões, 83 KB) → apagar → restaurar: dados importados e eventos intactos. Exportações, Caderno, biblioteca, treino e demonstração sem erro.

**Limites.** Os tempos (25 min A/B; 6 tríades ≈ 1 h 27) são estimativa, não medida na bancada. Em dupla, a segunda ficha pede xícaras novas. "Peso verde 4/5 kg" pode ser a capacidade digitada.

**Próxima oportunidade.** Cronometrar uma A/B real na bancada e ajustar `TEMPO`. Avaliar se a dupla pode provar as mesmas xícaras quando há uma terceira pessoa montando, sem gastar o segundo par.

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
