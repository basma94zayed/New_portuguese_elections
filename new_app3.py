import streamlit as st
import pandas as pd
import joblib
def app():
    model=joblib.load("XGModel.h5")
    st.title("PORTUGUESE ELECTIONS RESULTS")
    st.header(" my prediction for final representative of every district in parliamentary elections ")
    
    st.write(" this is project discribes evolution parliamentary election results in 2019 ")
    totalMandates=st.number_input("totalMandates",value=0)
    availableMandates=st.number_input("availableMandates",value=0)
    numParishes=st.number_input("numParishes",value=0)
    numParishesApproved=st.number_input("numParishesApproved",value=0)
    blankVotes=st.number_input("blankVotes",value=0)
    nullVotes=st.number_input("nullVotes",value=0)
    subscribedVoters=st.number_input("subscribedVoters",value=0)
    lastblankVotes=st.number_input("pre.blankVotes",value=0)
    lastnullVotes=st.number_input("pre.nullVotes",value=0)
    lastsubscribedVoters=st.number_input("pre.subscribedVoters",value=0)
    Votes=st.number_input("Votes",value=0)
    Percentage_partyvotes=st.number_input("Percentage",value=0.0)




    Predict= st.button("Predict")
    if Predict:
        df=pd.DataFrame.from_dict({
            
            "totalMandates":[totalMandates],
            "availableMandates":[availableMandates],
            "numParishes":[numParishes],
            "numParishesApproved":[numParishesApproved],
            "blankVotes":[blankVotes],
            "nullVotes":[nullVotes],
            "subscribedVoters":[subscribedVoters],
            "pre.blankVotes":[lastblankVotes],
            "pre.nullVotes":[lastnullVotes],
            "pre.subscribedVoters":[lastsubscribedVoters],
            "Votes":[Votes],
            "Percentage_partyvotes":Percentage_partyvotes


        })

        
        st.dataframe(df)
        prediction=model.predict(df)
        st.write(f"prediction = {prediction}")
app()
