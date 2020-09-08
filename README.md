# cron_gzip

Tento skript vezme veškeré `.log` soubory ze složky `/var/log` a zazipuje je do `.gz` souborů, poté původní soubory vyčistí (promaže) do nulového stavu.

Jsou tu zde dvě různé verze podle toho, co přesně od skriptu potřebujete:
- `gzip_files.py` po každém spuštění nahradí původní soubory
- `gzip_files_date.py` přidá datum spuštění k názvu `.gz` souboru a při spuštění jiný den vytvoří nový `.gz` soubor.

## Použití

1. Naklonujeme repo pomocí
```
git clone https://github.com/elijabesu/cron_gzip.git
```

2. Skript spustíme pomocí

```
sudo python3 <cesta k souboru gzip_files.py>
```

Konkrétním příkladem by bylo `sudo python3 /home/faltynkova_eliska/cron_gzip/gzip_files.py`.

3. Hotovo

![gzip_files terminal](https://github.com/elijabesu/cron_gzip/blob/master/pictures/terminal.jpg)

### Použití gzip_files_date.py
Tento skript se spouští stejným způsobem, pouze vytváří pokaždé nový `gzip` soubor (jak je popsáno výše).

Máme následující soubory ve složce `/var/log`:

![pred](https://github.com/elijabesu/cron_gzip/blob/master/pictures/pred-spustenim.png)

Spustíme script (pokud jsme ve složce, kde je soubor uložený, jinak nahradíme `gzip_files_date.py` cestou k tomuto souboru):

```
sudo python3 <cesta k souboru gzip_files_date.py>
```

![behem](https://github.com/elijabesu/cron_gzip/blob/master/pictures/spusteni.png)

Výsledek:

![po](https://github.com/elijabesu/cron_gzip/blob/master/pictures/po-spusteni.png)

### Automatické spuštění
Pro příklad je použito nastavení spouštění každých 30 dní o půlnoci.

1. V příkazovém řádku si otevřeme cron table pomocí 

```
sudo crontab -e
```

2. V editoru napíšeme následující command (`<cesta k souboru>` nahradíme cestou k `gzip_files.py`):

```
0 0 */30 * * python3 <cesta k souboru>
```

Konkrétním příkladem by bylo `0 0 */30 * * python3 /home/faltynkova_eliska/cron_gzip/gzip_files.py`.

3. Uložíme a zavřeme soubor
    1. zavřeme soubor pomocí <kbd>Ctrl+X</kbd>
    2. potvrdíme uložení změn pomocí <kbd>Y</kbd>
    3. potvrdíme název souvoru pomocí <kbd>Enter</kbd>