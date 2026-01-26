import pandas as pd

df = pd.read_csv("C:\\Users\\franc\\Desktop\\DEVELHOPE\\sentiment_analysis\\data\\reviews.csv")

#print("prima", df.columns)

da_eliminare = ["ProductId", "UserId", "ProfileName", "HelpfulnessDenominator", "HelpfulnessNumerator"]
df.drop(da_eliminare, axis=1, inplace=True)

#imuovere righe senza testo
df = df.dropna(subset=["Text"])

# cols_to_keep = [
#     "Text",
#     "Summary",
#     "Score",
#     "Time"
# ]

# df = df[cols_to_keep]

#eliminiamo i duplicati
df = df.drop_duplicates(subset=["Text"])

# Rimuovere testi vuoti
df = df.dropna(subset=["Text"])
df = df[df["Text"].str.strip() != ""]

#Convertire il tempo (UNIX → datetime)
df["Time"] = pd.to_datetime(df["Time"], unit="s")

#funzione che assegna sentiment come target
def assegna_punteggio(score):
    if score <= 2:
        return "negative"
    elif score == 3:
        return "neutral"
    else:
        return "positive"

df["Sentiment"] = df["Score"].apply(assegna_punteggio)


# Pulizia testo base (livello beginner)
import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)   # link
    text = re.sub(r"[^a-z\s]", "", text)  # simboli
    return text

df["Text_clean"] = df["Text"].apply(clean_text)

df.drop("Text", axis=1, inplace=True)
#creiamo dataset pulito
df.to_csv("data/reviews_clean.csv", index= False)

#proviamo a fare le groupby per osservare eventuali sbilanciamenti del dataset

df_negative = df[df["Sentiment"] == "negative"]
df_positive = df[df["Sentiment"] == "positive"]
df_neutral = df[df["Sentiment"] == "neutral"]

print("Negative = ", df_negative.count())
print("positive = ", df_positive.count())
print("neutral = ", df_neutral.count())
