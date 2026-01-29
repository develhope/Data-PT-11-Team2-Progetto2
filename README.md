##  Titolo del progetto
*Amazon Product Reviews – Sentiment Analysis*
Progetto di analisi del sentiment delle recensioni di prodotti Amazon tramite tecniche di **Natural Language Processing (NLP)** e **Deep Learning**, 
con l’obiettivo di costruire un modello in grado di Classificare automaticamente il Sentiment delle recensioni in **tre classi (negativo, positivo, neutro)**, e testarne il comportamento su una nuova, mai vista.
Considerata l’attitudine dei programmatori alla visualizzazione dei risultati, è stato inoltre sviluppato un **semplice sito web** per consentire l’inserimento di nuove recensioni e la visualizzazione immediata della classificazione del sentiment.

---

##  Team Members
| Nome | Ruolo | Competenze principali |
|------|--------|-----------------------|
| Francesca Amarena | Lead Developer | Data Cleaning, NLP Model Design & Training, Deep Learning |
| Matteo Gagliardi | Team Manager |  Data Cleaning, Preprocessing, Exploratory Data Analysis, Model Evaluation, Testing, Data Visualization |
 
---

##  Obiettivi del progetto
1. Pulire e preprocessare un dataset di recensioni testuali provenienti da Amazon.
2. Applicare tecniche di **Natural Language Processing** per trasformare il testo in dati strutturati.
3. Addestrare un modello di **Sentiment Analysis** in grado di classificare le recensioni in base al sentiment espresso su un primo dataset di test.
4. Valutare le prestazioni del modello sui dati di training.
5. Testare il modello sul dataset pulito, grande, per verificare la sua affidabilità su dati non visti.
6. Integrare il modello in una semplice interfaccia web per l’utilizzo interattivo.

---
##  Motivazione della scelta del Dataset
Abbiamo scelto il dataset Amazon Product Reviews perché rappresenta un caso di studio reale e molto diffuso nel contesto dell’e-commerce.
L’analisi automatica delle recensioni consente di estrarre informazioni utili sul grado di soddisfazione degli utenti,supportando aziende e consumatori nei processi decisionali.
Inoltre, il dataset offre un’elevata quantità di dati testuali non strutturati, ideale per l’applicazione pratica di tecniche di NLP e modelli di Machine Learning.

---

##  Dataset

*DATASET PER ADDESTRAMENTO:*

*Fonte:* Kaggle – Amazon Product Reviews -> https://www.kaggle.com/datasets/arhamrumi/amazon-product-reviews  
*Contenuto principale:*
- Recensioni di prodotti Amazon

- Variabili chiave:
    1)Testo della recensione
    2)Rating (1–5 stelle)

Il dataset è stato sottoposto a un processo di data cleaning, che include:
    -Rimozione di valori nulli e duplicati
    -Normalizzazione del testo
    -Tokenizzazione e rimozione delle stopwords
    -Conversione del rating in tre classi di sentiment

  

*DATASET PER TEST:*
*Fonte:* Recensioni italiane 
*Contenuto principale:*
- Recensioni di prodotti Amazon

- Variabili chiave:
    1)Valutazioni positive e negative (0,1)
    2)Testo della recensione

Il dataset non è stato sottoposto a un processo di data cleaning

---

##  Struttura del progetto
Il progetto è stato organizzato in fasi successive, dalla preparazione dei dati fino al testing finale del modello:

*Francesca*: Analisi esplorativa dei dati, feature extraction,progettazione e addestramento del modello
*Matteo*: Analisi esplorativa dei dati, preprocessing, pulizia del dataset e test su dataset esterno

---

## Interfaccia Web
Per rendere il progetto più fruibile, è stato sviluppato un **semplice sito web** utilizzando:
- **Flask** per la gestione del backend
- **HTML, CSS e JavaScript (basic)** per la realizzazione dell’interfaccia utente
- utilizzo di tecniche di **prompt engineering** per migliorare l’organizzazione del codice front-end

Il sito consente di:
- inserire una recensione testuale
- ottenere la classificazione del sentiment (negativo, neutro o positivo)
- visualizzare il risultato in modo immediato

---

## Conclusioni
Il progetto dimostra come l’analisi automatica del sentiment possa supportare le aziende nell’interpretazione delle recensioni dei clienti, trasformando grandi volumi di feedback testuale in insight utili.
Il modello sviluppato è in grado di analizzare nuove recensioni in modo affidabile, offrendo uno strumento scalabile per monitorare la percezione dei prodotti e può essere integrato in applicazioni reali di e-commerce, contribuendo a migliorare:
- il processo decisionale
- la qualità dei prodotti
- l’esperienza complessiva del cliente

Questa soluzione può essere applicata a contesti reali di e-commerce per migliorare il processo decisionale, la qualità dei prodotti e l’esperienza complessiva del cliente.
## Conclusioni
Il progetto dimostra come l’analisi automatica del sentiment possa supportare le aziende nell’interpretazione delle recensioni dei clienti, trasformando grandi volumi di feedback testuale in insight utili.
Il modello sviluppato è in grado di analizzare nuove recensioni in modo affidabile, offrendo uno strumento scalabile per monitorare la percezione dei prodotti.

Questa soluzione può essere applicata a contesti reali di e-commerce per migliorare il processo decisionale, la qualità dei prodotti e l’esperienza complessiva del cliente.
