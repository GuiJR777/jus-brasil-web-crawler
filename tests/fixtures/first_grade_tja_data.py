from models.parts import Parts
from models.process import Process
from models.process_moviment import ProcessMoviment


FIRST_PAGE_TJA_DATA = Process(
    classe='Procedimento Comum Cível',
    area='Cível',
    assunto='Dano Material',
    data_de_distribuicao='02/05/2018',
    juiz='José Cícero Alves da Silva',
    valor_da_acao=281178.42,
    partes_do_processo=Parts(
        advogados_autor=[
            'Vinicius Faria de Cerqueira'
        ],
        advogados_reu=[
            'Carlos Henrique de Mendonça Brandão',
            'Guilherme Freire Furtado',
            'Maria Eugênia Barreiros de Mello',
            'Vítor Reis de Araujo Carvalho'
        ],
        autor='José Carlos Cerqueira Souza Filho',
        reu='Cony Engenharia Ltda.',
    ),
    lista_das_movimentacoes=[
        ProcessMoviment(
            data='21/07/2023',
            details='Ato PublicadoRelação: 0450/2023\nData da Publicação: 24/07/2023\nNúmero do Diário: 3349'),
        ProcessMoviment(
            data='20/07/2023',
            details='Disponibilização no Diário da Justiça EletrônicoRelação: 0450/2023\nTeor do ato: Autos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Comum Cível Autor: José Carlos Cerqueira Souza Filho e outro Réu: Cony Engenharia Ltda. e outro ATO ORDINATÓRIO Em cumprimento ao disposto no Provimento nº 15/2019, da Corregedoria Geral da Justiça do Estado de Alagoas, fica(m) a(s) parte(s) ré intimada(s), na pessoa do seu advogado, para, no prazo de 15 (quinze) dias, providenciar(em) o recolhimento das custas processuais, sob pena de expedição de certidão ao FUNJURIS (Resolução TJ/AL nº 19/2007) para inscrição na divida ativa estadual, após o que será arquivado o processo. Ocorrendo o pagamento, devidamente atualizado, após a emissão da supracitada certidão de débito, deverá o interessado entregar a ficha de compensação bancária quitada na sede do FUNJURIS, que se responsabilizará pela devida baixa, além de oficiar à secretaria de onde se originou o débito acerca do referido pagamento (Resolução nº 19/2007, art. 33, § 6º). Maceió, 20 de julho de 2023 Marcelo Rodrigo Falcão Vieira Analista(escrivão substituto)\nAdvogados(s): Nelson Wilians Fratoni Rodrigues (OAB 9395AAL/), Carlos Henrique de Mendonça Brandão (OAB 6770AL /), Vinicius Faria de Cerqueira (OAB 9008/AL), Maria Eugênia Barreiros de Mello (OAB 14717AL/), Guilherme Freire Furtado (OAB 14781/AL), Vítor Reis de Araujo Carvalho (OAB 14928/AL)'),
        ProcessMoviment(
            data='20/07/2023',
            details='Ato ordinatório praticadoAutos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Comum Cível Autor: José Carlos Cerqueira Souza Filho e outro Réu: Cony Engenharia Ltda. e outro ATO ORDINATÓRIO Em cumprimento ao disposto no Provimento nº 15/2019, da Corregedoria Geral da Justiça do Estado de Alagoas, fica(m) a(s) parte(s) ré intimada(s), na pessoa do seu advogado, para, no prazo de 15 (quinze) dias, providenciar(em) o recolhimento das custas processuais, sob pena de expedição de certidão ao FUNJURIS (Resolução TJ/AL nº 19/2007) para inscrição na divida ativa estadual, após o que será arquivado o processo. Ocorrendo o pagamento, devidamente atualizado, após a emissão da supracitada certidão de débito, deverá o interessado entregar a ficha de compensação bancária quitada na sede do FUNJURIS, que se responsabilizará pela devida baixa, além de oficiar à secretaria de onde se originou o débito acerca do referido pagamento (Resolução nº 19/2007, art. 33, § 6º). Maceió, 20 de julho de 2023 Marcelo Rodrigo Falcão Vieira Analista(escrivão substituto)Vencimento:10/08/2023'),
        ProcessMoviment(
            data='20/07/2023',
            details='Devolvido CJU - Cálculo de Custas Finais RealizadoDevolvido CJU - Cálculo de Custas Finais Realizado'),
        ProcessMoviment(
            data='20/07/2023',
            details='Realizado cálculo de custas'),
        ProcessMoviment(
            data='21/07/2023',
            details='Ato PublicadoRelação: 0450/2023\nData da Publicação: 24/07/2023\nNúmero do Diário: 3349'),
        ProcessMoviment(
            data='20/07/2023',
            details='Disponibilização no Diário da Justiça EletrônicoRelação: 0450/2023\nTeor do ato: Autos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Comum Cível Autor: José Carlos Cerqueira Souza Filho e outro Réu: Cony Engenharia Ltda. e outro ATO ORDINATÓRIO Em cumprimento ao disposto no Provimento nº 15/2019, da Corregedoria Geral da Justiça do Estado de Alagoas, fica(m) a(s) parte(s) ré intimada(s), na pessoa do seu advogado, para, no prazo de 15 (quinze) dias, providenciar(em) o recolhimento das custas processuais, sob pena de expedição de certidão ao FUNJURIS (Resolução TJ/AL nº 19/2007) para inscrição na divida ativa estadual, após o que será arquivado o processo. Ocorrendo o pagamento, devidamente atualizado, após a emissão da supracitada certidão de débito, deverá o interessado entregar a ficha de compensação bancária quitada na sede do FUNJURIS, que se responsabilizará pela devida baixa, além de oficiar à secretaria de onde se originou o débito acerca do referido pagamento (Resolução nº 19/2007, art. 33, § 6º). Maceió, 20 de julho de 2023 Marcelo Rodrigo Falcão Vieira Analista(escrivão substituto)\nAdvogados(s): Nelson Wilians Fratoni Rodrigues (OAB 9395AAL/), Carlos Henrique de Mendonça Brandão (OAB 6770AL /), Vinicius Faria de Cerqueira (OAB 9008/AL), Maria Eugênia Barreiros de Mello (OAB 14717AL/), Guilherme Freire Furtado (OAB 14781/AL), Vítor Reis de Araujo Carvalho (OAB 14928/AL)'),
        ProcessMoviment(
            data='20/07/2023',
            details='Ato ordinatório praticadoAutos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Comum Cível Autor: José Carlos Cerqueira Souza Filho e outro Réu: Cony Engenharia Ltda. e outro ATO ORDINATÓRIO Em cumprimento ao disposto no Provimento nº 15/2019, da Corregedoria Geral da Justiça do Estado de Alagoas, fica(m) a(s) parte(s) ré intimada(s), na pessoa do seu advogado, para, no prazo de 15 (quinze) dias, providenciar(em) o recolhimento das custas processuais, sob pena de expedição de certidão ao FUNJURIS (Resolução TJ/AL nº 19/2007) para inscrição na divida ativa estadual, após o que será arquivado o processo. Ocorrendo o pagamento, devidamente atualizado, após a emissão da supracitada certidão de débito, deverá o interessado entregar a ficha de compensação bancária quitada na sede do FUNJURIS, que se responsabilizará pela devida baixa, além de oficiar à secretaria de onde se originou o débito acerca do referido pagamento (Resolução nº 19/2007, art. 33, § 6º). Maceió, 20 de julho de 2023 Marcelo Rodrigo Falcão Vieira Analista(escrivão substituto)Vencimento:10/08/2023'),
        ProcessMoviment(
            data='20/07/2023',
            details='Devolvido CJU - Cálculo de Custas Finais RealizadoDevolvido CJU - Cálculo de Custas Finais Realizado'),
        ProcessMoviment(
            data='20/07/2023',
            details='Realizado cálculo de custas'),
        ProcessMoviment(
            data='20/07/2023',
            details='Juntada de Documento'),
        ProcessMoviment(
            data='05/05/2023',
            details='Execução de Sentença IniciadaSeq.: 01 - Cumprimento de sentença'),
        ProcessMoviment(
            data='05/05/2023',
            details='Ato PublicadoRelação: 0282/2023\nData da Publicação: 08/05/2023\nNúmero do Diário: 3296'),
        ProcessMoviment(
            data='04/05/2023',
            details='Disponibilização no Diário da Justiça EletrônicoRelação: 0282/2023\nTeor do ato: Autos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Comum Cível Autor: José Carlos Cerqueira Souza Filho e outro Réu: Cony Engenharia Ltda. e outro ATO ORDINATÓRIO Em cumprimento ao Provimento nº 15/2019, da Corregedoria-Geral da Justiça do Estado de Alagoas, em virtude do retorno dos autos da instância superior, manifestem-se as partes, em 15 (quinze) dias, requerendo o que de direito. Maceió, 04 de maio de 2023 Marcelo Rodrigo Falcão Vieira Analista(escrivão substituto)\nAdvogados(s): Nelson Wilians Fratoni Rodrigues (OAB 9395A/AL), Carlos Henrique de Mendonça Brandão (OAB 6770/AL), Vinicius Faria de Cerqueira (OAB 9008/AL), Maria Eugênia Barreiros de Mello (OAB 14717/AL), Guilherme Freire Furtado (OAB 14781/AL), Vítor Reis de Araujo Carvalho (OAB 14928/AL)'),
        ProcessMoviment(
            data='04/05/2023',
            details='Recebido pela Contadoria UNIFICADA'),
        ProcessMoviment(
            data='04/05/2023',
            details='Ato Ordinatório - Artigo 162, §4º, CPCAto Ordinatório- Remessa à contadoria'),
        ProcessMoviment(
            data='04/05/2023',
            details='Ato ordinatório praticadoAutos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Comum Cível Autor: José Carlos Cerqueira Souza Filho e outro Réu: Cony Engenharia Ltda. e outro ATO ORDINATÓRIO Em cumprimento ao Provimento nº 15/2019, da Corregedoria-Geral da Justiça do Estado de Alagoas, em virtude do retorno dos autos da instância superior, manifestem-se as partes, em 15 (quinze) dias, requerendo o que de direito. Maceió, 04 de maio de 2023 Marcelo Rodrigo Falcão Vieira Analista(escrivão substituto)Vencimento:25/05/2023'),
        ProcessMoviment(
            data='03/05/2023',
            details='Transitado em Julgado'),
        ProcessMoviment(
            data='03/05/2023',
            details='Recebimento da Instância Superior -  Altera situação para "Julgado"'),
        ProcessMoviment(
            data='26/04/2023',
            details='Recebido recurso eletrônicoData do julgamento: 07/10/2021\nTrânsito em julgado: \nTipo de julgamento: Acórdão\nDecisão: à unanimidade de votos, em CONHECER de ambos os recursos de Apelação Cível; e, no mérito, por idêntica votação, NEGAR-LHES PROVIMENTO, mantendo incólume a Sentença proferida pelo Juízo de Direito de Primeiro Grau. Acordam, ainda, em majorar os honorários advocatícios sucumbenciais para 17% sobre o valor da condenação, nos termos do voto do Relator. \nSituação do provimento: \nRelator: Des. Otávio Leão Praxedes'),
        ProcessMoviment(
            data='22/02/2021',
            details='Remetido recurso eletrônico ao Tribunal de Justiça/Turma de recurso'),
        ProcessMoviment(
            data='10/02/2021',
            details='Juntada de DocumentoNº Protocolo: WMAC.21.70031538-2\nTipo da Petição: Contrarrazões\nData: 10/02/2021 19:27'),
        ProcessMoviment(
            data='06/01/2021',
            details='Ato PublicadoRelação :0003/2021\nData da Publicação: 21/01/2021\nNúmero do Diário: 2738'),
        ProcessMoviment(
            data='06/01/2021',
            details='Ato PublicadoRelação :0003/2021\nData da Publicação: 21/01/2021\nNúmero do Diário: 2738'),
        ProcessMoviment(
            data='06/01/2021',
            details='Ato PublicadoRelação :0003/2021\nData da Publicação: 21/01/2021\nNúmero do Diário: 2738'),
        ProcessMoviment(
            data='06/01/2021',
            details='Ato PublicadoRelação :0003/2021\nData da Publicação: 21/01/2021\nNúmero do Diário: 2738'),
        ProcessMoviment(
            data='06/01/2021',
            details='Ato PublicadoRelação :0003/2021\nData da Publicação: 21/01/2021\nNúmero do Diário: 2738'),
        ProcessMoviment(
            data='06/01/2021',
            details='Ato PublicadoRelação :0003/2021\nData da Publicação: 21/01/2021\nNúmero do Diário: 2738'),
        ProcessMoviment(
            data='05/01/2021',
            details='Disponibilização no Diário da Justiça EletrônicoRelação: 0003/2021\nTeor do ato: Ato Ordinatório: Interposto recurso de apelação pelos réus (Banco do Brasil e Cony Engenharia), intime-se a parte recorrida para apresentar contrarrazões, no prazo de 15 (quinze) dias, conforme o art. 1010,§ 1º do CPC. Se apresentada Apelação Adesiva pela parte recorrida (art.997, §2º do CPC), intime-se a parte contrária para contrarrazões, no prazo de 15 (quinze) dias, nos termos do Art. 1010, §2º do CPC. Caso as contrarrazões do recurso principal ou do adesivo ventilem matérias elencadas no art.1009, §1º do CPC, intime-se o recorrente para se manifestar sobre elas no prazo de 15(quinze) dias, conforme o art. 1009, § 2º, do CPC. Após as providências acima, remetam-se os autos ao Egrégio Tribunal de Justiça. Maceió, 04 de janeiro de 2021. Fernanda Patrícia Belo Marques Técnico Judiciário\nAdvogados(s): Carlos Henrique de Mendonça Brandão (OAB 6770/AL), Vinicius Faria de Cerqueira (OAB 9008/AL), Nelson Wilians Fratoni Rodrigues (OAB 9395A/AL), Maria Eugênia Barreiros de Mello (OAB 14717/AL), Guilherme Freire Furtado (OAB 14781/AL), Vítor Reis de Araujo Carvalho (OAB 14928/AL)'),
        ProcessMoviment(
            data='04/01/2021',
            details='Ato Ordinatório - Artigo 162, §4º, CPCAto Ordinatório: Interposto recurso de apelação pelos réus (Banco do Brasil e Cony Engenharia), intime-se a parte recorrida para apresentar contrarrazões, no prazo de 15 (quinze) dias, conforme o art. 1010,§ 1º do CPC. Se apresentada Apelação Adesiva pela parte recorrida (art.997, §2º do CPC), intime-se a parte contrária para contrarrazões, no prazo de 15 (quinze) dias, nos termos do Art. 1010, §2º do CPC. Caso as contrarrazões do recurso principal ou do adesivo ventilem matérias elencadas no art.1009, §1º do CPC, intime-se o recorrente para se manifestar sobre elas no prazo de 15(quinze) dias, conforme o art. 1009, § 2º, do CPC. Após as providências acima, remetam-se os autos ao Egrégio Tribunal de Justiça. Maceió, 04 de janeiro de 2021. Fernanda Patrícia Belo Marques Técnico Judiciário'),
        ProcessMoviment(
            data='18/12/2020',
            details='Juntada de DocumentoNº Protocolo: WMAC.20.70269584-0\nTipo da Petição: Juntada de Instrumento de Procuração\nData: 18/12/2020 17:23'),
        ProcessMoviment(
            data='18/12/2020',
            details='Juntada de DocumentoNº Protocolo: WMAC.20.70269581-5\nTipo da Petição: Recurso de Apelação\nData: 18/12/2020 17:18'),
        ProcessMoviment(
            data='15/12/2020',
            details='Juntada de DocumentoNº Protocolo: WMAC.20.70265228-8\nTipo da Petição: Recurso de Apelação\nData: 15/12/2020 13:26'),
        ProcessMoviment(
            data='24/11/2020',
            details='Ato PublicadoRelação :0912/2020\nData da Publicação: 25/11/2020\nNúmero do Diário: 2711'),
        ProcessMoviment(
            data='24/11/2020',
            details='Ato PublicadoRelação :0912/2020\nData da Publicação: 25/11/2020\nNúmero do Diário: 2711'),
        ProcessMoviment(
            data='24/11/2020',
            details='Ato PublicadoRelação :0912/2020\nData da Publicação: 25/11/2020\nNúmero do Diário: 2711'),
        ProcessMoviment(
            data='24/11/2020',
            details='Ato PublicadoRelação :0912/2020\nData da Publicação: 25/11/2020\nNúmero do Diário: 2711'),
        ProcessMoviment(
            data='23/11/2020',
            details='Disponibilização no Diário da Justiça EletrônicoRelação: 0912/2020\nTeor do ato: Forte nessas razões, JULGO PARCIALMENTE PROCEDENTES os pedidos da proemial, julgando extinto o processo com resolução de mérito, nos termos do art. 487, inciso I, do Estatuto Processual emergente, para o fim de CONDENAR AS DEMANDADAS, solidariamente: a) a ressarcir os danos materiais promovidos (lucros cessantes), cujo valor fixo em R$ 1.500,00 (três mil e quinhentos reais), por cada mês de atraso na entrega do imóvel , a incidir desde o dia 1 de agosto de 2017 até a data da efetiva entrega do imóvel, a ser apurada na fase de liquidação da sentença. Ressalto que esses valores deverão ser atualizados monetariamente pelo INPC desde a data em que cada aluguel seria devido, e acrescidos de juros de mora de 1% (um por cento) ao mês, contados da citação (art. 405 do Código Substantivo Civil). Para aqueles que venceram após a data da propositura da demanda, o juros de mora deverá incidir a partir da data de cada inadimplemento, para obstar o enriquecimento sem causa; b) em donos morais de R$ 5.000,00 (cinco mil reais), com juros de mora de 1% (um por cento) ao mês, a partir do dia 1 de agosto de 2017 (art. 397). Correção monetária, pelo INPC, desde a data do arbitramento; c) determino a substituição do índice INCC pelo IGP-M, a partir de 01 de agosto de 2017, e, como colorário, a devolução dos valores pagos a maior, com suas respectivas atualizações, nas mesmas condições do item a, deste dispositivo. Rejeito o pedido de restituição em dobro, por não vislumbrar má-fé dos beneficiários dos pagamentos indevidos. Oportunamente, condeno as demandada ao pagamento das custas e despesas processuais e dos honorários do advogado da parte adversa, que fixo, nos termos do art. 85, §2º, do Código de Processo Civil, e considerada a complexidade da demanda e as intervenções que exigiu, em 15% (quinze por cento) sobre o valor atualizado da condenação. Por fim, de modo a evitar o ajuizamento de embargos de declaração meramente protelatórios, registre-se que, ficam preteridas as demais alegações, por incompatíveis com a linha de raciocínio adotada, observando que os pedidos de ambas as partes foram apreciados nos limites em que foram formulados. Com efeito, ficam as partes advertidas, desde logo, que a oposição de embargos de declaração fora das hipóteses legais e/ou com postulação meramente infringente lhes sujeitará a imposição da multa prevista pelo artigo 1026, §2º, do Código de Processo Civil. Publique-se. Registre-se. Intimem-se.\nAdvogados(s): Orlando de Moura Cavalcante Neto (OAB 7313/AL), Thiago Maia Nobre Rocha (OAB 6213/AL), Vinicius Faria de Cerqueira (OAB 9008/AL), Marcus Vinicius Cavalcante Lins Filho (OAB 10871/AL)'),
        ProcessMoviment(
            data='23/11/2020',
            details='Julgado procedente em parte do pedidoForte nessas razões, JULGO PARCIALMENTE PROCEDENTES os pedidos da proemial, julgando extinto o processo com resolução de mérito, nos termos do art. 487, inciso I, do Estatuto Processual emergente, para o fim de CONDENAR AS DEMANDADAS, solidariamente: a) a ressarcir os danos materiais promovidos (lucros cessantes), cujo valor fixo em R$ 1.500,00 (três mil e quinhentos reais), por cada mês de atraso na entrega do imóvel , a incidir desde o dia 1 de agosto de 2017 até a data da efetiva entrega do imóvel, a ser apurada na fase de liquidação da sentença. Ressalto que esses valores deverão ser atualizados monetariamente pelo INPC desde a data em que cada aluguel seria devido, e acrescidos de juros de mora de 1% (um por cento) ao mês, contados da citação (art. 405 do Código Substantivo Civil). Para aqueles que venceram após a data da propositura da demanda, o juros de mora deverá incidir a partir da data de cada inadimplemento, para obstar o enriquecimento sem causa; b) em donos morais de R$ 5.000,00 (cinco mil reais), com juros de mora de 1% (um por cento) ao mês, a partir do dia 1 de agosto de 2017 (art. 397). Correção monetária, pelo INPC, desde a data do arbitramento; c) determino a substituição do índice INCC pelo IGP-M, a partir de 01 de agosto de 2017, e, como colorário, a devolução dos valores pagos a maior, com suas respectivas atualizações, nas mesmas condições do item a, deste dispositivo. Rejeito o pedido de restituição em dobro, por não vislumbrar má-fé dos beneficiários dos pagamentos indevidos. Oportunamente, condeno as demandada ao pagamento das custas e despesas processuais e dos honorários do advogado da parte adversa, que fixo, nos termos do art. 85, §2º, do Código de Processo Civil, e considerada a complexidade da demanda e as intervenções que exigiu, em 15% (quinze por cento) sobre o valor atualizado da condenação. Por fim, de modo a evitar o ajuizamento de embargos de declaração meramente protelatórios, registre-se que, ficam preteridas as demais alegações, por incompatíveis com a linha de raciocínio adotada, observando que os pedidos de ambas as partes foram apreciados nos limites em que foram formulados. Com efeito, ficam as partes advertidas, desde logo, que a oposição de embargos de declaração fora das hipóteses legais e/ou com postulação meramente infringente lhes sujeitará a imposição da multa prevista pelo artigo 1026, §2º, do Código de Processo Civil. Publique-se. Registre-se. Intimem-se.Vencimento:16/12/2020'),
        ProcessMoviment(
            data='23/09/2020',
            details='Conclusos'),
        ProcessMoviment(
            data='16/08/2020',
            details='Visto em AutoinspeçãoDespacho Visto em Autoinspeção'),
        ProcessMoviment(
            data='11/05/2020',
            details='Juntada de DocumentoNº Protocolo: WMAC.20.70092549-0\nTipo da Petição: Pedido de Andamento do proc./sent./decisões/desp.\nData: 11/05/2020 13:28'),
        ProcessMoviment(
            data='10/12/2019',
            details='Conclusos'),
        ProcessMoviment(
            data='11/11/2019',
            details='Despacho de Mero ExpedienteDESPACHO Compulsando detidamente o feito, verifico que este inclui-se nos processos com prioridade de impulsionamento, consoante recomendação exarada pelo Conselho Nacional de Justiça, a qual determina a priorização de andamento das demandas paralisadas há mais de 100 (dias). Destarte, considerando que cada uma desses processos exige análise acurada por este magistrado a fim de que lhe seja dado efetivo provimento, determino a conclusão de todos os autos que se amoldem à hipótese alhures delineada - de competência do gabinete - para análise e devido impulsionamento, este especificamente, na fila concluso - impulso ao feito. Cumpra-se. Maceió(AL), 11 de novembro de 2019. José Cícero Alves da Silva Juiz de Direito'),
        ProcessMoviment(
            data='12/07/2019',
            details='Juntada de PetiçãoNº Protocolo: WMAC.19.70150828-9\nTipo da Petição: Petição\nData: 11/07/2019 23:50'),
        ProcessMoviment(
            data='12/02/2019',
            details='Juntada de PetiçãoNº Protocolo: WMAC.19.70034823-7\nTipo da Petição: Petição\nData: 12/02/2019 14:58'),
        ProcessMoviment(
            data='11/02/2019',
            details='Juntada de PetiçãoNº Protocolo: WMAC.19.70032532-6\nTipo da Petição: Petição\nData: 11/02/2019 09:13'),
        ProcessMoviment(
            data='06/12/2018',
            details='Conclusos'),
        ProcessMoviment(
            data='05/12/2018',
            details='Juntada de PetiçãoNº Protocolo: WMAC.18.70259903-1\nTipo da Petição: Petição\nData: 05/12/2018 16:46'),
        ProcessMoviment(
            data='29/11/2018',
            details='Juntada de PetiçãoNº Protocolo: WMAC.18.70255192-6\nTipo da Petição: Petição\nData: 29/11/2018 15:07'),
        ProcessMoviment(
            data='28/11/2018',
            details='Ato PublicadoRelação :0499/2018\nData da Publicação: 29/11/2018\nNúmero do Diário: 2233'),
        ProcessMoviment(
            data='27/11/2018',
            details='Disponibilização no Diário da Justiça EletrônicoRelação: 0499/2018\nTeor do ato: ATO ORDINATÓRIO Em cumprimento ao disposto no art. 152,VI do CPC, procedo à intimação das partes para especificarem e justificarem as provas que ainda pretendem produzir, fundamentamente, pelo prazo comum de 5(cinco) dias. Maceió, 27 de novembro de 2018\nAdvogados(s): Orlando de Moura Cavalcante Neto (OAB 7313/AL), Thiago Maia Nobre Rocha (OAB 6213/AL), Vinicius Faria de Cerqueira (OAB 9008/AL), Rafael Sganzerla Durand (OAB 10132A/AL), Marcus Vinicius Cavalcante Lins Filho (OAB 10871/AL)'),
        ProcessMoviment(
            data='27/11/2018',
            details='Ato ordinatório praticadoATO ORDINATÓRIO Em cumprimento ao disposto no art. 152,VI do CPC, procedo à intimação das partes para especificarem e justificarem as provas que ainda pretendem produzir, fundamentamente, pelo prazo comum de 5(cinco) dias. Maceió, 27 de novembro de 2018'),
        ProcessMoviment(
            data='26/11/2018',
            details='Juntada de DocumentoNº Protocolo: WMAC.18.70251514-8\nTipo da Petição: Impugnação à Contestação\nData: 26/11/2018 15:37'),
        ProcessMoviment(
            data='26/11/2018',
            details='Juntada de DocumentoNº Protocolo: WMAC.18.70251511-3\nTipo da Petição: Impugnação à Contestação\nData: 26/11/2018 15:35'),
        ProcessMoviment(
            data='09/11/2018',
            details='Ato PublicadoRelação :0456/2018\nData da Publicação: 12/11/2018\nNúmero do Diário: 2222'),
        ProcessMoviment(
            data='08/11/2018',
            details='Disponibilização no Diário da Justiça EletrônicoRelação: 0456/2018\nTeor do ato: Autos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Ordinário Autor: José Carlos Cerqueira Souza Filho e outro Réu: Conaço Engenharia Ltda. e outro ATO ORDINATÓRIO Intimo a parte autora a apresentar, querendo, no prazo de 15 (quinze) dias, impugnação às contestações. Maceió, 06 de novembro de 2018 Hallph Sá de Araújo Analista Judiciário\nAdvogados(s): Vinicius Faria de Cerqueira (OAB 9008/AL)'),
        ProcessMoviment(
            data='06/11/2018',
            details='Ato ordinatório praticadoAutos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Ordinário Autor: José Carlos Cerqueira Souza Filho e outro Réu: Conaço Engenharia Ltda. e outro ATO ORDINATÓRIO Intimo a parte autora a apresentar, querendo, no prazo de 15 (quinze) dias, impugnação às contestações. Maceió, 06 de novembro de 2018 Hallph Sá de Araújo Analista JudiciárioVencimento:29/11/2018'),
        ProcessMoviment(
            data='16/10/2018',
            details='Juntada de DocumentosNº Protocolo: WMAC.18.70221617-5\nTipo da Petição: Contestação\nData: 16/10/2018 14:43'),
        ProcessMoviment(
            data='10/10/2018',
            details='Juntada de DocumentosNº Protocolo: WMAC.18.70218154-1\nTipo da Petição: Contestação\nData: 10/10/2018 14:04'),
        ProcessMoviment(
            data='24/09/2018',
            details='Juntada de Documento'),
        ProcessMoviment(
            data='24/09/2018',
            details='Juntada de Documento'),
        ProcessMoviment(
            data='24/09/2018',
            details='Audiência RealizadaAssentada - Genérico'),
        ProcessMoviment(
            data='24/09/2018',
            details='Juntada de PetiçãoNº Protocolo: WMAC.18.70203989-3\nTipo da Petição: Petição\nData: 24/09/2018 10:09'),
        ProcessMoviment(
            data='21/09/2018',
            details='Juntada de PetiçãoNº Protocolo: WMAC.18.70203544-8\nTipo da Petição: Petição\nData: 21/09/2018 18:07'),
        ProcessMoviment(
            data='21/09/2018',
            details='Juntada de PetiçãoNº Protocolo: WMAC.18.70203528-6\nTipo da Petição: Petição\nData: 21/09/2018 17:42'),
        ProcessMoviment(
            data='21/09/2018',
            details='Juntada de PetiçãoNº Protocolo: WMAC.18.70203260-0\nTipo da Petição: Petição\nData: 21/09/2018 13:58'),
        ProcessMoviment(
            data='20/09/2018',
            details='Visto em correiçãoDESPACHO VISTO EM CORREIÇÃO'),
        ProcessMoviment(
            data='06/06/2018',
            details='Juntada de AR - CumpridoEm 06  de  junho  de  2018 é juntado a estes autos o aviso de recebimento (AR803969759TJ - Cumprido), referente  ao  ofício  n. 0710802-55.2018.8.02.0001-0002, emitido para Conaço Engenharia Ltda.. Usuário:'),
        ProcessMoviment(
            data='06/06/2018',
            details='Juntada de AR - CumpridoEm 06  de  junho  de  2018 é juntado a estes autos o aviso de recebimento (AR803969745TJ - Cumprido), referente  ao  ofício  n. 0710802-55.2018.8.02.0001-0001, emitido para Banco do Brasil S A. Usuário:'),
        ProcessMoviment(
            data='15/05/2018',
            details='Ato PublicadoRelação :0220/2018\nData da Publicação: 16/05/2018\nNúmero do Diário: 2105'),
        ProcessMoviment(
            data='15/05/2018',
            details='Ato PublicadoRelação :0220/2018\nData da Publicação: 16/05/2018\nNúmero do Diário: 2105'),
        ProcessMoviment(
            data='11/05/2018',
            details='Disponibilização no Diário da Justiça EletrônicoRelação: 0220/2018\nTeor do ato: DECISÃOTrata-se de ação ordinária de indenização por danos morais e materias c/c obrigação de fazer c/c declaração de nulidade de contrato de financiamento bancário c/c pedido de tutela antecipada proposta por JOSÉ CARLOS CERQUEIRA SOUZA FILHO e LIVIA NASCIMENTO DA ROCHA, qualificados na inicial, em face de a CONY ENGENHARIA LTDA. e BANCO DO BRASIL, igualmente qualificados.Narra a exordial que os autores adquiriram o apartamento residencial de nº 502, da Torre I, do Empreendimento Residencial Dellavia Park Club, situado na Ladeira Murilo Monteiro Valente, n.º 375, no bairro do Barro Duro, Maceió/AL, cuja vendedora foi a ré CONY ENGENHARIA LTDA., pelo valor de R$ 232.000,00 (duzentos e trinta e dois mil reais).Segue narrando que o instrumento celebrado em 02/12/2013 previa a entrega do imóvel no prazo de 36 (trinta e seis) meses contados do início da obra, sendo admitida uma tolerância de no máximo 18 (dezoito) meses. Dentro dessa perspectiva, foi prometido que a obra seria iniciada em no máximo 60 (sessenta) dias da assinatura do contrato, ou seja seria iniciada em 02/02/2014 com previsão de entrega para 02/02/2017, porém, até a presente data a obra não foi concluída.Aduz que os demandantes ainda sendo cobrados ilegalmente pelo BANCO DO BRASIL, também réu da ação, numa suposta "taxa de obra", que decorre de financiamento bancário.Requer, em sede de tutela de urgência, que seja determinado ao BANCO DO BRASIL a SUSPENSÃO da cobrança de taxa de Obra.É o relatório. Decido.Ab initio, concedo aos Demandantes as benesses da assistência judiciária gratuita, em respeito as determinações contidas no art. 98 e art. 99 da Lei nº. 13.105/2015 (Código de Processo Civil - CPC/2015).O Código de Defesa do Consumidor, em seu art. 6.º, VIII, assegura como direito básico do consumidor a facilitação da defesa de seus direitos, inclusive com a inversão do ônus da prova, a seu favor, quando, a critério do juiz, for verossímil a alegação ou quando for ele hipossuficiente, segundo as regras ordinárias de experiência. Busca-se, assim assegurar a igualdade material.Em que pese bastar apenas um dos requisitos para a inversão, o caso em tela preenche as duas condições. Assim com fulcro no art. 6.º, VIII, do CDC DECIDO POR INVERTER O ÔNUS DA PROVA.Passo a apreciar o pedido de tutela provisória de urgência.Segundo o art. 300 do CPC/15, a tutela de urgência será concedida quando houver elementos que evidenciem a probabilidade do direito e o perigo de dano ou o risco ao resultado útil do processo. O dispositivo deixa evidentes os requisitos da tutela antecipada de urgência, quais sejam, a probabilidade do direito, doutrinariamente conhecida como fumus boni iuris, e o perigo de dano ou risco ao resultado útil do processo, chamado periculum in mora.Nesse trilhar, importa esclarecer que a tutela de urgência antecipada se funda em um Juízo de cognição sumária, de modo que a medida, quando concedida, será precária, haja vista ser fundamental a necessidade de ser reversível (300, §3º, do CPC/2015).Portanto, a antecipação provisória dos efeitos finais da tutela definitiva, permite o gozo antecipado e imediato dos efeitos próprios da tutela definitiva pretendida, mas não se funda em um juízo de valor exauriente, de modo que pode ser desconstituída a qualquer tempo.Nessa esteira de pensamento, passa-se a analisar o caso concreto e o preenchimento dos requisitos necessários à concessão da tutela provisória pretendida.No caso em tela, pretende a parte autora a suspensão da cobrança da "taxa de obra", em razão do suposto descumprimento contratual por parte da demandada no tocante ao prazo estabelecido para a entrega do imóvel.Conforme se extrai dos autos, as partes firmaram um contrato de compra e venda de um apartamento, tendo sido estipulada o prazo para sua entrega em 36 (trinta e seis) meses, com um prazo de tolerância de 18 (dezoito) meses, consoante cláusula quarta do contrato (fls.39). Logo o prazo final para entrega do imóvel se encerra em 02/08/2018, levando em consideração o prazo de tolerância estabelecido no contrato.É cediço que a taxa de evolução de obra é devida desde a aprovação do financiamento até o término da obra.\xa0Portanto, se a obra atrasar, é devido o pagamento da referida taxa ao banco que financiou o imóvel, no caso, o Banco do Brasil, até a sua conclusão. Sendo certo que ocorrendo a mora da construtora requerida em relação à entrega do imóvel, a parte autora não pode ser penalizada com o pagamento de tal encargo.\xa0No entanto, no caso em deslinde, ainda não houve mora da construtora, haja vista que ainda não fora encerrado o prazo estimado para entrega do imóvel. Nesse ponto impende destacar que é legal a cláusula contratual que prevê a prorrogação do prazo razoável para entrega do imóvel, considerando o princípio pacta sunt servanda.\xa0Desta feita, verifica-se a ausência de probabilidade do direito da parte autora, haja vista que, consoante dito alhures, a taxa de evolução de obra é devida até a conclusão da obra, bem como que não houve mora por parte da construtora demandada, haja vista que não houve, ainda, atraso na entrega do imóvel, tendo em vista a cláusula que prevê prazo de tolerância para entrega do imóvel.Ante o exposto, por considerar ausente a probabilidade do direito (art. 300 do CPC/15), INDEFIRO o pedido de tutela de urgência requestado.Inclua-se o feito em pauta de audiência de conciliação. Cite-se a parte ré eintime-a desta decisão, bem como para que compareça à audiência na data designada pelo Cartório, o que deve ser feito com antecedência mínima de 20 dias.Intime-se os autores por advogado constituído (art. 334, §3º, CPC/15).Deverá a parte ré ser advertida da possibilidade do art. 334, §5º, bem como do termo inicial do prazo de contestação (art. 335).Fiquem as partes advertidas, ainda, de que o não comparecimento injustificado à audiência de conciliação é considerado ato atentatório à dignidade da justiça e será sancionado com multa de até dois por cento da vantagem econômica pretendida ou do valor da causa (art. 334, §8º).Publique-se. Intime-seMaceió, 10 de maio de 2018.Henrique Gomes de Barros TeixeiraJuiz de Direito\nAdvogados(s): Vinicius Faria de Cerqueira (OAB 9008/AL)'),
        ProcessMoviment(
            data='11/05/2018',
            details='Disponibilização no Diário da Justiça EletrônicoRelação: 0220/2018\nTeor do ato: Conciliação\nData: 24/09/2018 Hora 14:00\nLocal: Sala de Audiência\nSituacão: Pendente\nAdvogados(s): Vinicius Faria de Cerqueira (OAB 9008/AL)'),
        ProcessMoviment(
            data='11/05/2018',
            details='Carta ExpedidaAR DIGITAL - Citação e Intimação - Audiência de Instrução e Julgamento - Juizado'),
        ProcessMoviment(
            data='11/05/2018',
            details='Carta ExpedidaAR DIGITAL - Citação e Intimação - Audiência de Instrução e Julgamento - Juizado'),
        ProcessMoviment(
            data='11/05/2018',
            details='Audiência DesignadaConciliação\nData: 24/09/2018 Hora 14:00\nLocal: Sala de Audiência\nSituacão: Realizada'),
        ProcessMoviment(
            data='10/05/2018',
            details='Não Concedida a Antecipação de tutelaDECISÃOTrata-se de ação ordinária de indenização por danos morais e materias c/c obrigação de fazer c/c declaração de nulidade de contrato de financiamento bancário c/c pedido de tutela antecipada proposta por JOSÉ CARLOS CERQUEIRA SOUZA FILHO e LIVIA NASCIMENTO DA ROCHA, qualificados na inicial, em face de a CONY ENGENHARIA LTDA. e BANCO DO BRASIL, igualmente qualificados.Narra a exordial que os autores adquiriram o apartamento residencial de nº 502, da Torre I, do Empreendimento Residencial Dellavia Park Club, situado na Ladeira Murilo Monteiro Valente, n.º 375, no bairro do Barro Duro, Maceió/AL, cuja vendedora foi a ré CONY ENGENHARIA LTDA., pelo valor de R$ 232.000,00 (duzentos e trinta e dois mil reais).Segue narrando que o instrumento celebrado em 02/12/2013 previa a entrega do imóvel no prazo de 36 (trinta e seis) meses contados do início da obra, sendo admitida uma tolerância de no máximo 18 (dezoito) meses. Dentro dessa perspectiva, foi prometido que a obra seria iniciada em no máximo 60 (sessenta) dias da assinatura do contrato, ou seja seria iniciada em 02/02/2014 com previsão de entrega para 02/02/2017, porém, até a presente data a obra não foi concluída.Aduz que os demandantes ainda sendo cobrados ilegalmente pelo BANCO DO BRASIL, também réu da ação, numa suposta "taxa de obra", que decorre de financiamento bancário.Requer, em sede de tutela de urgência, que seja determinado ao BANCO DO BRASIL a SUSPENSÃO da cobrança de taxa de Obra.É o relatório. Decido.Ab initio, concedo aos Demandantes as benesses da assistência judiciária gratuita, em respeito as determinações contidas no art. 98 e art. 99 da Lei nº. 13.105/2015 (Código de Processo Civil - CPC/2015).O Código de Defesa do Consumidor, em seu art. 6.º, VIII, assegura como direito básico do consumidor a facilitação da defesa de seus direitos, inclusive com a inversão do ônus da prova, a seu favor, quando, a critério do juiz, for verossímil a alegação ou quando for ele hipossuficiente, segundo as regras ordinárias de experiência. Busca-se, assim assegurar a igualdade material.Em que pese bastar apenas um dos requisitos para a inversão, o caso em tela preenche as duas condições. Assim com fulcro no art. 6.º, VIII, do CDC DECIDO POR INVERTER O ÔNUS DA PROVA.Passo a apreciar o pedido de tutela provisória de urgência.Segundo o art. 300 do CPC/15, a tutela de urgência será concedida quando houver elementos que evidenciem a probabilidade do direito e o perigo de dano ou o risco ao resultado útil do processo. O dispositivo deixa evidentes os requisitos da tutela antecipada de urgência, quais sejam, a probabilidade do direito, doutrinariamente conhecida como fumus boni iuris, e o perigo de dano ou risco ao resultado útil do processo, chamado periculum in mora.Nesse trilhar, importa esclarecer que a tutela de urgência antecipada se funda em um Juízo de cognição sumária, de modo que a medida, quando concedida, será precária, haja vista ser fundamental a necessidade de ser reversível (300, §3º, do CPC/2015).Portanto, a antecipação provisória dos efeitos finais da tutela definitiva, permite o gozo antecipado e imediato dos efeitos próprios da tutela definitiva pretendida, mas não se funda em um juízo de valor exauriente, de modo que pode ser desconstituída a qualquer tempo.Nessa esteira de pensamento, passa-se a analisar o caso concreto e o preenchimento dos requisitos necessários à concessão da tutela provisória pretendida.No caso em tela, pretende a parte autora a suspensão da cobrança da "taxa de obra", em razão do suposto descumprimento contratual por parte da demandada no tocante ao prazo estabelecido para a entrega do imóvel.Conforme se extrai dos autos, as partes firmaram um contrato de compra e venda de um apartamento, tendo sido estipulada o prazo para sua entrega em 36 (trinta e seis) meses, com um prazo de tolerância de 18 (dezoito) meses, consoante cláusula quarta do contrato (fls.39). Logo o prazo final para entrega do imóvel se encerra em 02/08/2018, levando em consideração o prazo de tolerância estabelecido no contrato.É cediço que a taxa de evolução de obra é devida desde a aprovação do financiamento até o término da obra.\xa0Portanto, se a obra atrasar, é devido o pagamento da referida taxa ao banco que financiou o imóvel, no caso, o Banco do Brasil, até a sua conclusão. Sendo certo que ocorrendo a mora da construtora requerida em relação à entrega do imóvel, a parte autora não pode ser penalizada com o pagamento de tal encargo.\xa0No entanto, no caso em deslinde, ainda não houve mora da construtora, haja vista que ainda não fora encerrado o prazo estimado para entrega do imóvel. Nesse ponto impende destacar que é legal a cláusula contratual que prevê a prorrogação do prazo razoável para entrega do imóvel, considerando o princípio pacta sunt servanda.\xa0Desta feita, verifica-se a ausência de probabilidade do direito da parte autora, haja vista que, consoante dito alhures, a taxa de evolução de obra é devida até a conclusão da obra, bem como que não houve mora por parte da construtora demandada, haja vista que não houve, ainda, atraso na entrega do imóvel, tendo em vista a cláusula que prevê prazo de tolerância para entrega do imóvel.Ante o exposto, por considerar ausente a probabilidade do direito (art. 300 do CPC/15), INDEFIRO o pedido de tutela de urgência requestado.Inclua-se o feito em pauta de audiência de conciliação. Cite-se a parte ré eintime-a desta decisão, bem como para que compareça à audiência na data designada pelo Cartório, o que deve ser feito com antecedência mínima de 20 dias.Intime-se os autores por advogado constituído (art. 334, §3º, CPC/15).Deverá a parte ré ser advertida da possibilidade do art. 334, §5º, bem como do termo inicial do prazo de contestação (art. 335).Fiquem as partes advertidas, ainda, de que o não comparecimento injustificado à audiência de conciliação é considerado ato atentatório à dignidade da justiça e será sancionado com multa de até dois por cento da vantagem econômica pretendida ou do valor da causa (art. 334, §8º).Publique-se. Intime-seMaceió, 10 de maio de 2018.Henrique Gomes de Barros TeixeiraJuiz de DireitoVencimento:01/06/2018'),
        ProcessMoviment(
            data='03/05/2018',
            details='Conclusos'),
        ProcessMoviment(
            data='02/05/2018',
            details='Conclusos'),
        ProcessMoviment(
            data='02/05/2018',
            details='Distribuído por Sorteio'
            )
        ]
    )