# ScriptUpDLLs
Script made in Python to automatically load DLLs for a given feed in AZURE DEVOPS

# Instructions
* Add this feed

```console
eduardollanda@pc:~$ nuget.exe sources Add -Name "name of your feed" -Source "LINK DO FEED"
```

* Put the script where the DLLs are
* When calling the script you should pass as argument the name of your feed:

```console
eduardollanda@pc:~$ python DLLs "name of your feed"
```
*OBS: You only need to add the feed once