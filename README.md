# ScriptUpDLLs
Script feito em Python para upar DLLs automaticamente para um determinado feed no AZURE DEVOPS

# Modo de uso
* Adicione o feed

```console
conductorlabs@pc:~$ nuget.exe sources Add -Name "seu feed" -Source "LINK DO FEED"
```

* Coloque o script onde estão as DLLs
* Ao chamar o Script deve-se passar como argumento o nome de seu feed:

```console
conductorlabs@pc:~$ python DLLs "nome do seu feed"
```
