##  Titolo del progetto
*Amazon Product Reviews – Sentiment Analysis*
Progetto di analisi del sentiment delle recensioni di prodotti Amazon tramite tecniche di Natural Language Processing (NLP) e Machine Learning, 
con l’obiettivo di classificare automaticamente l’opinione degli utenti e testare il modello su un dataset esterno per verificarne la capacità di generalizzazione.


---

##  Team Members
| Nome | Ruolo | Competenze principali |
|------|--------|-----------------------|
| Francesca Amarena | Lead Developer | Data Cleaning, NLP, Model Training |
| Matteo Gagliardi | Team Manager |  Data Preprocessing, Exploratory Data Analysis, Model Evaluation|

---

##  Obiettivi del progetto
1. Pulire e preprocessare un dataset di recensioni testuali provenienti da Amazon.
2. Applicare tecniche di Natural Language Processing per trasformare il testo in dati strutturati.
3. Addestrare un modello di Sentiment Analysis in grado di classificare le recensioni in base al sentiment espresso.
4. Valutare le prestazioni del modello sui dati di training.
5. Testare il modello su un secondo dataset per verificare la sua affidabilità su dati non visti.
   
---
##  Motivazione della scelta del Dataset
Abbiamo scelto il dataset Amazon Product Reviews perché rappresenta un caso di studio reale e molto diffuso nel contesto dell’e-commerce.
L’analisi automatica delle recensioni consente di estrarre informazioni utili sul grado di soddisfazione degli utenti,supportando aziende e consumatori nei processi decisionali.
Inoltre, il dataset offre un’elevata quantità di dati testuali non strutturati, ideale per l’applicazione pratica di tecniche di NLP e modelli di Machine Learning.

---

##  Dataset
*DATASET PER ADDESTRAMENTO:*

*Fonte:* Kaggle – Amazon Product Reviews  
*Contenuto principale:*
- Recensioni di prodotti Amazon

- Variabili chiave:
    1)Testo della recensione
    2)Rating (1–5 stelle)

Il dataset è stato sottoposto a un processo di data cleaning, che include:
    -Rimozione di valori nulli e duplicati
    -Normalizzazione del testo
    -Tokenizzazione e rimozione delle stopwords

  

*DATASET PER TEST:*
---

##  Struttura del progetto
Il progetto è stato organizzato in fasi successive, dalla preparazione dei dati fino al testing finale del modello:

*Francesca*: Pulizia del dataset, feature extraction, addestramento del modello
*Matteo*: Analisi esplorativa dei dati, preprocessing, valutazione del modello e test su dataset esterno

## Conclusioni
Il progetto dimostra come l’analisi automatica del sentiment possa supportare le aziende nell’interpretazione delle recensioni dei clienti, trasformando grandi volumi di feedback testuale in insight utili.
Il modello sviluppato è in grado di analizzare nuove recensioni in modo affidabile, offrendo uno strumento scalabile per monitorare la percezione dei prodotti.

Questa soluzione può essere applicata a contesti reali di e-commerce per migliorare il processo decisionale, la qualità dei prodotti e l’esperienza complessiva del cliente.
