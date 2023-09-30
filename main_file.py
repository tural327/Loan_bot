my_key_ip = "6332261623:AAE4Xbr1Xv5Mg4Uwpx9oW4g57EkMuySHbMs"
from telegram import Update
from telegram.ext import *
import pickle
import math
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np




with open('random_forest_model.pkl', 'rb') as file:
    random_forest_model = pickle.load(file)

with open('max_numbers.pkl', 'rb') as file:
    max_numbers = pickle.load(file)

with open('cloumn_name.pkl', 'rb') as file:
    cloumn_name = pickle.load(file)




# training values
no_of_dependents = [0]
loan_term = [0]
cibil_score = [0]
residential_assets_value = [0]
commercial_assets_value = [0]
luxury_assets_value = [0]
bank_asset_value = [0]
income_annum_log = [0]
loan_amount_log = [0]
education_0_1 = [0]   #0 Graduate 1 not Graduate
self_employed_0_1 = [0] # 0 yes 1 no


# prediton model
def my_prediction(no_of_dependents,loan_term,cibil_score,residential_assets_value,commercial_assets_value,luxury_assets_value,bank_asset_value,income_annum_log,loan_amount_log,education_0_1,self_employed_0_1):
    no_of_dependents = no_of_dependents / 5
    loan_term = loan_term / 20
    cibil_score = cibil_score / 900
    residential_assets_value  = residential_assets_value / 29100000
    commercial_assets_value = commercial_assets_value / 19400000
    luxury_assets_value = luxury_assets_value / 39200000
    bank_asset_value = bank_asset_value / 14700000
    income_annum_log = math.log(income_annum_log) / 16.10804531510
    loan_amount_log = math.log(loan_amount_log) / 17.49181122987135

    if education_0_1 == "Graduate":
        education = 0
    elif education_0_1 == "Not Graduate":
        education = 1
    if self_employed_0_1 == 'No':
        self_employed = 0
    elif self_employed_0_1 == 'Yes':
        self_employed = 1

    result = [no_of_dependents,loan_term, cibil_score, residential_assets_value, commercial_assets_value, luxury_assets_value, bank_asset_value, income_annum_log, loan_amount_log, education, self_employed]

    result = pd.DataFrame(result).T
    result = random_forest_model.predict(result)  
    result = np.round(result)
    result = int(result[0])

    if result==0:
        main_resunt = 'Approved'
    if result == 1:
        main_resunt = 'Rejected'
    
    return main_resunt


### quesion asking


async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salam ! baslamaq ucun sadece 'start' yaz")

async def make_all_zero(update:Update,context:ContextTypes.DEFAULT_TYPE):
    no_of_dependents = [0]
    loan_term = [0]
    cibil_score = [0]
    residential_assets_value = [0]
    commercial_assets_value = [0]
    luxury_assets_value = [0]
    bank_asset_value = [0]
    income_annum_log = [0]
    loan_amount_log = [0]
    education_0_1 = [0]   #0 Graduate 1 not Graduate
    self_employed_0_1 = [0] # 0 yes 1 no
    await update.message.reply_text("her sey sifirlandi yeniden baslaya bilersen")

async def handle(update:Update,context:ContextTypes.DEFAULT_TYPE):

    text: str = update.message.text
    if text=='start':
        await update.message.reply_text("please provide to us your the number of dependents of the applicant")
    elif text.isdigit() and no_of_dependents[0]==0:
        no_of_dependents[0] = int(text)
        await update.message.reply_text(f"Great!  The number of dependents of the applicant {text} acceppted! now please provide  the number of dependents of the applicant")
    elif text.isdigit() and loan_term[0]==0:
        loan_term[0] = int(text)
        await update.message.reply_text(f"Cool!  the number of dependents of the applicant {text} acceppted! now please provide credit score of the applicant")
    elif text.isdigit() and cibil_score[0]==0:
        cibil_score[0] = int(text)
        await update.message.reply_text(f"Good job  Credit score of the applicant {text} acceppted! now please provide the total value of the applicant's residential assets")
    elif text.isdigit() and residential_assets_value[0]==0:
        residential_assets_value[0] = int(text)
        await update.message.reply_text(f"great  the total value of the applicant's residential assets. {text} acceppted! now please provide  the total value of the applicant's commercial assets")
    elif text.isdigit() and commercial_assets_value[0]==0:
        commercial_assets_value[0] = int(text)
        await update.message.reply_text(f"You are doing good job! The total value of the applicant's commercial assets {text} acceppted! now please provide the total value of the applicant's luxury assets")
    elif text.isdigit() and luxury_assets_value[0]==0:
        luxury_assets_value[0] = int(text)
        await update.message.reply_text(f"Dont worry almost done! and we acceppted the total value of the applicant's luxury assets as {text}now please provide the total value of the applicant's bank assets")
    elif text.isdigit() and bank_asset_value[0]==0:
        bank_asset_value[0] = int(text)
        await update.message.reply_text(f"Well I got it ! so your  the total value of the applicant's bank assets is {text}Please provide the annual income of the applicant")
    elif text.isdigit() and income_annum_log[0]==0:
        income_annum_log[0] = int(text)
        await update.message.reply_text(f"Perfect! The annual income of the applicant is {text} can I ask your the total amount requested for the loan ?")
    elif text.isdigit() and loan_amount_log[0]==0:
        loan_amount_log[0] = int(text)
        await update.message.reply_text(f"Your the total amount requested for the loan is {text}Please provide your edducation level, either Graduate or Not Graduate")
    elif  education_0_1[0]==0:
        if text=="Graduate" or text == "Not Graduate":
            education_0_1[0] = str(text)
            await update.message.reply_text(f"The last one either if the applicant is self employed or not (Yes/No)")
        else:
            await update.message.reply_text("Zehmet olmasa telebe uygun davranin")
    if self_employed_0_1[0]==0:
        if text=="Yes" or text == "No":
            self_employed_0_1[0] = str(text)
            await update.message.reply_text(f"Let me thing about your credit application")
            result_text = my_prediction(no_of_dependents[0],loan_term[0],cibil_score[0],residential_assets_value[0],commercial_assets_value[0],luxury_assets_value[0],bank_asset_value[0],income_annum_log[0],loan_amount_log[0],education_0_1[0],self_employed_0_1[0])
            await update.message.reply_text(f"Your credit request was {result_text}")
            await update.message.reply_text("Start from top! /make_zero_all press!")

if __name__ == '__main__':
    app = Application.builder().token(my_key_ip).build()
    app.add_handler(CommandHandler('start',start))
    app.add_handler(CommandHandler('make_zero_all',make_all_zero))

    app.add_handler(MessageHandler(filters.TEXT,handle))
    print("working.....")
    app.run_polling(poll_interval=1)
            
