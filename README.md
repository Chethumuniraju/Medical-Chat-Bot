

create -n mchatbot  python=3.8 -y

conda activate mchatbot

 
pip install -r requirements.txt



python store_index.py

python app.py


