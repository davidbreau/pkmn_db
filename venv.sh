VENV_DIR="venv"

if [ -d "$VENV_DIR" ]; then
    echo "$VENV_DIR existing. activating ..."
    source $VENV_DIR/bin/activate
else
    echo "$VENV_DIR not existing. creation pending ..."
    python -m venv $VENV_DIR
    # Vérifier si la création a réussi
    if [ -d "$VENV_DIR" ]; then
        echo "$VENV_DIR created"
        source $VENV_DIR/bin/activate
        echo "now installing dependencies ..."
        pip install -r requirements.txt
        pip install --upgrade pip
    else
        echo "$VENV_DIR creation failed"
        exit 1


    fi
fi
