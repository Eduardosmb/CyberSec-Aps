# Escaneador de portas
Este projeto é uma aplicação gráfica simples desenvolvida em Python usando a biblioteca `tkinter` para escanear portas abertas em um determinado host. O escaneamento é realizado utilizando `threads` para melhorar a eficiência, especialmente quando escaneando intervalos maiores de portas.

## Como Funciona

O programa permite que o usuário insira um host e um intervalo de portas para escanear. Para cada porta no intervalo especificado, ele tenta estabelecer uma conexão. Se a conexão for bem-sucedida, a porta é considerada "aberta" e o serviço associado a essa porta é identificado (se estiver listado nas portas bem conhecidas).

As portas conhecidas e seus serviços são mapeados em um dicionário no código, mas o programa também pode detectar outras portas abertas que não estejam listadas, marcando-as como "Serviço Desconhecido".

## Estrutura do Código

- **`portas_bem_conhecidas`**: Um dicionário que mapeia portas bem conhecidas para seus respectivos serviços.
- **`escanear_porta(host, porta, area_texto)`**: Função que tenta se conectar a uma porta específica em um host e atualiza a interface com o resultado.
- **`iniciar_escanemento(host_entrada, porta_inicio_entrada, porta_fim_entrada, area_texto)`**: Função que inicia o processo de escaneamento para um intervalo de portas, utilizando `threads`.
- **`iniciar_interface_grafica()`**: Função que configura e inicia a interface gráfica do usuário utilizando `tkinter`.

## Como Usar

### Requisitos

- **Python 3**: Certifique-se de ter o Python 3 instalado na sua máquina.
- **Biblioteca `tkinter`**: `tkinter`.

### Clonar o Repositório

Para começar a usar o programa, clone este repositório em sua máquina:

```bash
git clone https://github.com/seu-usuario/scanner-de-portas.git
python3 aps.py
```

## Exemplo de Uso

### Entrada

- **Host**: `127.0.0.1`
- **Porta Inicial**: `20`
- **Porta Final**: `80`
