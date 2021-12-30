# UK Lateral Flow Test Checker
## Install
You will need the dependencies `selenium` and `plyer`. Install these as follows:
```bash
pip install selenium
pip install plyer
```

Clone the repository and then you can run the script. You may have to set the executable bit if you get a permission error:
```bash
chmod +x lateral-flow.py
```

## Usage
Run as follows:
```bash
./lateral-flow.py
```

This will print lateral flow availability into the console every 30 minutes. For extra functionality, such as desktop notifications, see the help text:
```bash
./lateral-flow.py --help
```
