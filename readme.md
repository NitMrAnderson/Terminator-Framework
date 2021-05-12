# Terminator Framework </br> T-70
**Terminator Framework T-70** is web pentesting framework with a plugin system.

Install requirements:
```
pip3 install -r requirements.txt
```

Run: 
``` 
python3 terminator.py
```

After you install Terminator requirements and run framework requirements for some plugins still may be not installed.
If it's so Terminator will return u message: 
```
Err! Maybe some requirements not installed!
It's may be fixed if u run "requirements"
```
</br>To fix it just run in Terminator console: ```requirements```. 

To see a list of supported commands run in Terminator console: ```help```.  

To install your plugin just copy folder with plugin into the ```./core/bin``` directory.