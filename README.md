### Instalation

```bash
#as root
apt install python-venv -y # for a specific python version use "python3.8-venv" instead

#as normal user
python -m venv /path/to/folder/.venv #for a specific python version use "python3.8" instead

source /path/to/folder/.venv/bin/activate #activate venv
pip install selenium schedule #pip installations
```

### Run

```bash
python run manage.py
```
