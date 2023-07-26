# Post Combos

Programa feito em Python usando GUI

Script de manipulação de ‘strings’ para criação de uma url post para consulta de combos categóricos numa API usando o postman.

## Estrutura do algorítimo da aplicação

O script recebe como entrada um arquivo de texto com uma lista de ‘strings’, uma em cada linha, e gera como saída um arquivo de texto com uma lista de urls, uma em cada linha, para consulta de combos categóricos numa API usando o postman.

Como variáveis os programa deverá conter:

No servidor:
- **{servidor}** - Servidor onde a API está hospedada [tipo string]
- **{pasta_da_aplicacao}** - Pasta onde a aplicação está hospedada [tipo string]

No PC do utilizador:
- **{pasta_dos_arquivos}** - Abre uma caixa no qual o utilzador deverár inforar onde os arquivos de consulta de combos estão armazenados.  [tipo string]
- **{string_combo}** - ‘String’ que será obtida do arquivo de entrada e usada para gerar a url de consulta de combo [tipo string]
- **{url_post_list}** - Arquivo de texto com a lista de urls de consulta de combos
- **{url_post_combo}** - Url de consulta de combo gerada a partir da ‘string’ obtida do arquivo de entrada [tipo string]

### Exemplo de Entrada para os combos

Como entrada, o utilizador deverá apontar o caminho onde o arquivo com a lista de combos está armazenado. O arquivo deverá conter uma lista de ‘strings’, uma em cada linha, como no exemplo abaixo:

file_string_combos.txt

Dentro do arquivo, as ‘strings’ deverão estar separadas por quebra de linha, como no exemplo abaixo:

```txt
string_combo_A
string_combo_B
string_combo_C
```

### Exemplo da url gerada para consulta de combo

url_post_list.txt

```txt
http://{servidor}/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&
    BIP_folder=IBFS:/WFC/Repository/{pasta_da_aplicacao}/procedures/combos/&BIP_item={string_combo}
```

