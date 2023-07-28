import requests

cookies = {
    'JSESSIONID': '5588BAFC12CBF777DCF9CD7466F5A1AC.sajcas2',
    'NSC_WJQ_TBKDBT': 'ffffffffc3a014db45525d5f4f58455e445a4a4229c4',
    'NSC_WJQ_FTBK': 'ffffffffc3a014d845525d5f4f58455e445a4a4229a0',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'pt-BR,pt;q=0.7',
    'Connection': 'keep-alive',
    'Cookie': 'JSESSIONID=5588BAFC12CBF777DCF9CD7466F5A1AC.sajcas2; NSC_WJQ_TBKDBT=ffffffffc3a014db45525d5f4f58455e445a4a4229c4; NSC_WJQ_FTBK=ffffffffc3a014d845525d5f4f58455e445a4a4229a0',
    'Referer': 'https://esaj.tjce.jus.br/cpopg/show.do?processo.codigo=01Z081I9T0000&processo.foro=1&processo.numero=0070337-91.2008.8.06.0001',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Brave";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

params = {
    'script': '1690444828767',
    'retorno': 'https://esaj.tjce.jus.br/cpopg/show.do?processo.codigo=01Z081I9T0000&processo.foro=1&processo.numero=0070337-91.2008.8.06.0001',
}

response = requests.get(
    'https://esaj.tjce.jus.br/sajcas/conteudoIdentificacaoJson',
    params=params,
    cookies=cookies,
    headers=headers,
)

print(response.json())