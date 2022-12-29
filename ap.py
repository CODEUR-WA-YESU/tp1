import pandas as pd
import joblib

test=[[2,1,113,13]]

model=joblib.load('mesanomod.pkl')

print("D'apres le donnees se trouvant dans test nous estimons que le politicien aura comme voix: ",model.predict(test)[0])