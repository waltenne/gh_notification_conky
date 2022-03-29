# O que é?

Essa integração irá conectar na API do Github, coletando os seguintes dados

- Stars
- Forks
- Issues
- Pull Requests

Onde será criado um banco local para gravar essas dados coletados, ao chegar atualização ocorrerá uma notificação sonora utilizando a voz do Jefferson do LinuxTips

# Estrutura do diretório
```
gh_notification_conky
├── com
│   └── github
│       ├── db.py
│       └── repository.py
├── linuxtips
│   ├── resource
│   │   ├── e_olha_so.mp3
│   │   ├── sensacional.mp3
│   │   ├── vai.mp3
│   │   └── zika_de_mais.mp3
│   └── sounds.py
├── main.py
├── README.md
└── repo
    ├── config.py
    └── integration.ini
```

## Como configurar

## Integration.ini

A configuração é feita no arquivo **integration.ini** dentro do diretório repo, nele possui os seguintes parametros

- GITHUB_TOKEN=
- token do usuario utilizado da autenticação no github
- GITHUB_USER=
  nome do usuario utilizado da autenticação no github
- GITHUB_REPOSITORY=
  {usuario}/{repositorio} que será consultado, por exemplo waltenne/guiadevopsbrasil

Para gerar o token do Github indico esse guia.

[Criar um token de acesso pessoal](https://docs.github.com/pt/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

## Conky

- Instale o Conky [Repositorio](https://github.com/brndnmtthws/conky)
- Baixe o conversor de código lua para o conky
  ```wget https://raw.githubusercontent.com/brndnmtthws/conky/main/extras/convert.lua```
- Copie o diretório github dentro de conky para o **~/.conky**
- Crie um Script de inicialização do conky, onde **user** é o nome do usuário do sistema

```
#!/bin/bash
sleep 10 &&
conky -d -c "/home/user/.conky/github/conky"
exit
```

- Dê permissão de execução chmod +x nome_script_criado.sh
- Configure no Sistema Operacional a Inicialização do Conky

[Ubuntu](https://ubunlog.com/pt/iniciar-scripts-al-inicio-ubuntu/#:~:text=Para%20isso%20vamos%20Sistema%E2%80%93%3E%20Prefer%C3%AAncias,Ubuntu%20ir%C3%A1%20carregar%20nossos%20scripts.)
[Debian](https://pt.stackoverflow.com/questions/249287/como-executar-comandos-do-shell-na-inicializa%C3%A7%C3%A3o-do-debian)