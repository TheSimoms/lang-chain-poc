# LangChain POC

Enkel POC for å vise hvordan store språkmodeller (LLM) kan brukes til å lete frem informasjon i egne data.

POC-en bruker GPT4All til å lete frem informasjon i PDF-dokumenter.

## Komme i gang

### Gjøre klar Python

Prosjektet er utviklet med Python 3.11. Det anbefales å opprette et virtuelt Python-miljø.

Opprett miljøet:
```console
python3.11 -m venv venv
```

Ta miljøet i bruk:
```console
. venv/bin/activate
```

Installer avhengigheter:
```console
pip3 install -r requirements.txt
```

### Gjøre klar LLM

Last ned ønsket modell fra [GPT4All](https://gpt4all.io/index.html) sine nettsider.

Lagre modellen som `data/modell.gguf`.

### Gjøre klar dokumenter

Modellen er avhengig av kontekst for å kunne lete frem data.

Lagre relevante PDF-dokumenter i `data/pdf/`.

## Kjøre programmet

### Terminal

```console
python3 lang_chain_poc/__init__.py "Hvor mange veier må en mann gå før du kaller han en mann?"
```

### Nettleser

```console
flask --app application run
```

Tjenesten kan nås på http://127.0.0.1:5000.
