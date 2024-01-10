#!/bin/bash

python3 -m venv venv

if [[ "$OSTYPE" == "linux-gnu"* ]]; then

    
source venv/bin/activate
elif [[ "$OSTYPE" == "darwin"* ]]; then

    
source venv/bin/activate
else
    venv\Scripts\activate.bat  # Windows
fi

pip install -r requirements.txt