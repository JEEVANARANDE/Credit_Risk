echo $PATH

export PYTHONPATH=/c/Python_Lab/ineuron/internship/Credit_Risk_Data/Credit_Risk/src:${PYTHONPATH}
echo $PYTHONPATH


git rm -r --cached 'data\raw\SouthGermanCredit_data.csv'
git commit -m "stop tracking data\raw\SouthGermanCredit_data.csv"


dvc repro
  205  python src/get_data.py
  206  python src/get_data.py
  207  python Cassandra_Python_Connectivity/connect_database.py
  208  python src/get_data.py
  209  python src/load_data.py
  210  touch src/split_data.py
  211  dvc repro
  212  dvc repro
  213  git add . && git commit -m "stage 2 complete" && git push origin main
  214  touch src/train_and_evaluate.py