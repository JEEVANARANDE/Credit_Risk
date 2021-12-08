echo $PATH

export PYTHONPATH=/c/Python_Lab/ineuron/internship/Credit_Risk_Data/Credit_Risk/src:${PYTHONPATH}
echo $PYTHONPATH


git rm -r --cached 'data\raw\SouthGermanCredit_data.csv'
git commit -m "stop tracking data\raw\SouthGermanCredit_data.csv"