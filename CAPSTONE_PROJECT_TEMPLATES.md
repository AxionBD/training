# 🎯 APPLIED AI PRACTITIONER PROGRAM: CAPSTONE PROJECT TEMPLATES

**Applied Artificial Intelligence (AAI)**  
**Capstone Project Guide & Templates**  
**Date:** March 4, 2026

---

## 📌 OVERVIEW

**Purpose:** Complete a real-world AI/ML project that demonstrates job-ready competency

**Duration:** Weeks 3–5 (final project, ~20–30 hours)

**Deliverables Required:**
- ✅ Working code (GitHub repo)
- ✅ Project documentation (README)
- ✅ Data analysis or model output
- ✅ Deployment (live app or demo)
- ✅ 10-minute presentation

**Grading Rubric:**
| Component | Weight | Details |
|-----------|--------|---------|
| Technical correctness | 30% | Code works, models trained correctly |
| Creativity & innovation | 20% | Original approach, interesting problem |
| Code quality | 15% | Clean, documented, organized |
| Presentation | 15% | Clear communication & demo |
| Completeness | 20% | All deliverables, proper eval |

**Passing Score:** 70%+

---

---

# 📊 PROJECT OPTION 1: PREDICTIVE ANALYTICS (MACHINE LEARNING)

**Emphasis:** ML modeling, data exploration, evaluation  
**Skills Demonstrated:** Python, pandas, scikit-learn, visualization  
**Complexity:** Intermediate  
**Team Size:** Individual or pair  

---

## 🎯 PROJECT OVERVIEW

**Goal:** Build a predictive ML model on a real dataset and deploy it as a web app.

**Example Projects:**
1. **Housing Price Prediction**
   - Predict house prices based on features (size, location, age)
   - Dataset: Boston Housing, Ames Housing
   
2. **Customer Churn Prediction**
   - Predict if customers will leave a service
   - Dataset: Telecom churn, Bank churn (Kaggle)

3. **Credit Risk Assessment**
   - Predict loan default probability
   - Dataset: Credit card default (UCI), Lending Club

4. **Movie Recommendation System**
   - Recommend movies based on user preferences
   - Dataset: MovieLens (Kaggle)

5. **Medical Diagnosis**
   - Predict disease presence (e.g., diabetes, heart disease)
   - Dataset: UCI ML Datasets

---

## 📋 PROJECT REQUIREMENTS

### **Phase 1: Problem Definition (Days 1–2)**

**Deliverable:** Project proposal (1 page)

**Include:**
- [ ] Problem statement (3–4 sentences)
- [ ] Dataset description
- [ ] Target variable (what we're predicting)
- [ ] Features used
- [ ] Success metric (accuracy, RMSE, F1, etc.)
- [ ] Why this problem matters

**Example:**
```
PROBLEM STATEMENT:
"Telecom companies lose 25% of customers annually (churn). 
This costs millions. By predicting which customers are likely 
to churn, companies can intervene with retention strategies.

GOAL: Build a model that predicts customer churn with 80%+ accuracy.

DATASET: Bank telecom churn dataset (20K customers, 21 features)
TARGET: Binary (churn: yes/no)
METRICS: Accuracy, Precision, Recall, F1-score, ROC-AUC
```

---

### **Phase 2: Data Exploration & Cleaning (Days 3–5)**

**Deliverable:** Jupyter notebook with EDA

**Include:**
- [ ] Data loading & shape
- [ ] Missing values analysis
- [ ] Data types review
- [ ] Statistical summary
- [ ] 5+ visualizations (distributions, correlations, relationships)
- [ ] Data cleaning decisions documented
- [ ] Feature engineering (if applicable)

**Code Template:**
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('churn.csv')
print(df.shape)
print(df.info())
print(df.describe())

# Missing values
print(df.isnull().sum())

# Visualizations
plt.figure(figsize=(12, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Feature Correlation Matrix')
plt.show()

# Data cleaning
df = df.dropna()  # or df.fillna(...)
df['numeric_col'] = pd.to_numeric(df['numeric_col'])

print("Data cleaned! Shape:", df.shape)
```

---

### **Phase 3: Model Development (Days 6–8)**

**Deliverable:** Trained models with evaluation

**Requirements:**
- [ ] Split data (train/test, 80/20)
- [ ] Build 3+ models:
  - Model 1: Logistic Regression (baseline)
  - Model 2: Random Forest or Decision Tree
  - Model 3: Gradient Boosting (XGBoost) or SVM
- [ ] Train and evaluate each model
- [ ] Compare performance
- [ ] Select best model with justification

**Code Template:**
```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Data preparation
X = df.drop('churn', axis=1)
y = df['churn']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model 1: Logistic Regression
lr = LogisticRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)
print("LR Accuracy:", accuracy_score(y_test, lr_pred))

# Model 2: Random Forest
rf = RandomForestClassifier(n_estimators=100)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
print("RF Accuracy:", accuracy_score(y_test, rf_pred))

# Model 3: Gradient Boosting
gb = GradientBoostingClassifier()
gb.fit(X_train, y_train)
gb_pred = gb.predict(X_test)
print("GB Accuracy:", accuracy_score(y_test, gb_pred))

# Select best
models = {
    'Logistic Regression': (lr, lr_pred),
    'Random Forest': (rf, rf_pred),
    'Gradient Boosting': (gb, gb_pred)
}

best_model_name = max(models, key=lambda x: accuracy_score(y_test, models[x][1]))
print(f"Best model: {best_model_name}")
```

---

### **Phase 4: Model Evaluation & Interpretation (Days 9–10)**

**Deliverable:** Comprehensive evaluation report

**Include:**
- [ ] Confusion matrix
- [ ] ROC curve
- [ ] Feature importance analysis
- [ ] Error analysis (false positives/negatives)
- [ ] Recommendations for improvement

**Visualization Example:**
```python
from sklearn.metrics import confusion_matrix, roc_curve, auc
import matplotlib.pyplot as plt

# Confusion matrix
cm = confusion_matrix(y_test, best_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.show()

# ROC curve
fpr, tpr, thresholds = roc_curve(y_test, best_model.predict_proba(X_test)[:, 1])
roc_auc = auc(fpr, tpr)
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label='ROC Curve (AUC = {:.2f})'.format(roc_auc))
plt.plot([0, 1], [0, 1], 'k--', label='Random')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend()
plt.title('ROC Curve')
plt.show()

# Feature importance
importances = best_model.feature_importances_
indices = np.argsort(importances)[::-1]
plt.figure(figsize=(10, 6))
plt.title("Feature Importance")
plt.bar(range(X.shape[1]), importances[indices])
plt.xticks(range(X.shape[1]), X.columns[indices], rotation=45)
plt.show()
```

---

### **Phase 5: Deployment (Days 11–12)**

**Deliverable:** Live Streamlit app

**App Components:**
- [ ] Data upload (CSV, or sample data)
- [ ] Prediction interface (user inputs features)
- [ ] Model prediction (real-time)
- [ ] Visualization of results
- [ ] Model info (accuracy, precision, recall)

**Streamlit App Code:**
```python
import streamlit as st
import pickle
import pandas as pd

# Load saved model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Customer Churn Prediction")
st.write("Enter customer details to predict churn probability")

# Input fields
age = st.slider("Age", 18, 80, 30)
tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.slider("Monthly Charges ($)", 0, 150, 50)

# Make prediction
input_data = pd.DataFrame({
    'age': [age],
    'tenure': [tenure],
    'monthly_charges': [monthly_charges]
})

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]
    
    st.write(f"**Prediction:** {'Will Churn' if prediction == 1 else 'Will Stay'}")
    st.write(f"**Churn Probability:** {probability:.2%}")
    
    # Visualization
    fig, ax = plt.subplots()
    ax.bar(['Will Stay', 'Will Churn'], [1-probability, probability])
    st.pyplot(fig)
```

**Deploy to Streamlit Cloud:**
1. Push code to GitHub
2. Connect repo to Streamlit Cloud
3. Deploy (free, automatic updates)

---

### **Phase 6: Final Presentation (Day 13)**

**Deliverable:** 10-minute presentation

**Presentation Outline:**
1. **Problem & Motivation** (1 min)
   - Why does this problem matter?
   
2. **Data Overview** (1 min)
   - Dataset size, features, target variable
   
3. **Methodology** (2 mins)
   - Data cleaning steps
   - Models trained
   - Evaluation metrics
   
4. **Results** (3 mins)
   - Best model performance
   - Key findings
   - Feature importance
   - Error analysis
   
5. **Live Demo** (2 mins)
   - Show app in action
   
6. **Improvements & Lessons** (1 min)
   - What you'd do differently
   - What you learned

---

## 📁 GITHUB REPO STRUCTURE

```
customer-churn-prediction/
├── README.md                 # Project description
├── requirements.txt          # Python dependencies
├── data/
│   ├── raw/
│   │   └── churn.csv
│   └── processed/
│       └── cleaned_churn.csv
├── notebooks/
│   ├── 01_EDA.ipynb         # Exploration
│   ├── 02_Modeling.ipynb    # Model training
│   └── 03_Evaluation.ipynb  # Results
├── src/
│   ├── preprocess.py        # Data cleaning functions
│   ├── model.py             # Model training code
│   └── utils.py             # Helper functions
├── models/
│   └── best_model.pkl       # Saved trained model
├── app.py                   # Streamlit app
└── results/
    ├── confusion_matrix.png
    ├── roc_curve.png
    └── feature_importance.png
```

---

## ✅ EVALUATION RUBRIC

| Criterion | Excellent (90-100%) | Good (80-89%) | Satisfactory (70-79%) | Needs Improvement (<70%) |
|-----------|---------------------|---------------|----------------------|--------------------------|
| **Data Cleaning** | Complete, well-documented | Mostly complete | Some documentation | Incomplete |
| **Model Selection** | 3+ models, justified choice | 2-3 models | 2 models | <2 models |
| **Evaluation** | Accuracy, precision, recall, ROC-AUC | 3+ metrics | 2 metrics | <2 metrics |
| **Visualization** | 5+ plots, clear insights | 4-5 plots | 2-3 plots | <2 plots |
| **Code Quality** | Clean, organized, documented | Generally clean | Somewhat messy | Unorganized |
| **Deployment** | Live app, working | Working locally | Partial | None |
| **Presentation** | Clear, engaging, complete | Clear, mostly complete | Adequate | Unclear |

---

---

# 🤖 PROJECT OPTION 2: GENERATIVE AI APPLICATION

**Emphasis:** LLMs, prompt engineering, RAG, chatbots  
**Skills Demonstrated:** Python, LangChain, OpenAI API, Streamlit  
**Complexity:** Intermediate  
**Team Size:** Individual or pair  

---

## 🎯 PROJECT OVERVIEW

**Goal:** Build an AI-powered application using LLMs (chatbot, Q&A system, content gen)

**Example Projects:**

1. **Company Documentation Assistant**
   - Upload company docs, PDFs, knowledge base
   - Ask questions, get answers from docs
   - *Technology:* RAG + ChatGPT

2. **Research Paper Q&A System**
   - Upload research papers
   - Ask questions about findings
   - *Technology:* RAG + Claude/OpenAI

3. **Personal Finance Advisor Chatbot**
   - Answers financial questions
   - Provides personalized advice
   - *Technology:* LLM + prompt engineering

4. **Customer Support Bot**
   - Handles FAQs automatically
   - Escalates complex issues to humans
   - *Technology:* LLM + knowledge base

5. **Content Generator for Marketing**
   - Generate product descriptions, ad copy
   - Customize for different platforms
   - *Technology:* LLM + prompt templates

---

## 📋 PROJECT REQUIREMENTS

### **Phase 1: Concept & Design (Days 1–2)**

**Deliverable:** 1-page project proposal

**Include:**
- [ ] Problem/use case
- [ ] Target users
- [ ] AI approach (prompt engineering vs. RAG vs. both)
- [ ] Data source (documents, PDFs, APIs)
- [ ] Success metrics
- [ ] Tech stack

**Example:**
```
PROJECT: Company HR Chatbot

PROBLEM:
Employees ask HR the same questions 100x per month (policies, benefits, time off).
This wastes HR time and employees don't get immediate answers.

SOLUTION:
Build a chatbot that:
- Answers HR policy questions (from company handbook)
- Provides personalized benefits info
- Escalates complex questions to HR team

TECH STACK:
- LangChain for RAG orchestration
- OpenAI API for LLM
- Pinecone for vector database
- Streamlit for UI

SUCCESS METRICS:
- Answers 80%+ of questions correctly
- Users find answer helpful 85%+ of time
- Reduces HR support tickets by 30%

DATA SOURCE:
- Company HR handbook (PDF)
- FAQ document (Google Doc)
- Benefits guide (PDF)
```

---

### **Phase 2: Data Preparation (Days 3–4)**

**Deliverable:** Cleaned, processed documents

**Include:**
- [ ] Document collection (gather 3–5 relevant docs/PDFs)
- [ ] Text extraction (from PDFs, if needed)
- [ ] Chunking (split into 500–1000 token chunks)
- [ ] Metadata tagging (source, date, category)

**Code Template:**
```python
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Extract text from PDFs
pdf_text = ""
with open('handbook.pdf', 'rb') as f:
    reader = PdfReader(f)
    for page in reader.pages:
        pdf_text += page.extract_text()

# Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", " ", ""]
)
chunks = splitter.split_text(pdf_text)
print(f"Created {len(chunks)} chunks")

# Add metadata
documents = [
    {"content": chunk, "source": "handbook.pdf"}
    for chunk in chunks
]
```

---

### **Phase 3: Vector Database Setup (Days 5–6)**

**Deliverable:** Working RAG system with embeddings

**Include:**
- [ ] Embeddings generation (OpenAI or open-source)
- [ ] Vector database setup (Pinecone, Chroma, Weaviate)
- [ ] Document storage
- [ ] Retrieval testing

**Code Template:**
```python
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Create embeddings
embeddings = OpenAIEmbeddings(openai_api_key="sk-...")

# Store in Chroma (free, local vector DB)
vectordb = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

# Test retrieval
query = "What is the vacation policy?"
results = vectordb.similarity_search(query, k=3)  # Top 3 results

for result in results:
    print(f"Source: {result.metadata['source']}")
    print(f"Content: {result.page_content}\n")
```

---

### **Phase 4: Chatbot Development (Days 7–9)**

**Deliverable:** Working chatbot with conversation memory

**Features:**
- [ ] RAG integration
- [ ] Multi-turn conversations
- [ ] Response evaluation (Is answer good?)
- [ ] Error handling & fallbacks

**Code Template:**
```python
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# Initialize LLM
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

# Memory for conversation history
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# Create RAG chain
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectordb.as_retriever(),
    return_source_documents=True
)

# Custom prompt
prompt_template = """
You are a helpful HR assistant. Answer questions based on the provided documents.
If you don't know, say "I don't have that information."

Question: {question}
Relevant Documents:
{context}

Answer:
"""

# Run conversation
question = "What is the parental leave policy?"
response = qa({"query": question})
print(f"Assistant: {response['result']}")
print(f"Sources: {[doc.metadata['source'] for doc in response['source_documents']]}")
```

---

### **Phase 5: Streamlit UI Development (Days 10–11)**

**Deliverable:** Live chat interface

**Features:**
- [ ] Chat input/output display
- [ ] Conversation history
- [ ] Source document display
- [ ] Confidence score / relevance

**Streamlit Code:**
```python
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

st.title("HR Assistant Chatbot")
st.write("Ask me anything about company policies!")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Load vector DB
@st.cache_resource
def load_vectordb():
    embeddings = OpenAIEmbeddings()
    vectordb = Chroma(
        persist_directory="./chroma_db",
        embedding_function=embeddings
    )
    return vectordb

vectordb = load_vectordb()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if user_input := st.chat_input("Ask a question..."):
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Get RAG response
    llm = ChatOpenAI(model_name="gpt-3.5-turbo")
    from langchain.chains import RetrievalQA
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectordb.as_retriever(),
        return_source_documents=True
    )
    
    response = qa({"query": user_input})
    assistant_message = response["result"]
    
    # Display assistant response
    st.session_state.messages.append({"role": "assistant", "content": assistant_message})
    with st.chat_message("assistant"):
        st.markdown(assistant_message)
        
        # Show sources
        with st.expander("Sources"):
            for doc in response["source_documents"]:
                st.write(f"**{doc.metadata['source']}**")
                st.write(doc.page_content)
```

---

### **Phase 6: Testing & Evaluation (Days 12–13)**

**Deliverable:** Evaluation report with test cases

**Evaluate:**
- [ ] Accuracy of answers (manual review)
- [ ] Relevance of retrieved documents
- [ ] Conversation quality
- [ ] Error handling
- [ ] Response time

**Test Cases:**
```
Test Case 1: Direct question
Q: "How many vacation days do I get?"
Expected: Answer with specific number
Result: ✓ Passed

Test Case 2: Follow-up question
Q: "What about sick days?"
Expected: Answer based on chat history
Result: ✓ Passed

Test Case 3: Out-of-domain question
Q: "What's the capital of France?"
Expected: "I don't have that information"
Result: ✓ Passed
```

---

### **Phase 7: Presentation (Day 14)**

**Demo:** Live chatbot interaction with 3–4 questions

---

## 📁 GITHUB REPO STRUCTURE

```
hr-chatbot/
├── README.md
├── requirements.txt
├── data/
│   └── documents/
│       ├── handbook.pdf
│       ├── faq.txt
│       └── benefits_guide.pdf
├── src/
│   ├── rag.py           # RAG pipeline
│   ├── chatbot.py       # Chatbot logic
│   └── utils.py
├── chroma_db/           # Vector database
├── app.py               # Streamlit app
├── .streamlit/
│   └── secrets.toml     # API keys
└── tests/
    ├── test_retrieval.py
    └── test_responses.py
```

---

---

# 💼 PROJECT OPTION 3: BUSINESS AUTOMATION SOLUTION

**Emphasis:** AI APIs, workflow automation, business value  
**Skills Demonstrated:** API integration, Zapier/Make, prompt engineering  
**Complexity:** Beginner to intermediate  
**Team Size:** Individual or pair  

---

## 🎯 PROJECT OVERVIEW

**Goal:** Automate a real business process using AI tools & APIs

**Example Projects:**

1. **Automated Email Generation System**
   - Input: Customer data → Output: Personalized emails
   - Automation: Email sent automatically via Zapier
   
2. **Report Automation**
   - Collect data → Generate insight report → Email to stakeholders
   
3. **Customer Support Automation**
   - Incoming customer emails → Categorize → Auto-respond to FAQs
   
4. **Social Media Content Generation**
   - Input: Product info → Output: Instagram captions → Auto-post
   
5. **Lead Qualification System**
   - New leads → AI scores + categorizes → Alerts sales team

---

## 📋 PROJECT REQUIREMENTS

### **Phase 1: Business Problem Identification (Days 1)**

**Deliverable:** Problem statement & ROI calculation

**Include:**
- [ ] Current manual process (hours/month)
- [ ] Pain points
- [ ] Proposed AI solution
- [ ] ROI calculation (time saved × hourly rate)
- [ ] Implementation timeline

**Example:**
```
PROBLEM:
Marketing team manually writes personalized email to 200 leads/month.
Time: 5 hours/week × 4 weeks = 20 hours/month
Cost: 20 hours × ৳500/hour = ৳10,000/month

SOLUTION:
Use ChatGPT API + Zapier to auto-generate emails
Time to implement: 2 days
Manual review: 1 hour/month (quality check)

ROI:
Monthly time saved: 19 hours = ৳9,500
Payback period: 1 day (implementation cost ≈ ৳1000)
Annual savings: ৳114,000
```

---

### **Phase 2: Workflow Design (Days 2–3)**

**Deliverable:** Workflow diagram & documentation

**Document:**
- [ ] Inputs (data source)
- [ ] Processing steps (AI + logic)
- [ ] Outputs (action taken)
- [ ] Error handling
- [ ] Approval process (if needed)

**Zapier Workflow Example:**
```
1. Trigger: New lead in Google Sheets
2. Action 1: Extract lead data
3. Action 2: Call ChatGPT API → Generate email
4. Action 3: Log to Airtable (audit trail)
5. Action 4: Send email via Gmail
6. Condition: If email fails → Alert on Slack
```

---

### **Phase 3: Implementation (Days 4–10)**

**Deliverable:** Working automation

**Build:**
- [ ] Set up Zapier/Make account
- [ ] Create workflow / automation
- [ ] Connect APIs (ChatGPT, Gmail, Slack, etc.)
- [ ] Test with sample data
- [ ] Error handling & logging

**Code Example (Python):**
```python
from openai import OpenAI
import pandas as pd

client = OpenAI(api_key="sk-...")

# Load leads
leads = pd.read_csv("leads.csv")

# Generate personalized emails
for idx, lead in leads.iterrows():
    prompt = f"""
    Write a personalized email to {lead['name']} 
    about {lead['product_interest']}.
    Keep it short (3-4 sentences).
    Add a CTA.
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    email_body = response.choices[0].message.content
    
    # Send email (or save for review)
    print(f"To: {lead['email']}")
    print(f"Body:\n{email_body}\n")
    
    # Save to file
    with open(f"emails/{lead['email']}.txt", "w") as f:
        f.write(email_body)
```

---

### **Phase 4: Testing & Optimization (Days 11–12)**

**Deliverable:** Test report with metrics

**Test:**
- [ ] Quality of outputs (manual review)
- [ ] Accuracy of automation
- [ ] Error rates
- [ ] Performance metrics
- [ ] Cost analysis

**Sample Metrics:**
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Email generation time | <30 seconds | 15 seconds | ✓ |
| Email quality score | 80%+ | 87% | ✓ |
| Error rate | <1% | 0.5% | ✓ |
| Cost per email | <৳2 | ৳1.50 | ✓ |

---

### **Phase 5: Presentation (Day 13)**

**Demo:** Live workflow execution (trigger → output)

---

---

# 🤝 PROJECT OPTION 4: REAL COMPANY PROJECT

**Emphasis:** Real-world problem solving  
**Skills Demonstrated:** Everything!  
**Complexity:** High  
**Team Size:** Individual or pair  

---

## 🎯 PROJECT OVERVIEW

**Goal:** Partner with a real company to solve a genuine AI/data problem

**Partner Companies:** (AAI will provide list)
- Company A: Predict customer churn
- Company B: Build AI chatbot for support
- Company C: Optimize pricing strategy
- Company D: Analyze market trends

---

## 📋 PROJECT REQUIREMENTS

**Same as Options 1–3, but:**
- [ ] Work with real company data (NDA signed)
- [ ] Real business metrics & KPIs
- [ ] Present to company stakeholders
- [ ] Solution deployed in production (possibly)
- [ ] Letter of recommendation from company

**Bonus:** High chance of job offer post-project!

---

---

# 📊 CAPSTONE PROJECT SUBMISSION CHECKLIST

**DUE: Week 5, Sunday, 11:59 PM**

### **GitHub Repo**
- [ ] README.md (project overview + setup instructions)
- [ ] All source code (.py files)
- [ ] Jupyter notebooks (EDA, modeling, etc.)
- [ ] requirements.txt (dependencies)
- [ ] Data samples (if possible, for reproducibility)
- [ ] Deployed app link (Streamlit Cloud, Heroku, etc.)

### **Documentation**
- [ ] Problem statement
- [ ] Data description
- [ ] Methodology
- [ ] Results & findings
- [ ] Conclusions
- [ ] Future improvements

### **Presentation Materials**
- [ ] 10-minute presentation slides (PDF)
- [ ] Video demo (3–5 minutes, optional but recommended)
- [ ] Live app/demo link

### **Code Quality**
- [ ] Clean, readable code
- [ ] Comments & docstrings
- [ ] No hardcoded values
- [ ] Follows Python conventions (PEP 8)
- [ ] Reproducible (others can run it)

---

## 🏆 GRADING SUMMARY

**Final Grade = 30% Technical + 20% Creativity + 15% Code + 15% Presentation + 20% Completeness**

**Passing: 70%+**

---

**Document Version:** 1.0  
**Status:** Ready for Student Assignment  
**Last Updated:** March 4, 2026
