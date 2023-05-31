# simple-brute-force-dvr

Este é um script de linha de comando desenvolvido para facilitar a varredura de dispositivos DVR (Digital Video Recorder) em uma rede. Ele permite descobrir dispositivos DVR ativos em uma rede específica.

### Requisitos

Antes de usar este script, certifique-se de ter os seguintes requisitos instalados:

* Python 3.x
* Biblioteca vlc

### Instalação

Certifique-se de ter o Python 3.x instalado no seu sistema.
Você pode baixar a versão mais recente do Python em https://www.python.org/downloads/.

Abra o terminal ou prompt de comando e execute o seguinte comando para instalar a biblioteca vlc:

* python
```sh
  pip install python-vlc
```
    
### Uso

Faça o download do arquivo scan.py e salve-o no diretório desejado.
Abra o terminal ou prompt de comando e navegue até o diretório onde o arquivo scan.py está localizado.
Execute o seguinte comando para iniciar a varredura de DVRs na rede:

* python
 ```sh
python scan.py -f ARQUIVO_COM_LISTA_DE_IPS.txt
 ```

O script irá iniciar a varredura e exibirá os resultados no terminal.

Observação: Você pode deve passar uma lista de IPs em arquivo de texto como argumento com a opção -f.

### Argumentos do Script

O script scan.py suporta os seguintes argumentos obrigatórios:

    -f: Especifica o arquivo de texto com a lista de IPs.

Exemplo de uso com argumentos:
 ```sh
python scan.py -f EXAMPLE_LIST.txt
  ```

Este comando irá varrer a lista de IPs que contem no arquivo.

### Considerações Finais

Este script é fornecido como uma ferramenta de varredura básica e deve ser usado com responsabilidade.
Certifique-se de ter permissão para realizar a varredura na rede e respeite as leis e regulamentações aplicáveis.

Tenha em mente que a varredura de dispositivos DVR em uma rede sem a devida autorização pode ser ilegal.
Verifique sempre as leis e regulamentações locais antes de realizar qualquer varredura de rede.